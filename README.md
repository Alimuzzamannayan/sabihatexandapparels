# Sabiha Tex & Apparels — Website

Source for [sabihatexandapparels.com](https://sabihatexandapparels.com) — a Dhaka-based
apparel sourcing and buying house.

## Pages
`index.html` (home), `about.html`, `services.html`, `products.html`,
`mens.html`, `womens.html`, `kids.html`, `home-textiles.html`,
`quality.html`, `contact.html`, `404.html`.
`coming-soon.html` is the previous animated placeholder, kept for reference.

## How the pages are built
The header, footer and shared blocks live in `tools/build.py` so they are not
copy-pasted across eleven files. Edit the content there, then regenerate:

```
python tools/build.py
```

That rewrites the `.html` files plus `sitemap.xml` and `robots.txt`.
The generated files are committed — GitHub Pages serves them directly, there is
no build step on deploy. If you hand-edit an `.html` file, re-running the script
will overwrite it, so make the change in `tools/build.py` instead.

## Assets
- `assets/css/style.css` — all styling (no framework)
- `assets/js/site.js` — mobile menu, scroll reveal, enquiry form (opens the visitor's mail app)
- `assets/img/` — photographs, CC0 licence via [Openverse](https://openverse.org) (no attribution required)

## Contact details used on the site
Email smtsajib25@gmail.com · Mobile +8801925256616, +8801725256616
Corporate office: 122/123 (1st Floor), Darus Salam, Mirpur Road, Dhaka-1216
Main branch: Atpara, PO Kaliratpara, Upazila & Zilla: Munshiganj

## Hosting
- GitHub Pages from `main` (root), custom domain via `CNAME`
- DNS, TLS certificate and `www` handling on Cloudflare (SSL mode Full, Always Use HTTPS)
- `www.sabihatexandapparels.com` is served without redirect by the Cloudflare Worker `sabiha-www`

## Local preview
```
python -m http.server 8111
```
then open http://localhost:8111
