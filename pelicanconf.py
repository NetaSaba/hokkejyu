AUTHOR = 'Hollen9'
SITENAME = 'Hokkejyu'
SITEURL = "https://netasaba.github.io/hokkejyu"

PATH = "content"

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh_TW'
LOCALE = ('zh_TW')

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

OUTPUT_PATH = 'docs/'

THEME = 'themes/notmyidea'

STATIC_PATHS = ['images']

# PLUGINS = ['i18n_subsites']
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}


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

# I18N_SUBSITES = {
#     'en': {
#         'SITENAME': 'Hokkejyu-ruri!',
#     },
#     'zh_TW': {
#         'SITENAME': 'Hokkejyu-ruri! 好可啾嚕里',
#     }
# }

# 自定義文章和頁面的 URL 和保存路徑，根據 lang 變數輸出到不同目錄
ARTICLE_URL = '{lang}/{slug}.html'
ARTICLE_SAVE_AS = '{lang}/{slug}.html'

PAGE_URL = '{lang}/pages/{slug}.html'
PAGE_SAVE_AS = '{lang}/pages/{slug}.html'

# 當你有多語言時的特定語言文章和頁面保存格式
ARTICLE_LANG_URL = '{lang}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}.html'

PAGE_LANG_URL = '{lang}/pages/{slug}.html'
PAGE_LANG_SAVE_AS = '{lang}/pages/{slug}.html'


# 在導航欄中添加語言切換選項
LINKS = (
    ('English', 'https://netasaba.github.io/hokkejyu/en/'),
    ('台灣中文', 'https://netasaba.github.io/hokkejyu/zh_TW/'),
    ('日本語', 'https://netasaba.github.io/hokkejyu/ja/'),
    ('한국어', 'https://netasaba.github.io/hokkejyu/ko/'),
)

# Social widget
SOCIAL = (
    ("Hollen9 Web", "https://hollen9.com"),
    ("Twitter", "https://twitter.com/hollen9"),
    ("Steam", "https://steamcommunity.com/id/hollen9")
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
