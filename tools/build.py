#!/usr/bin/env python3
"""Builds the static pages of sabihatexandapparels.com.

Every page shares one header/footer, so they live here instead of being
copy-pasted into eleven HTML files. Run `python tools/build.py` from the
repository root after editing; the generated .html files are committed.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.sabihatexandapparels.com"
EMAIL = "smtsajib25@gmail.com"
PHONE1 = "+8801925256616"
PHONE2 = "+8801725256616"
WHATSAPP = "8801925256616"
CORP = "122/123 (1st Floor), Darus Salam, Mirpur Road, Dhaka-1216, Bangladesh"
BRANCH = "Atpara, PO Kaliratpara, Upazila &amp; Zilla: Munshiganj, Bangladesh"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("products.html", "Products"),
    ("quality.html", "Quality"),
    ("contact.html", "Contact"),
]

LOGO = """<svg viewBox="0 0 48 48" aria-hidden="true">
        <circle cx="24" cy="24" r="23" fill="#16204d"/>
        <path d="M15.5 31.5c2.5 2.7 5.4 3.7 8.8 3.7 4.4 0 7.7-2.3 7.7-6 0-7.3-14.9-4.8-14.9-11.5 0-2.9 2.7-4.9 6.4-4.9 2.8 0 5.1 1 6.8 2.8" fill="none" stroke="#f4eee0" stroke-width="3.1" stroke-linecap="round"/>
        <path d="M9 24h30" stroke="#dfa63a" stroke-width="1.9" stroke-dasharray="3 3"/>
      </svg>"""

ICON_PIN = '<svg viewBox="0 0 24 24"><path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24"><path d="M5 3h4l2 5-2.5 1.5a12 12 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
ICON_CLOCK = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5.5l3.5 2"/></svg>'

WA_SVG = ('<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C8.8 3 3 8.8 3 16c0 2.3.6 4.5 1.7 6.4L3 29l6.8-1.8A13 13 0 1 0 16 3zm0 23.6c-2.1 0-4.1-.6-5.9-1.6l-.4-.2-4 1 1.1-3.9-.3-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-1.8-.9-3-1.6-4.2-3.6-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.6l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-1.2 1.2-1.2 2.9-.1 4.6 1.1 1.7 2.4 3.9 5.9 5.4 2.3 1 3.2 1.1 4.3.9.7-.1 1.9-.8 2.2-1.6.3-.8.3-1.4.2-1.6-.1-.1-.3-.2-.6-.3z"/></svg>')


def head(title, desc, canonical, og_image="assets/img/hero-sewing.jpg", extra=""):
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="canonical" href="{site}/{canonical}" />
<meta name="theme-color" content="#16204d" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Sabiha Tex &amp; Apparels" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="{site}/{canonical}" />
<meta property="og:image" content="{site}/{og}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="assets/css/style.css" />
{extra}</head>
<body>""".format(title=title, desc=desc, site=SITE, canonical=canonical, og=og_image, extra=extra)


def header(active):
    links = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        links += '      <a href="{h}"{c}>{l}</a>\n'.format(h=href, c=cur, l=label)
    return """
<div class="topbar">
  <div class="wrap">
    <span>Apparel sourcing &amp; buying house &middot; Dhaka, Bangladesh</span>
    <span><a href="mailto:{email}">{email}</a> &nbsp;|&nbsp; <a href="tel:{p1}">{p1}</a></span>
  </div>
</div>

<header class="site">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Sabiha Tex &amp; Apparels — home">
      {logo}
      <span><b>Sabiha Tex &amp; Apparels</b><small>Textile &middot; Apparel Sourcing</small></span>
    </a>
    <button class="burger" aria-expanded="false" aria-controls="menu" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="main" id="menu">
{links}      <a class="btn nav-cta" href="contact.html">Send an enquiry</a>
    </nav>
  </div>
</header>
""".format(email=EMAIL, p1=PHONE1, logo=LOGO, links=links)


def footer():
    return """
<footer class="site">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="index.html" style="margin-bottom:16px">
          {logo}
          <span><b>Sabiha Tex &amp; Apparels</b><small>Textile &middot; Apparel Sourcing</small></span>
        </a>
        <p style="color:#aeb5d4;max-width:38ch">A Dhaka-based buying house for apparel, knitwear, denim and home textiles — from supplier selection to shipment.</p>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="quality.html">Quality &amp; compliance</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Products</h4>
        <ul>
          <li><a href="mens.html">Men's apparel</a></li>
          <li><a href="womens.html">Women's apparel</a></li>
          <li><a href="kids.html">Kids' apparel</a></li>
          <li><a href="home-textiles.html">Home textiles &amp; fabrics</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <address>
          <strong style="color:#fff">Corporate office</strong><br />
          {corp}<br /><br />
          <strong style="color:#fff">Main branch</strong><br />
          {branch}<br /><br />
          <a href="tel:{p1}">{p1}</a> &middot; <a href="tel:{p2}">{p2}</a><br />
          <a href="mailto:{email}">{email}</a>
        </address>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="yr">2026</span> Sabiha Tex &amp; Apparels. All rights reserved.</span>
      <span>Photographs: CC0 stock via Openverse</span>
    </div>
  </div>
</footer>

<a class="float-wa" href="https://wa.me/{wa}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{wasvg}</a>
<script src="assets/js/site.js"></script>
</body>
</html>
""".format(logo=LOGO, corp=CORP, branch=BRANCH, p1=PHONE1, p2=PHONE2, email=EMAIL, wa=WHATSAPP, wasvg=WA_SVG)


