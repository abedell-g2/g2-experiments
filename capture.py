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

    return content

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
