# chanmo.github.io

A single static page. No build step, no framework, no trackers.

- `index.html` — the whole site, CSS inline
- `404.html` — shown for any missing path (uses root-relative asset URLs)
- `blog/index.html` — sends visitors from the former blog address to the homepage
- `favicon.svg`, `apple-touch-icon.png`, `og.png` — tab icon, iOS home-screen icon, share card
- `fonts/` — Inter 400/500 and Inter Display 500, subset to Latin (SIL OFL, see `fonts/OFL.txt`)
- `.nojekyll` — serve files as-is

To change something: edit the HTML, commit, push. GitHub Pages serves the repository root.

The previous Jekyll blog (2022–2023) remains in Git history.
