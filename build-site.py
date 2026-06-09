import os, re

SITE_DIR = "/sessions/gifted-friendly-edison/mnt/BT Articles Word/bogey-train-site"
ARTICLES_DIR = os.path.join(SITE_DIR, "articles")

# The rich green from the current site
GREEN = "#73775b"
GREEN_LIGHT = "#8a8e6f"
GREEN_DARK = "#5c5f49"
GREEN_BG = "#f4f5f0"
GREEN_BORDER = "#d4d6c8"

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --green: """ + GREEN + """;
  --green-light: """ + GREEN_LIGHT + """;
  --green-dark: """ + GREEN_DARK + """;
  --green-bg: """ + GREEN_BG + """;
  --green-border: """ + GREEN_BORDER + """;
  --text: #1a1a1a;
  --text-secondary: #555;
  --text-caption: #777;
  --bg: #fff;
  --max-width: 720px;
  --max-width-wide: 960px;
}

body {
  font-family: Georgia, 'Times New Roman', serif;
  color: var(--text);
  background: var(--bg);
  line-height: 1.75;
  font-size: 17px;
  -webkit-font-smoothing: antialiased;
}

/* NAV */
.site-nav {
  max-width: var(--max-width-wide);
  margin: 0 auto;
  padding: 1.5rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid var(--green);
}
.site-nav .logo { height: 50px; }
.site-nav .nav-links { display: flex; gap: 2rem; }
.site-nav .nav-links a {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 14px;
  letter-spacing: 0.5px;
  text-decoration: none;
  color: var(--text-secondary);
  text-transform: uppercase;
}
.site-nav .nav-links a:hover { color: var(--green); }

/* HOMEPAGE */
.home-header {
  max-width: var(--max-width-wide);
  margin: 0 auto;
  padding: 3rem 2rem 1rem;
}
.home-header h1 {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 13px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--green);
  font-weight: 400;
}

.featured-article {
  max-width: var(--max-width-wide);
  margin: 0 auto;
  padding: 1.5rem 2rem 2.5rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2.5rem;
  align-items: center;
}
.featured-article .featured-text .category {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--green);
  margin-bottom: 0.75rem;
}
.featured-article .featured-text h2 {
  font-size: 28px;
  line-height: 1.25;
  margin-bottom: 0.75rem;
  font-weight: 400;
}
.featured-article .featured-text h2 a {
  color: var(--text);
  text-decoration: none;
}
.featured-article .featured-text h2 a:hover { color: var(--green-dark); }
.featured-article .featured-text .excerpt {
  font-size: 15px;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 0.5rem;
}
.featured-article .featured-text .meta {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 12px;
  color: var(--text-caption);
}
.featured-article .featured-img img {
  width: 100%;
  height: 280px;
  object-fit: cover;
  border-radius: 4px;
}

.article-list {
  max-width: var(--max-width-wide);
  margin: 0 auto;
  padding: 0 2rem 3rem;
  border-top: 1px solid var(--green-border);
}
.article-list-item {
  display: flex;
  gap: 1.25rem;
  align-items: center;
  padding: 1.25rem 0;
  border-bottom: 1px solid #eee;
  text-decoration: none;
  color: inherit;
}
.article-list-item:hover h3 { color: var(--green-dark); }
.article-list-item .thumb {
  width: 80px;
  height: 60px;
  object-fit: cover;
  border-radius: 3px;
  flex-shrink: 0;
}
.article-list-item h3 {
  font-size: 17px;
  font-weight: 400;
  margin-bottom: 3px;
  transition: color 0.2s;
}
.article-list-item .subtitle {
  font-size: 13px;
  color: var(--text-caption);
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

/* ARTICLE PAGE */
.article-header {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 3rem 2rem 1.5rem;
  text-align: center;
}
.article-header .category {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--green);
  margin-bottom: 1rem;
}
.article-header h1 {
  font-size: 34px;
  line-height: 1.2;
  font-weight: 400;
  margin-bottom: 1rem;
}
.article-header .meta {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 13px;
  color: var(--text-caption);
}

.article-body {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 2rem 4rem;
}
.article-body p {
  margin-bottom: 1.25rem;
}
.article-body strong {
  font-weight: 700;
}
.article-body em {
  font-style: italic;
}
.article-body img {
  max-width: 100%;
  height: auto;
  margin: 1.5rem 0;
  border-radius: 3px;
}
.article-body blockquote, .article-body .pullquote {
  border-left: 3px solid var(--green);
  padding: 1rem 1.5rem;
  margin: 2rem 0;
  font-style: italic;
  color: var(--text-secondary);
  background: var(--green-bg);
}
.article-body a {
  color: var(--green-dark);
  text-decoration: underline;
  text-decoration-color: var(--green-border);
  text-underline-offset: 2px;
}
.article-body a:hover {
  color: var(--green);
}
.article-body h2, .article-body h3, .article-body strong:only-child {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
.article-body h2 {
  font-size: 22px;
  font-weight: 500;
  margin: 2.5rem 0 1rem;
  color: var(--green-dark);
}
.article-body hr {
  border: none;
  border-top: 2px solid var(--green);
  margin: 2rem auto;
  width: 60px;
}

/* Captions: italic paragraphs right after images */
.article-body .caption {
  font-size: 13px;
  color: var(--text-caption);
  font-style: italic;
  margin-top: -0.75rem;
  margin-bottom: 1.5rem;
}

/* ABOUT PAGE */
.about-content {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 3rem 2rem 4rem;
}
.about-content h1 {
  font-size: 28px;
  font-weight: 400;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--green);
}
.about-content p {
  margin-bottom: 1.25rem;
}

