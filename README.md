# Sabiha Tex & Apparels — Website

Source for [sabihatexandapparels.com](https://sabihatexandapparels.com).

Currently serving an animated "We are cooking something" coming-soon page
(textile & apparel items rising out of a dye pot).

## Stack
- Static HTML/CSS/SVG (no build step) — `index.html`
- Hosted on GitHub Pages (`CNAME` → sabihatexandapparels.com)
- DNS + SSL/TLS via Cloudflare (proxied, SSL mode Full, Always Use HTTPS)
- `www.sabihatexandapparels.com` is served (no redirect) by the Cloudflare Worker
  `sabiha-www` on route `www.sabihatexandapparels.com/*`, which proxies to the
  root domain, because GitHub Pages supports only one custom domain

## Local preview
Open `index.html` in a browser, or run `npx serve .`