def hero(img, eyebrow, h1, text, buttons="", chips=None, compact=False, crumbs=""):
    chip_html = ""
    if chips:
        chip_html = '\n    <div class="chips">' + "".join("<span>%s</span>" % c for c in chips) + "</div>"
    return """
<section class="hero{cl}">
  <img class="bg" src="{img}" alt="" />
  <div class="wrap">
    {crumbs}<p class="eyebrow light">{eyebrow}</p>
    <h1>{h1}</h1>
    <p>{text}</p>{chips}
    {buttons}
  </div>
</section>
""".format(cl=" compact" if compact else "", img=img, eyebrow=eyebrow, h1=h1, text=text,
           chips=chip_html, buttons=buttons, crumbs=crumbs)


def crumb(label):
    return '<p class="crumbs"><a href="index.html">Home</a> / %s</p>\n    ' % label


def cta_band(title="Ready to place your next order in Bangladesh?",
             text="Send us your tech pack, sketch or sample reference. We will come back with factory options, a sample plan and a costing."):
    return """
<section class="cta-band">
  <div class="wrap reveal">
    <div>
      <h2>{t}</h2>
      <p>{x}</p>
    </div>
    <div class="btn-row" style="margin:0">
      <a class="btn light" href="contact.html">Send an enquiry</a>
      <a class="btn outline-light" href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp us</a>
    </div>
  </div>
</section>
""".format(t=title, x=text, wa=WHATSAPP)


def cards(items, cls="g3"):
    out = '<div class="grid %s">' % cls
    for i, (num, title, text) in enumerate(items, 1):
        out += """
  <article class="card reveal" style="transition-delay:{d}ms">
    <span class="num">{n}</span>
    <h3>{t}</h3>
    <p>{x}</p>
  </article>""".format(d=(i % 4) * 70, n=num, t=title, x=text)
    return out + "\n</div>"


def mcards(items):
    out = '<div class="grid g4">'
    for i, (href, img, kicker, title, text) in enumerate(items):
        out += """
  <a class="mcard reveal" style="transition-delay:{d}ms" href="{h}">
    <img src="{img}" alt="{t}" loading="lazy" />
    <div class="cap"><span>{k}</span><h3>{t}</h3><p>{x}</p></div>
  </a>""".format(d=i * 80, h=href, img=img, k=kicker, t=title, x=text)
    return out + "\n</div>"


def items_grid(items):
    out = '<div class="items">'
    for i, (img, title, text) in enumerate(items):
        out += """
  <article class="item reveal" style="transition-delay:{d}ms">
    <img src="{img}" alt="{t}" loading="lazy" />
    <div class="body"><h3>{t}</h3><p>{x}</p></div>
  </article>""".format(d=(i % 3) * 80, img=img, t=title, x=text)
    return out + "\n</div>"


def steps(items):
    out = '<ol class="steps">'
    for i, (title, text) in enumerate(items, 1):
        out += """
  <li class="reveal"><span class="idx">{i:02d}</span><div><h3>{t}</h3><p>{x}</p></div></li>""".format(
            i=i, t=title, x=text)
    return out + "\n</ol>"


def faq(items):
    out = '<div class="faq">'
    for q, a in items:
        out += """
  <details><summary>{q}</summary><p>{a}</p></details>""".format(q=q, a=a)
    return out + "\n</div>"


def ticks(items):
    return '<ul class="ticks">' + "".join("<li>%s</li>" % i for i in items) + "</ul>"


def tags(items):
    return '<div class="taglist">' + "".join("<span>%s</span>" % i for i in items) + "</div>"


# ---------------------------------------------------------------- page bodies

PROCESS = [
    ("Enquiry &amp; tech pack", "You send a sketch, tech pack, sample or a reference photo with your target quantity and delivery window."),
    ("Factory selection", "We shortlist units that actually run your product type &mdash; knit, woven, denim, sweater or home textile &mdash; and that meet the audit standards your brand asks for."),
    ("Sampling &amp; development", "Fabric and trim sourcing, proto, fit and salesman samples, lab dips and strike-offs, revised until the sample is approved."),
    ("Costing &amp; order placement", "A transparent, item-wise costing. Once you approve, we place the order and confirm the production schedule with the factory."),
    ("Production follow-up", "We stay on the floor: fabric in-house, cutting, sewing lines, washing and finishing, with regular updates and photos to you."),
    ("Inspection", "Pre-production, inline and final random inspections against your approved sample and AQL, plus measurement and packing checks."),
    ("Shipment &amp; documents", "Booking with your nominated forwarder, carton marking, and the export documents your bank or customs broker needs."),
]

SERVICES = [
    ("01", "Supplier identification", "We match every enquiry with factories that genuinely run that product, capacity and price level, instead of pushing one unit for everything."),
    ("02", "Sample development", "Proto, fit, size set and salesman samples, lab dips, strike-offs and trim cards &mdash; followed up until your approval."),
    ("03", "Costing &amp; negotiation", "Item-wise costing on fabric, trims, CM and finishing so you can see what you pay for, and negotiation on your behalf."),
    ("04", "Order follow-up", "Daily contact with merchandisers and production managers, with a written status so you know where every style stands."),
    ("05", "Quality control", "Pre-production meetings, inline checks and final random inspection to your AQL, with photo reports."),
    ("06", "Compliance coordination", "We arrange factory audits and paperwork for the social and technical standards your buyer or brand requires."),
    ("07", "Private label &amp; packaging", "Labels, hangtags, polybags, cartons and barcode work prepared to your artwork and retailer manual."),
    ("08", "Shipping &amp; documents", "Booking, inspection certificates, invoices, packing lists and export documentation handled with your forwarder."),
]

