# -*- coding: utf-8 -*-

# Scrapy settings for web_crawling project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'web_crawling'

SPIDER_MODULES = ['web_crawling.spiders']
NEWSPIDER_MODULE = 'web_crawling.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'web_crawling (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'web_crawling.pipelines.WebCrawlingPipeline':300
}