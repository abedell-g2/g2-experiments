# G2 Design Experiments

Static HTML experiments for G2 UI/UX exploration, built from real page code.

**Live site:** https://abedell-g2.github.io/g2-experiments/

## How it works

Each experiment is a static HTML snapshot of a real G2 page with:
- Real compiled CSS (`nessy_app.css` + Elevate CSS) from the UE codebase
- Realistic data (no live API calls)
- An experiment banner linking back to this index

Converting an experiment back to production-ready ERB is minimal — the HTML structure maps 1:1 to the Slim templates.

## Adding a new experiment

1. Fetch a real page from your local `g2.test` instance
2. Run the transform script to clean up dev assets and swap in new data
3. Add a card to `index.html`
4. Push — GitHub Pages auto-deploys

## Asset updates

CSS files in `assets/` are compiled from the UE repo. To update them:
```bash
cp ~/Developer/ue/public/assets/nessy_app.css ./assets/nessy_app.css
cp ~/Developer/ue/engines/elevate/public/elevate-assets/application.css ./assets/elevate.css
```