FAQ_HOME = [
    ("What exactly does a buying house do?",
     "We work on the buyer's side. You tell us what you want made; we find the right factory, develop the samples, negotiate the price, watch production on the floor, inspect the goods and get them shipped. You deal with one office in Dhaka instead of chasing several factories."),
    ("What products can you source?",
     "Knit and woven garments for men, women and kids &mdash; t-shirts, polos, shirts, jeans and denim, chinos, shorts, sweatshirts, sweaters and outerwear &mdash; plus home textiles such as bed linen, and woven and knit fabrics."),
    ("Do you work with new or small brands?",
     "Yes. Quantities, fabric and finishing decide which factory fits, so send your details and we will tell you honestly whether we can place the order well."),
    ("How do I start?",
     "Send a tech pack, sketch, photo or physical sample with your target quantity, fabric and delivery date to " + EMAIL + " or message us on WhatsApp. We reply with factory options and a sample plan."),
    ("Can you follow the compliance standards our brand requires?",
     "Yes. Tell us which audits and standards you need the factory to hold &mdash; for example BSCI, Sedex, WRAP, OEKO-TEX or GOTS &mdash; and we shortlist units accordingly and share their current certificates."),
    ("Who controls quality before shipment?",
     "Our own team inspects at the factory: pre-production, during the sewing run and a final random inspection against the approved sample and your AQL, with a written and photo report before the goods leave."),
]


def page_home():
    return "".join([
        hero(
            "assets/img/hero-sewing.jpg",
            "Apparel sourcing &amp; buying house &middot; Dhaka",
            "Your sourcing office on the factory floor in Bangladesh",
            "Sabiha Tex &amp; Apparels is a Dhaka-based buying house. We find the right factory for your order, develop your samples, follow the production line every day and ship your goods with the documents in order.",
            buttons='<div class="btn-row"><a class="btn light" href="contact.html">Send an enquiry</a><a class="btn outline-light" href="services.html">What we do</a></div>',
            chips=["Knitwear", "Woven", "Denim", "Sweaters", "Kids' wear", "Home textiles"],
        ),
        """
<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Who we are</p>
      <h2>One office between your brand and the sewing line</h2>
      <p class="lede" style="margin-top:16px">Buying from Bangladesh works when somebody is in the factory every week &mdash; checking fabric, measuring samples and pushing the schedule. That is the job we do for you.</p>
      <p style="margin-top:14px">We are a textile and apparel sourcing house based at Darus Salam, Dhaka, with a branch office in Munshiganj. We work with knit, woven, denim, sweater and home-textile units, and we choose the unit to suit your product, quantity and compliance requirements &mdash; not the other way round.</p>
      """ + ticks([
            "A single point of contact for sampling, production and shipment",
            "Item-wise costing you can read line by line",
            "Written production updates with photographs from the floor",
            "Inspection before any carton leaves the factory",
        ]) + """
      <div class="btn-row"><a class="btn ghost" href="about.html">About our company</a></div>
    </div>
    <figure class="reveal">
      <div class="stack-img">
        <img src="assets/img/fabric-rolls.jpg" alt="Rolls of fabric stacked in a textile warehouse" loading="lazy" />
        <img src="assets/img/tshirts-folded.jpg" alt="Stack of folded t-shirts" loading="lazy" />
        <img src="assets/img/handshake.jpg" alt="Two people shaking hands over a meeting table" loading="lazy" />
      </div>
    </figure>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">What we do</p>
      <h2>Sourcing services, end to end</h2>
      <p>From the first enquiry to the shipping documents, every step of your order is handled and reported by one team.</p>
    </div>
    """ + cards([(n, t, x) for n, t, x in SERVICES[:6]]) + """
    <div class="btn-row"><a class="btn ghost" href="services.html">All services in detail</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Product range</p>
      <h2>What we source</h2>
      <p>Knit and woven apparel for the whole family, plus home textiles and fabric. Tell us the product and we will tell you which of our units builds it best.</p>
    </div>
    """ + mcards([
            ("mens.html", "assets/img/mens-model.jpg", "Category 01", "Men's apparel", "T-shirts, polos, shirts, denim, chinos, knitwear and outerwear."),
            ("womens.html", "assets/img/womens-hangers.jpg", "Category 02", "Women's apparel", "Tops, blouses, dresses, skirts, denim, knitwear and loungewear."),
            ("kids.html", "assets/img/kids-baby.jpg", "Category 03", "Kids' apparel", "Baby sets, t-shirts, dresses, school wear, knitwear and outerwear."),
            ("home-textiles.html", "assets/img/home-pillows.jpg", "Category 04", "Home textiles &amp; fabrics", "Bed linen, towels, cushion covers, woven and knit fabric, yarn and trims."),
        ]) + """
  </div>
</section>

<section class="section ink">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow light">How we work</p>
      <h2>From your tech pack to the shipping mark</h2>
      <p>A straight line of seven steps. You are told where your order stands at each one.</p>
    </div>
    """ + steps(PROCESS) + """
  </div>
</section>

<section class="section">
  <div class="wrap split rev">
    <div class="reveal">
      <p class="eyebrow">Quality &amp; compliance</p>
      <h2>Checked on the floor, not on paper</h2>
      <p class="lede" style="margin-top:16px">Quality control is the part of sourcing that cannot be done by email. Our team measures, counts and opens cartons at the factory.</p>
      """ + ticks([
            "Pre-production meeting so the factory and the approved sample agree",
            "Inline checks while the sewing lines are running",
            "Final random inspection to your AQL with a photo report",
            "Measurement, shade, trim, barcode and carton checks before loading",
            "Factories shortlisted against the audits your brand requires",
        ]) + """
      <div class="btn-row"><a class="btn ghost" href="quality.html">Our quality process</a></div>
    </div>
    <figure class="reveal"><img src="assets/img/measuring.jpg" alt="Measuring tapes used for garment inspection" loading="lazy" /></figure>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Questions</p>
      <h2>Frequently asked</h2>
    </div>
    """ + faq(FAQ_HOME) + """
  </div>
</section>
""",
        cta_band(),
    ])


