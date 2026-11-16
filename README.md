# FreedomPoint website

Static site for https://freedompoint.app (English at `/`, Spanish at `/es/`).

- Edit copy in `build.py`, then run `python3 build.py` to regenerate every HTML page, `sitemap.xml`, `robots.txt` and `CNAME`.
- Styles are shared in `style.css`. Screenshots live in `img/en/` and `img/es/` (taken from the app with fictional demo data).
- When the app is live, set `APP_STORE_URL` in `build.py` and rebuild: the "Coming soon" buttons become download links.
- Preview locally: `python3 -m http.server 8765` and open http://localhost:8765/
