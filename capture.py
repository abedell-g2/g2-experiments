#!/usr/bin/env python3
"""
Capture a G2 product page from g2.test as a static experiment.
Usage: python3 capture.py <product-slug> [--out <dir>]
Example: python3 capture.py kinfolk-platform
"""

import urllib.request, urllib.error, ssl, re, sys, os, argparse, html

BASE = "https://www.g2.test"
GITHUB_BASE = "https://abedell-g2.github.io/g2-experiments"
EXPERIMENT_BANNER = '''<div style="background: #5746b2; color: white; text-align: center; padding: 8px 16px; font-size: 13px; font-family: Figtree, sans-serif; font-weight: 600; position: sticky; top: 0; z-index: 9999;">
  🧪 G2 Experiment — Product Page: {name} &nbsp;·&nbsp; <a href="../index.html" style="color: white; text-decoration: underline;">Back to Experiments</a>
</div>'''

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch(url, turbo_frame=None):
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "text/html"}
    if turbo_frame:
        headers["Turbo-Frame"] = turbo_frame
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
        return r.read().decode("utf-8")

def extract_turbo_frame(html_content, frame_id):
    pattern = rf'<turbo-frame id="{frame_id}">(.*?)</turbo-frame>'
    m = re.search(pattern, html_content, re.DOTALL)
    return m.group(1) if m else None