def page_about():
    return "".join([
        hero("assets/img/fabric-store.jpg", "About us",
             "A buying house built on follow-up",
             "Sabiha Tex &amp; Apparels sources apparel, knitwear, denim and home textiles from Bangladesh for buyers who want one responsible partner on the ground.",
             compact=True, crumbs=crumb("About")),
        """
<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Our company</p>
      <h2>Who we are</h2>
      <p style="margin-top:16px">Sabiha Tex &amp; Apparels is a textile and apparel sourcing company based in Dhaka, Bangladesh, with a corporate office at Darus Salam on Mirpur Road and a main branch in Munshiganj.</p>
      <p style="margin-top:14px">We act as a buying house: we represent the buyer, not the factory. Our work starts when you send a tech pack or a sample, and it ends when your cartons are loaded with the documents complete. In between we select the unit, develop samples, agree the costing, follow the line and inspect the goods.</p>
      <p style="margin-top:14px">Bangladesh offers a deep base of knit, woven, denim and sweater manufacturing. The difficulty for an overseas buyer is knowing which unit suits a given product and then keeping that order on schedule. That is exactly the gap we fill.</p>
    </div>
    <figure class="reveal"><img src="assets/img/team-meeting.jpg" alt="Team reviewing an order at a meeting table" loading="lazy" /></figure>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">How we work</p>
      <h2>Four habits our buyers rely on</h2>
    </div>
    """ + cards([
            ("Principle 01", "We represent the buyer", "Our job is your price, your quality and your delivery date. We tell you plainly when a factory, a price or a lead time is not realistic."),
            ("Principle 02", "We stay on the floor", "Sampling and production are followed in person at the unit, not managed from a desk by email alone."),
            ("Principle 03", "We write everything down", "Costings, sample comments, inspection findings and shipment status go to you in writing, with photographs."),
            ("Principle 04", "We fit the factory to the order", "Different products need different units. We shortlist for your product type, quantity and compliance needs."),
        ], "g4") + """
  </div>
</section>

<section class="section">
  <div class="wrap split rev">
    <div class="reveal">
      <p class="eyebrow">What we handle</p>
      <h2>The scope of our service</h2>
      <p style="margin-top:16px">Everything below sits with us, so your team can stay on design and selling.</p>
      """ + ticks([
            "Factory search, capacity check and sample evaluation",
            "Fabric, yarn, trim and accessory sourcing",
            "Costing, negotiation and order placement",
            "Production planning and daily follow-up",
            "In-process and final quality inspection",
            "Labels, packing, carton marking and barcodes",
            "Shipment booking and export documentation",
        ]) + """
      <div class="btn-row"><a class="btn ghost" href="services.html">See the full service list</a></div>
    </div>
    <figure class="reveal"><img src="assets/img/sewing-line.jpg" alt="Operator working at an industrial sewing machine" loading="lazy" /></figure>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Find us</p>
      <h2>Our offices</h2>
    </div>
    <div class="grid g2">
      <article class="card reveal">
        <span class="num">Corporate office</span>
        <h3>Darus Salam, Dhaka</h3>
        <p>""" + CORP + """</p>
        <div class="btn-row" style="margin-top:18px"><a class="btn ghost" href="contact.html">Contact this office</a></div>
      </article>
      <article class="card reveal" style="transition-delay:90ms">
        <span class="num">Main branch</span>
        <h3>Munshiganj</h3>
        <p>""" + BRANCH + """</p>
        <div class="btn-row" style="margin-top:18px"><a class="btn ghost" href="contact.html">Contact this office</a></div>
      </article>
    </div>
  </div>
</section>
""",
        cta_band("Tell us what you want to produce",
                 "Send your tech pack or a sample reference. We will reply with factory options, a sampling plan and an indicative costing."),
    ])


def page_services():
    return "".join([
        hero("assets/img/tshirts-hanging.jpg", "Services",
             "Sourcing, sampling, production and shipment",
             "Eight services that cover the full distance between your first enquiry and the container leaving Chattogram.",
             compact=True, crumbs=crumb("Services")),
        """
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Service list</p>
      <h2>What we take off your desk</h2>
      <p>Take all of it, or only the parts you need &mdash; some buyers use us purely for inspection and follow-up of orders they placed themselves.</p>
    </div>
    """ + cards(SERVICES, "g2") + """
  </div>
</section>

<section class="section ink">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow light">Order journey</p>
      <h2>How an order runs with us</h2>
    </div>
    """ + steps(PROCESS) + """
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Materials</p>
      <h2>Fabrics and techniques we source</h2>
      <p style="margin-top:16px">We develop in the fabrics your product needs and arrange the washes, prints and embellishment that go with them.</p>
      """ + tags([
            "Single jersey", "Pique", "Interlock", "Rib", "Fleece &amp; terry", "Slub &amp; melange",
            "Poplin", "Twill", "Oxford", "Canvas", "Corduroy", "Denim &amp; stretch denim",
            "Flannel", "Viscose &amp; rayon", "Linen blends", "Recycled polyester", "Organic cotton",
            "Enzyme &amp; stone wash", "Garment dye", "AOP &amp; screen print", "Embroidery", "Sublimation",
        ]) + """
    </div>
    <figure class="reveal"><img src="assets/img/fabric-plaid.jpg" alt="Woven check and twill fabric swatches" loading="lazy" /></figure>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Logistics</p>
      <h2>Packing, shipping and papers</h2>
      <p>The last mile decides whether an on-time order still arrives on time.</p>
    </div>
    """ + cards([
            ("Packing", "Retail-ready packing", "Polybags, hangtags, size strips, barcodes and carton marking prepared to your retailer's manual and checked before loading."),
            ("Booking", "Freight coordination", "We work with your nominated forwarder or arrange quotations, and coordinate the loading schedule with the factory."),
            ("Documents", "Export documentation", "Commercial invoice, packing list, inspection certificate and the certificates of origin your side needs for customs clearance."),
        ]) + """
  </div>
</section>
""",
        cta_band("Need a quotation?",
                 "Share the style, fabric, quantity and delivery window. You will get factory options and an item-wise costing you can compare."),
    ])


