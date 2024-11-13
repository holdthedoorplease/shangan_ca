# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import date
import ablog

# Project information
project = 'ShangAn'
copyright = '2024, 上岸加拿大'
author = 'ShangAn'
release = '1.0.0'
language = 'zh'

# Insert '_extension' directory into the path so Sphinx can find it
sys.path.insert(0, os.path.abspath('_extension'))
sys.path.insert(0, os.path.abspath('scripts'))

html_baseurl = 'https://shangan.ca/'
html_extra_path = ['robots.txt']

# General configuration
extensions = [
    'myst_parser',
    'sphinx_design', 
    'gallery_directive',
    'component_directive',
    'ablog',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx_togglebutton',
    'sphinx_favicon',
    'sphinxcontrib.youtube',
    'sphinx.ext.autosectionlabel',
    'split_articles',
    'sphinx_sitemap'
]

autosectionlabel_prefix_document = True

# Path configurations
templates_path = ["_templates"]
html_static_path = ["_static"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# MyST options
myst_enable_extensions = ["colon_fence", "linkify", "substitution", "deflist", "html_image", "smartquotes"]
myst_heading_anchors = 2
myst_substitutions = {"rtd": "[Read the Docs](https://readthedocs.org/)"}

# Add Open Graph meta tags for SEO
myst_html_meta = {
    "og:title": "上岸加拿大",
    "og:description": "上岸加拿大，相聚枫叶国｜签证｜移民｜最全DIY教程",
    "og:image": "https://shangan.ca/_static/logo.svg",
    "og:type": "website",
    "robots": "index, follow",
    "twitter:card": "summary_large_image",
    "keywords": "加拿大移民, 签证, DIY教程, 上岸加拿大, 加拿大签证, 加拿大移民, 加拿大DIY教程, 学签, 工签, 旅游签, 探亲签, 超级签证, PR, EE, PNP, Webform, 安调, 调档, 强制令",
}

# ABlog settings
blog_basepath = 'news'
blog_path = 'news'
blog_post_pattern = 'news/articles/*/*/*.rst'
blog_feed_fulltext = True
blog_feed_subtitle = "Latest News and Updates"

blog_posts_per_page = 5
paginate_archived_posts = True

# Post related settings
post_auto_excerpt = 1
post_date_format = '%Y-%m-%d'
post_date_format_short = '%B %d, %Y'




# HTML output options
html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.ico"
html_title = "上岸加拿大"
 
html_theme_options = {
    "external_links": [
    ],
    "icon_links": [
        {"name": "Email", "url": "mailto:shanganjianada@gmail.com", "icon": "fa-solid fa-envelope"},
        {"name": "微博", "url": "https://weibo.com/shanganjianada", "icon": "fa-brands fa-weibo"},
        {"name": "微信公众号", "url": "https://mp.weixin.qq.com/s/shanganjianada", "icon": "fa-brands fa-weixin"}, 
        {"name": "小红书", "url": "https://www.xiaohongshu.com/user/profile/6586288c000000001c008e39", "icon": "fa-solid fa-heart"},
    ],
    "logo": {
        "text": "上岸加拿大",
        "image_dark": "_static/logo-dark.svg",
    },
    "show_toc_level": 1,
    "navbar_align": "left",
    "show_version_warning_banner": False,
    "footer_start": "",
    "footer_end": ["copyright"],
    "secondary_sidebar_items": ["page-toc", "aboutus"   ],

}

# Sidebar configuration
html_sidebars = {
    "**": ["sidebar-nav-bs", "custom-template", "sidebar-ethical-ads"],
    "index": [],
    "visitor/index": [],
    "immigration/index": [],
    "citizen/index": [],
    "news/index": [],
    "officialwebsites/index": [],
}


html_context = {
    "doc_path": "docs",
    "title": "HoldTheDoor"
}

# Custom styles and scripts
html_css_files = ["custom.css"]
html_js_files = ["pydata-icon.js", "custom-icon.js", "google_analytics.js"]
todo_include_todos = True

# Favicon configuration
favicons = [
    "favicon-32x32.png",
    "favicon-16x16.png",
    {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
    "android-chrome-192x192.png",
    {"rel": "mask-icon", "color": "#459db9", "href": "safari-pinned-tab.svg"},
    {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
    {"name": "msapplication-TileColor", "content": "#459db9"},
    {"name": "theme-color", "content": "#ffffff"},
    {"name": "msapplication-TileImage", "content": "mstile-150x150.png"},
]