def transform(content, slug, product_name):
    # Fix asset paths: local dev -> g2.com CDN
    content = content.replace('href="https://www.g2.test/assets/', 'href="https://www.g2.com/assets/')
    content = content.replace('src="https://www.g2.test/assets/', 'src="https://www.g2.com/assets/')
    content = re.sub(r'src="/assets/', 'src="https://www.g2.com/assets/', content)
    content = re.sub(r'href="/assets/', 'href="https://www.g2.com/assets/', content)

    # Fix product images: dev CloudFront -> production CDN
    content = content.replace('https://d3cat1s0n6zlx1.cloudfront.net', 'https://images.g2crowd.com')

    # Fix CSS references to use local copies
    content = re.sub(r'href="https://www\.g2\.com/assets/nessy_app[^"]*"', 'href="../assets/nessy_app.css"', content)
    content = re.sub(r'href="/elevate-assets/application[^"]*"', 'href="../assets/elevate.css"', content)
    content = re.sub(r'href="https://www\.g2\.test/assets/nessy_app[^"]*"', 'href="../assets/nessy_app.css"', content)
    content = re.sub(r'href="https://www\.g2\.test/elevate-assets[^"]*"', 'href="../assets/elevate.css"', content)

    # Fix elevate JS to load from g2.com CDN instead of broken root-relative path
    content = content.replace('src="/elevate-assets/application.js"',
                              'src="https://www.g2.com/elevate-assets/application.js"')

    # Resolve deferred images: replace placeholder GIFs with real src from data-deferred-image-src
    # G2's deferred-image Stimulus controller sets src from data-deferred-image-src on load;
    # without elevate.js this never fires, leaving all images as transparent GIFs.
    content = _fix_deferred_images(content)

    # Rewrite remaining g2.test URLs to github pages
    content = re.sub(r'https://www\.g2\.test/', f'{GITHUB_BASE}/', content)
    content = re.sub(r'https://g2\.test/', f'{GITHUB_BASE}/', content)

    # Fix canonical URL
    content = re.sub(r'<link rel="canonical"[^>]*/?>',
                     f'<link rel="canonical" href="{GITHUB_BASE}/product-page/index.html">',
                     content)

    # Inject experiment banner after <body
    banner = EXPERIMENT_BANNER.format(name=product_name)
    content = re.sub(r'(<body[^>]*>)', r'\1' + banner, content)

    # Remove scripts that would fail (analytics, live reloaders, etc.)
    content = re.sub(r'<script[^>]*data-turbo-track[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    # Remove browsersync dev artifact
    content = re.sub(r'<script[^>]*browsersync[^>]*></script>', '', content)

    return content


def _fix_deferred_images(content):
    """Replace placeholder transparent GIFs with real URLs from data-deferred-image-src.

    G2 uses a deferred-image Stimulus controller that sets img.src from
    data-deferred-image-src after the page loads. On a static page without
    elevate.js, this never fires, leaving every logo/screenshot as a transparent
    GIF. This function bakes the real src in at capture time.
    """
    PLACEHOLDERS = ('transparent-ad5be28fb', 'ffffff-68c7675')
    new_content = content
    offset = 0

    for m in re.finditer(r'data-deferred-image-src="([^"]+)"', content):
        real_src = m.group(1)
        pos = m.start() + offset

        # Scan back up to 2000 chars for the last placeholder src= before this attr
        search_start = max(0, pos - 2000)
        chunk = new_content[search_start:pos]

        placeholder_m = None
        for pm in re.finditer(r'src="[^"]*(?:' + '|'.join(PLACEHOLDERS) + r')[^"]*"', chunk):
            placeholder_m = pm

        if placeholder_m:
            abs_start = search_start + placeholder_m.start()
            abs_end = search_start + placeholder_m.end()
            new_src = f'src="{real_src}"'
            new_content = new_content[:abs_start] + new_src + new_content[abs_end:]
            offset += len(new_src) - (placeholder_m.end() - placeholder_m.start())

    # Remove the now-redundant deferred attributes
    new_content = re.sub(r'\s*data-deferred-image-src="[^"]*"', '', new_content)
    new_content = re.sub(r'\s*ue="\s*deferred-image\s*"', '', new_content)
    new_content = re.sub(r'(?<=ue=") ?deferred-image ?', '', new_content)
    new_content = new_content.replace(' ue=""', '')

    return new_content

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", help="Product slug, e.g. kinfolk-platform")
    parser.add_argument("--out", default=None, help="Output directory (default: product-page/)")
    parser.add_argument("--name", default=None, help="Product display name for banner")
    args = parser.parse_args()

    slug = args.slug
    out_dir = args.out or os.path.join(os.path.dirname(__file__), "product-page")
    os.makedirs(out_dir, exist_ok=True)

    print(f"Fetching {BASE}/products/{slug}/reviews ...")
    try:
        page = fetch(f"{BASE}/products/{slug}/reviews")
    except urllib.error.HTTPError as e:
        print(f"Error fetching page: {e}")
        sys.exit(1)

    # Extract product name from title
    product_name = args.name
    if not product_name:
        m = re.search(r'<title>([^|<]+)', page)
        if m:
            product_name = m.group(1).strip().replace(' Reviews 2026', '').replace(' Reviews', '').strip()
        else:
            product_name = slug.replace('-', ' ').title()
    print(f"Product: {product_name}")

    # Check if reviews frame is populated
    frame_content = extract_turbo_frame(page, "reviews-and-filters")
    frame_size = len(frame_content) if frame_content else 0
    print(f"Reviews frame size in main page: {frame_size} chars")

    # If reviews frame is small (empty), fetch it separately
    if frame_size < 10000:
        print(f"Fetching reviews frame separately from /products/{slug}/reviews_and_filters ...")
        try:
            frame_page = fetch(f"{BASE}/products/{slug}/reviews_and_filters")
            new_frame = extract_turbo_frame(frame_page, "reviews-and-filters")
            if new_frame and len(new_frame) > frame_size:
                print(f"Got larger reviews frame: {len(new_frame)} chars — injecting into page")
                page = page.replace(
                    f'<turbo-frame id="reviews-and-filters">{frame_content}</turbo-frame>',
                    f'<turbo-frame id="reviews-and-filters">{new_frame}</turbo-frame>'
                )
            else:
                print("Reviews frame still empty — reviews may not be indexed in ES")
        except Exception as e:
            print(f"Warning: could not fetch reviews frame: {e}")

    # Transform
    print("Transforming asset URLs and injecting banner...")
    page = transform(page, slug, product_name)

    # Write
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w") as f:
        f.write(page)

    size_kb = os.path.getsize(out_path) // 1024
    print(f"Written to {out_path} ({size_kb}KB)")

if __name__ == "__main__":
    main()