def page_products():
    return "".join([
        hero("assets/img/womens-jackets.jpg", "Products",
             "Apparel and textiles we source",
             "Knit and woven garments for men, women and kids, plus home textiles, fabric, yarn and trims.",
             compact=True, crumbs=crumb("Products")),
        """
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Categories</p>
      <h2>Four ranges, one sourcing office</h2>
      <p>Each range is produced in units chosen for that product type &mdash; a sweater order never goes to a basic t-shirt line.</p>
    </div>
    """ + mcards([
            ("mens.html", "assets/img/mens-model.jpg", "Range 01", "Men's apparel", "T-shirts, polos, shirts, jeans, chinos, knitwear, outerwear."),
            ("womens.html", "assets/img/womens-dress.jpg", "Range 02", "Women's apparel", "Tops, blouses, dresses, skirts, denim, knitwear, nightwear."),
            ("kids.html", "assets/img/kids-dress.jpg", "Range 03", "Kids' apparel", "Baby sets, tops, dresses, school wear, outerwear."),
            ("home-textiles.html", "assets/img/home-pillows.jpg", "Range 04", "Home textiles &amp; fabrics", "Bed linen, cushions, towels, woven and knit fabric, yarn."),
        ]) + """
  </div>
</section>

<section class="section tint">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Capabilities</p>
      <h2>Built to your specification</h2>
      <p style="margin-top:16px">Every style is developed against your tech pack, your approved sample and your size set. Where you do not have a tech pack, we can build one from a sketch or a reference garment.</p>
      """ + ticks([
            "Private label and own-brand production",
            "Fabric and trim development, including lab dips and strike-offs",
            "Washing, printing, embroidery and other value addition",
            "Size sets and grading to your market's fit",
            "Retail-ready packing to your manual",
        ]) + """
    </div>
    <figure class="reveal"><img src="assets/img/yarn.jpg" alt="Cones of coloured yarn" loading="lazy" /></figure>
  </div>
</section>
""",
        cta_band(),
    ])


def category_page(eyebrow, title, intro, hero_img, items, tag_list, note_title, note_text, crumb_label):
    return "".join([
        hero(hero_img, eyebrow, title, intro, compact=True, crumbs=crumb(crumb_label)),
        """
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Product types</p>
      <h2>""" + note_title + """</h2>
      <p>""" + note_text + """</p>
    </div>
    """ + items_grid(items) + """
    """ + tags(tag_list) + """
    <div class="btn-row"><a class="btn" href="contact.html">Enquire about this range</a><a class="btn ghost" href="products.html">All product ranges</a></div>
  </div>
</section>
""",
        cta_band(),
    ])


def page_mens():
    return category_page(
        "Men's apparel", "Men's knit, woven and denim",
        "Everyday basics through to outerwear, produced to your tech pack in units that run that product every day.",
        "assets/img/mens-model.jpg",
        [
            ("assets/img/tshirts-folded.jpg", "T-shirts &amp; polos", "Single jersey, pique, slub and melange in regular, slim and oversized fits, with print or embroidery."),
            ("assets/img/hangers.jpg", "Casual &amp; formal shirts", "Poplin, twill, oxford, flannel and linen blends, long and short sleeve, with your collar and cuff detailing."),
            ("assets/img/denim-pocket.jpg", "Jeans &amp; denim", "Rigid and stretch denim in your fit block, with enzyme, stone, bleach and tint washes."),
            ("assets/img/denim-jeans.jpg", "Chinos, trousers &amp; shorts", "Cotton twill, canvas and stretch chinos, cargo and swim shorts, to your waistband and pocketing spec."),
            ("assets/img/knitwear.jpg", "Sweaters &amp; knitwear", "Crew, v-neck, turtle neck, cable and fisherman rib in acrylic, cotton and wool blends at your gauge."),
            ("assets/img/knitwear-table.jpg", "Sweatshirts &amp; hoodies", "Brushed fleece and terry, zip and pull-over, with rib trims, drawcords and applied artwork."),
        ],
        ["Regular &amp; slim fits", "Oversized", "Garment dye", "Washes", "AOP", "Embroidery", "Reflective trims", "Workwear"],
        "Men's range", "Tell us the style and fabric; we will put it in the right unit and price it line by line.",
        "Men's apparel")


