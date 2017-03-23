# -*- coding: utf-8 -*-

# Scrapy settings for walkingstreet project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'walkingstreet'

SPIDER_MODULES = ['walkingstreet.spiders']
NEWSPIDER_MODULE = 'walkingstreet.spiders'

ITEM_PIPELINES = {
    'walkingstreet.pipelines.WalkingstreetPipeline': 300
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'walkingstreet (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'walkingstreet.middlewares.WalkingstreetSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'walkingstreet.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'walkingstreet.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

COOKIES={'_cnzz_CV30020080':'buzi_cookie%7Cd0365e70.5594.0c09.a95c.0f8617507ae5%7C-1',
                 'PHPSESSID':'v7aos12hl11f6cnff7ceqhkgk1',
                 '_dacevid3':'d0365e70.5594.0c09.a95c.0f8617507ae5',
                 '_HUPUSSOID':'c8dae74b-965c-4db6-b5ed-0d29295ac719',
                 '_cnzz_CV30020080':'buzi_cookie%7Cd0365e70.5594.0c09.a95c.0f8617507ae5%7C-1',
                 'AUM':'dgic8aVaD0I9XtKH8-GYD7O3jN5nt-yqlWtWpTno5j7lw',
                 '__dacevst':'1bcf1176.40d42ebe|1489758236669',
                 '_CLT':'918ebe7bb324d8673460f7af1d701a5c',
                 'u':'18555774|bGl1c2hpbGx5|b91a|47f494930255b895393f54a4a7e9a5ec|0255b895393f54a4|bGl1c2hpbGx5',
                 'ua':'19863420',
                 'us':'1220bdd0e67e6046b087888f089e4c20f6a8777eeb17238f5a0926f88cbfb9a997191ee69f046147feee7fb70c5c8b2dab613964d49e55572e6d807dcd674c6b'}