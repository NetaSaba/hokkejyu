AUTHOR = 'Hollen9'
SITENAME = 'Hokkejyu'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh_TW'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

OUTPUT_PATH = 'docs/'
MARKDOWN = {
    'extensions': ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.meta'],
    'extension_configs': {
	'markdown.extensions.codehilite': {'css_class': 'highlight'},
	'markdown.extensions.toc' : {},
	'markdown.extensions.extra': {},
	'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}



MARKUP = ('md')
# THEME = "themes/pelican-mediumfox"

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
SOCIAL = (
    ("Hollen9 個人網站", "https://hollen9.com"),
    ("Twitter 推特", "https://twitter.com/hollen9"),
    ("Steam 個人頁面", "https://steamcommunity.com/id/hollen9")
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