def page_womens():
    return category_page(
        "Women's apparel", "Women's knit, woven and denim",
        "Tops, dresses, denim and knitwear developed to your fit block and finished to your retail standard.",
        "assets/img/womens-model.jpg",
        [
            ("assets/img/womens-dress.jpg", "Tops &amp; blouses", "Knit tops, woven blouses and shirts in viscose, poplin, linen blends and printed fabrics."),
            ("assets/img/womens-hangers.jpg", "Dresses &amp; skirts", "Casual, printed and occasion styles with lining, trims and closures to your specification."),
            ("assets/img/denim-jeans.jpg", "Jeans &amp; trousers", "Stretch denim, twill and wide-leg styles, with your wash recipe and hardware."),
            ("assets/img/knitwear.jpg", "Knitwear &amp; cardigans", "Jumpers, cardigans and knitted dresses in your gauge, yarn blend and stitch pattern."),
            ("assets/img/womens-jackets.jpg", "Jackets &amp; outerwear", "Denim, padded and non-padded jackets, quilted and lined styles with branded hardware."),
            ("assets/img/hangers.jpg", "Nightwear &amp; loungewear", "Jersey, flannel and woven sets, robes and joggers for the lounge and sleep range."),
        ],
        ["Fit sampling", "Grading", "Lining &amp; interlining", "Lace &amp; trims", "Printed fabric", "Garment wash", "Occasion wear", "Basics"],
        "Women's range", "Send a reference garment or tech pack and we will build the fit sample first, then price the bulk.",
        "Women's apparel")


def page_kids():
    return category_page(
        "Kids' apparel", "Kids' and baby wear",
        "Safe, soft and correctly finished kids' clothing &mdash; produced with the trim and construction rules children's buyers demand.",
        "assets/img/kids-girl.jpg",
        [
            ("assets/img/kids-baby.jpg", "Baby sets &amp; bodysuits", "Soft jersey and interlock sets, rompers, bibs and sleepsuits with nickel-free snaps."),
            ("assets/img/kids-dress.jpg", "Girls' dresses &amp; skirts", "Printed and woven dresses, skirts and sets with lining, frills and safe closures."),
            ("assets/img/kids-girl.jpg", "T-shirts &amp; tops", "Jersey tees, polos and long sleeve tops with safe prints and envelope necks for small sizes."),
            ("assets/img/knitwear-table.jpg", "Sweatshirts &amp; knitwear", "Fleece sets, cardigans and jumpers in cotton and acrylic blends for school and play."),
            ("assets/img/womens-jackets.jpg", "Jackets &amp; outerwear", "Padded, fleece-lined and denim jackets built for daily wear and repeated washing."),
            ("assets/img/hangers.jpg", "School &amp; nightwear", "Uniform shirts, trousers, pinafores and pyjama sets in durable, easy-care fabric."),
        ],
        ["No loose small parts", "Nickel-free hardware", "Drawcord rules", "Flammability aware", "Soft hand feel", "Easy-care finish"],
        "Kids' range", "Children's wear carries extra rules on trims, cords and labelling &mdash; we build those into the sample stage, not after shipment.",
        "Kids' apparel")


def page_home_textiles():
    return category_page(
        "Home textiles &amp; fabrics", "Home textiles, fabric and yarn",
        "Bed linen, cushions and towels, plus greige and finished fabric, yarn and trims for buyers who source materials as well as garments.",
        "assets/img/home-pillows.jpg",
        [
            ("assets/img/home-pillows.jpg", "Bed linen &amp; cushions", "Sheets, duvet covers, pillow cases and cushion covers in cotton and poly-cotton, plain, printed or yarn-dyed."),
            ("assets/img/fabric-rolls.jpg", "Woven fabric", "Poplin, twill, oxford, canvas, flannel and denim &mdash; greige, dyed, printed or yarn-dyed to your sample."),
            ("assets/img/fabric-plaid.jpg", "Checks &amp; yarn-dyed", "Plaids, stripes and dobby constructions matched to your colour card and shrinkage standard."),
            ("assets/img/fabric-sari.jpg", "Printed &amp; speciality fabric", "Rotary, digital and pigment prints, plus textured and ethnic-inspired constructions."),
            ("assets/img/yarn.jpg", "Yarn &amp; trims", "Cotton, blended and fancy yarns, sewing thread, elastics, labels, buttons and zippers."),
            ("assets/img/packing.jpg", "Packing &amp; made-ups", "Folding, polybagging, header cards and retail packing for made-up home textile lines."),
        ],
        ["Cotton", "Poly-cotton", "Organic cotton", "Recycled fibre", "Yarn-dyed", "Rotary print", "Digital print", "Easy-care finish"],
        "Home textile &amp; fabric range", "Share a swatch or a specification &mdash; construction, GSM, width and finish &mdash; and we will source matching quality.",
        "Home textiles")