/* FOOTER */
.site-footer {
  max-width: var(--max-width-wide);
  margin: 0 auto;
  padding: 2rem;
  border-top: 2px solid var(--green);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 13px;
  color: var(--text-caption);
}
.site-footer .social a {
  color: var(--text-caption);
  text-decoration: none;
  margin-left: 1.5rem;
}
.site-footer .social a:hover { color: var(--green); }

/* RESPONSIVE */
@media (max-width: 700px) {
  .featured-article { grid-template-columns: 1fr; gap: 1.5rem; }
  .featured-article .featured-img { order: -1; }
  .featured-article .featured-text h2 { font-size: 22px; }
  .article-header h1 { font-size: 26px; }
  .site-nav, .home-header, .featured-article, .article-list,
  .article-body, .about-content, .site-footer { padding-left: 1.25rem; padding-right: 1.25rem; }
}
"""

def nav_html(current="home"):
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="{css_path}style.css">
  <link rel="icon" href="{img_path}images/logo.png" type="image/png">
</head>
<body>
  <nav class="site-nav">
    <a href="{root}index.html"><img src="{img_path}images/logo.png" alt="The Bogey Train" class="logo"></a>
    <div class="nav-links">
      <a href="{root}index.html">Articles</a>
      <a href="{root}about.html">About</a>
    </div>
  </nav>
"""

def footer_html():
    return """
  <footer class="site-footer">
    <span>A golf architecture journal by Sam Collett</span>
    <div class="social">
      <a href="https://twitter.com/bogeytrains" target="_blank" rel="noopener">X</a>
      <a href="https://www.instagram.com/the_bogey_train/" target="_blank" rel="noopener">Instagram</a>
    </div>
  </footer>
</body>
</html>
"""

# ARTICLES DATA
articles = [
    {
        "slug": "erin-hills",
        "title": "The Tempestuous Charmer: A Review of Erin Hills",
        "subtitle": "A review of one of Wisconsin's most storied courses",
        "category": "Review",
        "excerpt": "There are few negative feelings to have against Erin Hills. Though chaos and turnover have covered its history, the layout and design of the course remain engrossing.",
        "date": "Sam Collett",
        "thumb": "images/articles/erin-hills/media/image2.png",
        "hero": "images/articles/erin-hills/media/image2.png",
        "featured": True,
    },
    {
        "slug": "mid-round-lull",
        "title": "An Antidote to the Mid-Round Lull",
        "subtitle": "Four courses with exceptional middle stretches",
        "category": "Architecture",
        "excerpt": "Every course seeks to provide a compelling opening and closing hole. However, one of the least-discussed portions of a round integral to a player's enjoyment is the middle.",
        "date": "Sam Collett",
        "thumb": "images/articles/mid-round-lull/media/image3.png",
    },
    {
        "slug": "baseball-stadiums",
        "title": "Baseball Stadiums & Golf Architecture",
        "subtitle": "A curious comparison",
        "category": "Architecture",
        "excerpt": "The parallels are not as ridiculous as one might presume.",
        "date": "Sam Collett",
        "thumb": "images/articles/baseball-stadiums/media/image1.png",
    },
    {
        "slug": "kinsale",
        "title": "Hanse, Wagner Design MacRaynor-Inspired Kinsale Golf Club",
        "subtitle": "A template-driven development in Naples, Florida",
        "category": "News",
        "excerpt": "Gil Hanse and Jim Wagner expanded their portfolio with a Macdonald/Raynor-inspired private club outside Naples.",
        "date": "Sam Collett",
        "thumb": "images/articles/kinsale/media/image4.png",
    },
    {
        "slug": "rustic-canyon",
        "title": "An Appreciation of Rustic Canyon's Front Nine",
        "subtitle": "The less interesting, interesting nine",
        "category": "Architecture",
        "excerpt": "Often golfers become so overwhelmed by standout holes on a course that they lose appreciation for the more subtle ones.",
        "date": "Sam Collett",
        "thumb": "images/articles/rustic-canyon/media/image1.png",
    },
]

# Write CSS
with open(os.path.join(SITE_DIR, "style.css"), "w") as f:
    f.write(CSS)

# BUILD INDEX
featured = articles[0]
rest = articles[1:]

