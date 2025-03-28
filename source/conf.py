# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import datetime
#import ablog
# Project information
project = 'ShangAn'
copyright = '2025, 上岸加拿大'
author = 'ShangAn'
release = '1.0.0'
language = 'zh'

# Insert '_extension' directory into the path so Sphinx can find it
sys.path.insert(0, os.path.abspath('_extension'))
sys.path.insert(0, os.path.abspath('scripts'))

html_baseurl = 'https://www.shangan.ca/'
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
#myst_heading_anchors = 1
#myst_title_to_header = True
myst_substitutions = {"rtd": "[Read the Docs](https://readthedocs.org/)"}

myst_html_meta = {
    "title": "上岸加拿大",
    "description": "上岸加拿大，相聚枫叶国｜签证｜移民｜最全DIY教程",
    "image": "https://www.shangan.ca/_static/logo.svg",
    "type": "website",
    "robots": "index, follow",
    "keywords": "加拿大移民, 签证, DIY教程, 上岸加拿大, 加拿大签证, 加拿大移民, 加拿大DIY教程, 学签, 工签, 旅游签, 探亲签, 超级签证, PR, EE, PNP, Webform, 安调, 调档, 强制令",
    "twitter:card": "summary_large_image",
    "baidu-site-verification": "codeva-5PrHB8o0ZS",
    
    # Open Graph tags
    "og:title": "上岸加拿大",
    "og:description": "上岸加拿大，相聚枫叶国｜签证｜移民｜最全DIY教程",
    "og:image": "https://www.shangan.ca/_static/logo.svg",
    "og:type": "website"
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
#html_favicon = "_static/favicon.ico"
#html_extra_path = ['favicon.ico', 'robots.txt']
html_title = "上岸加拿大"
 
html_theme_options = {
    "external_links": [
    ],
    "icon_links": [
        {"name": "Email", "url": "mailto:shanganjianada@gmail.com", "icon": "fa-solid fa-envelope"},
        {"name": "微博", "url": "https://weibo.com/shanganjianada", "icon": "fa-brands fa-weibo"},
        {"name": "微信公众号", "url": "https://mp.weixin.qq.com/s/RL0e0EAMj4II5QxmTqK6Dg", "icon": "fa-brands fa-weixin"}, 
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
    "secondary_sidebar_items": ["page-toc", "aboutus"],

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
    "guide/index": [],
}




html_context = {
    "doc_path": "docs",
    "title": "上岸加拿大",
}

# Custom styles and scripts
html_css_files = ["custom.css"]
html_js_files = ["pydata-icon.js", "custom-icon.js", "google_analytics.js"]
todo_include_todos = True

# Function to get the last modification time of a file
""" def get_last_modified(app, docname, source):
    doc_path = app.env.doc2path(docname)
    if os.path.exists(doc_path):
        last_modified_time = os.path.getmtime(doc_path)
        last_modified_date = datetime.utcfromtimestamp(last_modified_time).strftime('%Y-%m-%d')
        source[0] = f":lastmod: {last_modified_date}\n" + source[0]

def setup(app):
    app.connect("source-read", get_last_modified) """