def page_quality():
    return "".join([
        hero("assets/img/measuring.jpg", "Quality &amp; compliance",
             "Inspected before it is shipped",
             "Quality control, factory compliance and documentation &mdash; handled at the unit by our own team.",
             compact=True, crumbs=crumb("Quality")),
        """
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Inspection</p>
      <h2>Four checkpoints on every order</h2>
      <p>Problems are cheap to fix at the sample stage and expensive after shipment, so we check early and often.</p>
    </div>
    """ + steps([
            ("Pre-production meeting", "Before cutting starts, the approved sample, tech pack, trim card and measurement sheet are reviewed with the factory team so everyone works to the same standard."),
            ("Fabric &amp; trim check", "Fabric is checked for shade, GSM, width, shrinkage and visible faults, and trims are matched against the approved trim card before bulk cutting."),
            ("Inline inspection", "While the lines run, we check measurements, stitching, shade continuity and workmanship so faults are caught within the same batch."),
            ("Final random inspection", "Finished, packed goods are inspected to your AQL &mdash; measurements, appearance, shade, trims, barcodes, cartons and shipping marks &mdash; with a written photo report before loading."),
        ]) + """
  </div>
</section>

<section class="section tint">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Compliance</p>
      <h2>Factories matched to your audit requirements</h2>
      <p style="margin-top:16px">Tell us which standards your brand or retailer requires, and we shortlist units that already hold them, then share their current certificates and audit dates with you.</p>
      """ + ticks([
            "Social audits such as BSCI, Sedex / SMETA and WRAP",
            "Product and chemical standards such as OEKO-TEX and GOTS for organic lines",
            "Fire, electrical and building safety documentation",
            "Factory profile, capacity and machinery list before you commit",
            "Third-party inspection welcome &mdash; we coordinate the visit",
        ]) + """
    </div>
    <figure class="reveal"><img src="assets/img/packing.jpg" alt="Warehouse packing and handling area" loading="lazy" /></figure>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Responsibility</p>
      <h2>Working with the factories, not around them</h2>
    </div>
    """ + cards([
            ("Fabric", "Lower-impact materials", "Where your range calls for it we develop in organic cotton, recycled polyester and other lower-impact fibres with the relevant transaction documents."),
            ("Waste", "Less waste per order", "Careful marker planning, fabric booking against real consumption and reuse of leftover fabric for samples and trials."),
            ("People", "Safe workplaces", "We place orders with units that can show current safety and social audit records, and we re-check them before repeat orders."),
        ]) + """
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Paperwork</p>
      <h2>Documents you receive</h2>
    </div>
    <div class="grid g2">
      <article class="card reveal">
        <h3>During production</h3>
        """ + ticks([
            "Approved sample comments and measurement sheets",
            "Fabric and trim in-house report",
            "Weekly production status with photographs",
            "Inline inspection findings and corrective actions",
        ]) + """
      </article>
      <article class="card reveal" style="transition-delay:90ms">
        <h3>At shipment</h3>
        """ + ticks([
            "Final inspection report with photographs",
            "Packing list and carton measurement details",
            "Commercial invoice and shipping documents",
            "Certificate of origin and test reports where required",
        ]) + """
      </article>
    </div>
  </div>
</section>
""",
        cta_band("Want our inspection service only?",
                 "If your order is already placed with a factory, we can run the inline and final inspections and report to you before shipment."),
    ])


def page_contact():
    map_q = "122/123+Darus+Salam+Mirpur+Road+Dhaka+1216+Bangladesh"
    return "".join([
        hero("assets/img/export-ship.jpg", "Contact",
             "Let's talk about your order",
             "Send a tech pack, a sketch or a sample reference with your quantity and delivery window. We reply with factory options, a sampling plan and a costing.",
             compact=True, crumbs=crumb("Contact")),
        """
<section class="section">
  <div class="wrap contact-grid">
    <div class="reveal">
      <p class="eyebrow">Our details</p>
      <h2>Sabiha Tex &amp; Apparels</h2>
      <div class="info-list">
        <div class="row">
          <span class="ic">""" + ICON_PIN + """</span>
          <div><h4>Corporate office</h4><address>""" + CORP + """</address></div>
        </div>
        <div class="row">
          <span class="ic">""" + ICON_PIN + """</span>
          <div><h4>Main branch</h4><address>""" + BRANCH + """</address></div>
        </div>
        <div class="row">
          <span class="ic">""" + ICON_PHONE + """</span>
          <div><h4>Mobile &amp; WhatsApp</h4>
            <a href="tel:""" + PHONE1 + '">' + PHONE1 + """</a>
            <a href="tel:""" + PHONE2 + '">' + PHONE2 + """</a>
          </div>
        </div>
        <div class="row">
          <span class="ic">""" + ICON_MAIL + """</span>
          <div><h4>Email</h4><a href="mailto:""" + EMAIL + '">' + EMAIL + """</a></div>
        </div>
        <div class="row">
          <span class="ic">""" + ICON_CLOCK + """</span>
          <div><h4>What to send</h4>
            <p style="font-size:15.3px;margin-top:2px">Tech pack or sketch, fabric details, quantity per colour and size, target price and delivery date.</p>
          </div>
        </div>
      </div>
      <div class="btn-row">
        <a class="btn" href="https://wa.me/""" + WHATSAPP + """" target="_blank" rel="noopener">Chat on WhatsApp</a>
        <a class="btn ghost" href="mailto:""" + EMAIL + """">Email us</a>
      </div>
    </div>

    <form class="enquiry reveal" novalidate>
      <h3 style="margin-bottom:6px">Send an enquiry</h3>
      <p style="font-size:14.6px;margin-bottom:20px">Fill this in and your email app opens with the details ready to send.</p>
      <div class="two">
        <div><label for="name">Your name *</label><input id="name" name="name" required /></div>
        <div><label for="company">Company</label><input id="company" name="company" /></div>
      </div>
      <div class="two">
        <div><label for="email">Email *</label><input id="email" name="email" type="email" required /></div>
        <div><label for="phone">Phone / WhatsApp</label><input id="phone" name="phone" /></div>
      </div>
      <div class="two">
        <div><label for="country">Country</label><input id="country" name="country" /></div>
        <div>
          <label for="category">Product category</label>
          <select id="category" name="category">
            <option>Men's apparel</option>
            <option>Women's apparel</option>
            <option>Kids' apparel</option>
            <option>Home textiles &amp; fabrics</option>
            <option>Inspection / QC only</option>
            <option>Other</option>
          </select>
        </div>
      </div>
      <label for="message">Your requirement *</label>
      <textarea id="message" name="message" placeholder="Style, fabric, quantity per colour and size, target price, delivery date" required></textarea>
      <button class="btn" type="submit" style="width:100%;justify-content:center">Send enquiry</button>
      <p class="form-note">This form opens your own email app. Nothing is stored on this website.</p>
    </form>
  </div>

  <div class="wrap">
    <div class="map reveal">
      <iframe title="Map of our corporate office at Darus Salam, Mirpur Road, Dhaka"
              src="https://www.google.com/maps?q=""" + map_q + """&output=embed"
              loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</section>
""",
    ])