index_body = nav_html("home").format(
    title="The Bogey Train — A Golf Architecture Journal",
    css_path="", img_path="", root=""
)
index_body += f"""
  <section class="featured-article">
    <div class="featured-text">
      <div class="category">{featured['category']}</div>
      <h2><a href="articles/{featured['slug']}.html">{featured['title']}</a></h2>
      <p class="excerpt">{featured['excerpt']}</p>
      <p class="meta">{featured['date']}</p>
    </div>
    <div class="featured-img">
      <a href="articles/{featured['slug']}.html">
        <img src="{featured['hero']}" alt="{featured['title']}">
      </a>
    </div>
  </section>

  <section class="article-list">
"""
for a in rest:
    index_body += f"""    <a href="articles/{a['slug']}.html" class="article-list-item">
      <img src="{a['thumb']}" alt="{a['title']}" class="thumb">
      <div>
        <h3>{a['title']}</h3>
        <span class="subtitle">{a['subtitle']}</span>
      </div>
    </a>
"""
index_body += "  </section>\n"
index_body += footer_html()

with open(os.path.join(SITE_DIR, "index.html"), "w") as f:
    f.write(index_body)

# BUILD ABOUT PAGE
about_body = nav_html("about").format(
    title="About — The Bogey Train",
    css_path="", img_path="", root=""
)
about_body += """
  <div class="about-content">
    <h1>About The Bogey Train</h1>

    <p>The Bogey Train is an independent golf architecture journal written by Sam Collett. The site examines golf courses as works of art, evaluating them on compositional merit: routing logic, strategic design, pacing, aesthetic integration, and the relationship between a course and the land it occupies.</p>

    <p>Golf architecture criticism borrows from the same evaluative frameworks used in film, music, and literature. A course's middle stretch can be assessed the way a film's second act is; a routing can be studied the way an album's sequencing is. The best designs reveal their identity through subtlety, and this site attempts to uncover those qualities through close analysis.</p>

    <p>The articles here explore specific courses, design principles, and the occasional cross-domain comparison. Whether it is the front nine at Rustic Canyon, the mid-round brilliance of Ballybunion, or the parallels between baseball stadiums and golf holes, the through-line is the same: what makes a design work, and why?</p>

    <p>Sam is based in the United States and can be found on <a href="https://twitter.com/bogeytrains">X</a> and <a href="https://www.instagram.com/the_bogey_train/">Instagram</a>.</p>
  </div>
"""
about_body += footer_html()

with open(os.path.join(SITE_DIR, "about.html"), "w") as f:
    f.write(about_body)

print("Built: index.html, about.html, style.css")

# BUILD ARTICLE PAGES
for a in articles:
    slug = a["slug"]
    raw_path = os.path.join(ARTICLES_DIR, f"{slug}-raw.html")
    
    with open(raw_path, "r") as f:
        raw = f.read()
    
    # Clean up the raw HTML:
    # 1. Remove the title (first <p><strong>...</strong></p>)
    raw = re.sub(r'^<p><strong>[^<]+</strong></p>\s*', '', raw, count=1)
    
    # 2. Remove auto-generated alt text descriptions
    raw = re.sub(r' alt="[^"]*Description automatically generated[^"]*"', ' alt=""', raw)
    raw = re.sub(r' alt="[^"]*Description automatically generated with[^"]*"', ' alt=""', raw)
    
    # 3. Clean up inline styles on images (remove width/height, let CSS handle it)
    raw = re.sub(r' style="width:[^"]*"', '', raw)
    
    # 4. Convert bold-only paragraphs to h2
    raw = re.sub(r'<p><strong>([^<]+)</strong>\s*</p>', r'<h2>\1</h2>', raw)
    # Handle bold with trailing space or quotes
    raw = re.sub(r'<p><strong>([^<]+)</strong>\s*"?\s*</p>', r'<h2>\1</h2>', raw)
    
    # 5. Convert horizontal rules
    raw = raw.replace('<hr />', '<hr>')
    
    # 6. Fix italic caption paragraphs after images
    # If a paragraph is entirely italic and short, mark it as caption
    def mark_captions(html):
        lines = html.split('\n')
        result = []
        prev_was_img = False
        for line in lines:
            is_img = '<img ' in line and '</p>' in line
            if prev_was_img and line.startswith('<p><em>') and '</em></p>' in line:
                line = line.replace('<p><em>', '<p class="caption"><em>')
            if is_img or (prev_was_img and '<img' in line):
                prev_was_img = True
            else:
                prev_was_img = False
            if '<img ' in line:
                prev_was_img = True
            result.append(line)
        return '\n'.join(result)
    
    raw = mark_captions(raw)
    
    # Build the page
    page = nav_html("article").format(
        title=f"{a['title']} — The Bogey Train",
        css_path="../", img_path="../", root="../"
    )
    page += f"""
  <header class="article-header">
    <div class="category">{a['category']}</div>
    <h1>{a['title']}</h1>
    <p class="meta">{a['date']}</p>
  </header>

  <article class="article-body">
{raw}
  </article>
"""
    page += footer_html().replace('href="index', 'href="../index').replace('href="about', 'href="../about')
    
    out_path = os.path.join(ARTICLES_DIR, f"{slug}.html")
    with open(out_path, "w") as f:
        f.write(page)
    
    print(f"Built: articles/{slug}.html")

# Clean up raw files
import glob
for f in glob.glob(os.path.join(ARTICLES_DIR, "*-raw.html")):
    os.remove(f)
    
print("\nAll pages built!")