def page_404():
    return """
<section class="section" style="padding-top:clamp(70px,10vw,130px)">
  <div class="wrap" style="max-width:720px;text-align:center">
    <p class="eyebrow" style="justify-content:center">Error 404</p>
    <h1>This page is not on the rail</h1>
    <p class="lede" style="margin:18px auto 0">The link may be old or mistyped. Try the main sections below, or write to us and we will point you to the right place.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="index.html">Back to home</a>
      <a class="btn ghost" href="contact.html">Contact us</a>
    </div>
  </div>
</section>
"""


ORG_JSONLD = """<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Sabiha Tex & Apparels",
  "url": "{site}/",
  "logo": "{site}/favicon.svg",
  "image": "{site}/assets/img/hero-sewing.jpg",
  "description": "Apparel and textile sourcing buying house in Dhaka, Bangladesh. Supplier selection, sampling, production follow-up, quality inspection and shipment.",
  "email": "{email}",
  "telephone": ["{p1}", "{p2}"],
  "address": [
    {{"@type": "PostalAddress", "streetAddress": "122/123 (1st Floor), Darus Salam, Mirpur Road", "addressLocality": "Dhaka", "postalCode": "1216", "addressCountry": "BD"}},
    {{"@type": "PostalAddress", "streetAddress": "Atpara, PO Kaliratpara", "addressLocality": "Munshiganj", "addressCountry": "BD"}}
  ],
  "areaServed": "Worldwide",
  "knowsAbout": ["apparel sourcing", "buying house", "knitwear", "woven garments", "denim", "home textiles"]
}}
</script>
""".format(site=SITE, email=EMAIL, p1=PHONE1, p2=PHONE2)

FAQ_JSONLD = """<script type="application/ld+json">
{{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{items}]}}
</script>
""".format(items=", ".join(
    '{{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}'.format(
        q=re.sub(r"&[a-z]+;", "", q).replace('"', "'"),
        a=re.sub(r"&[a-z]+;", "", a).replace('"', "'"))
    for q, a in FAQ_HOME))

PAGES = [
    ("index.html", "Sabiha Tex & Apparels — Apparel Sourcing &amp; Buying House in Bangladesh",
     "Sabiha Tex &amp; Apparels is a Dhaka-based apparel sourcing and buying house: supplier selection, sampling, costing, production follow-up, quality inspection and shipment for knitwear, woven, denim, kids' wear and home textiles.",
     page_home, ORG_JSONLD + FAQ_JSONLD),
    ("about.html", "About Us — Sabiha Tex &amp; Apparels",
     "A textile and apparel buying house in Dhaka, Bangladesh, representing overseas buyers from factory selection through to shipment.",
     page_about, ""),
    ("services.html", "Sourcing Services — Sabiha Tex &amp; Apparels",
     "Supplier identification, sample development, costing, production follow-up, quality control, compliance coordination, private label packaging and export documentation.",
     page_services, ""),
    ("products.html", "Products We Source — Sabiha Tex &amp; Apparels",
     "Men's, women's and kids' knit, woven and denim apparel, plus home textiles, fabric, yarn and trims sourced from Bangladesh.",
     page_products, ""),
    ("mens.html", "Men's Apparel Sourcing — Sabiha Tex &amp; Apparels",
     "T-shirts, polos, shirts, jeans and denim, chinos, shorts, sweaters, sweatshirts and outerwear for men, sourced and inspected in Bangladesh.",
     page_mens, ""),
    ("womens.html", "Women's Apparel Sourcing — Sabiha Tex &amp; Apparels",
     "Tops, blouses, dresses, skirts, denim, knitwear, outerwear and nightwear for women, developed to your fit block in Bangladesh.",
     page_womens, ""),
    ("kids.html", "Kids' &amp; Baby Wear Sourcing — Sabiha Tex &amp; Apparels",
     "Baby sets, t-shirts, dresses, school wear, knitwear and outerwear for children, produced with child-safe trims and construction.",
     page_kids, ""),
    ("home-textiles.html", "Home Textiles &amp; Fabric Sourcing — Sabiha Tex &amp; Apparels",
     "Bed linen, cushion covers, towels, woven and knit fabric, yarn and trims sourced from Bangladeshi mills and made-up units.",
     page_home_textiles, ""),
    ("quality.html", "Quality Control &amp; Compliance — Sabiha Tex &amp; Apparels",
     "Pre-production meetings, fabric checks, inline inspection and final random inspection to your AQL, plus factory compliance and documentation.",
     page_quality, ""),
    ("contact.html", "Contact — Sabiha Tex &amp; Apparels, Dhaka",
     "Corporate office at Darus Salam, Mirpur Road, Dhaka-1216 and main branch in Munshiganj. Call +8801925256616 or email smtsajib25@gmail.com.",
     page_contact, ""),
    ("404.html", "Page not found — Sabiha Tex &amp; Apparels",
     "The page you asked for does not exist on sabihatexandapparels.com.",
     page_404, ""),
]


def build():
    for filename, title, desc, body_fn, extra in PAGES:
        html = head(title, desc, filename, extra=extra) + header(filename) + body_fn() + footer()
        with open(os.path.join(ROOT, filename), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(html)
        print("wrote", filename, len(html) // 1024, "KB")

    urls = [p[0] for p in PAGES if p[0] != "404.html"]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = SITE + "/" + ("" if u == "index.html" else u)
        pri = "1.0" if u == "index.html" else "0.8"
        sitemap.append("  <url><loc>%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>" % (loc, pri))
    sitemap.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(sitemap) + "\n")

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
    print("wrote sitemap.xml, robots.txt")


if __name__ == "__main__":
    build()
