# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy
import utils
import requests 
import json
from urllib.parse import urlparse
import datetime

class ProthomaloSpider(CrawlSpider):
    name = 'prothomalo'
    allowed_domains = ['www.prothomalo.com']
    start_urls = ['https://www.prothomalo.com/economy/article/1655837/%E0%A6%B0%E0%A6%AA%E0%A7%8D%E0%A6%A4%E0%A6%BE%E0%A6%A8%E0%A6%BF-%E0%A6%96%E0%A6%BE%E0%A6%A4%E0%A7%87-%E0%A6%A8%E0%A6%A4%E0%A7%81%E0%A6%A8-%E0%A6%A8%E0%A6%A4%E0%A7%81%E0%A6%A8-%E0%A6%95%E0%A7%8D%E0%A6%B0%E0%A7%87%E0%A6%A4%E0%A6%BE-%E0%A6%86%E0%A6%B8%E0%A6%9B%E0%A7%87']

    rules = (
        Rule(LinkExtractor(allow='/article/', ), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='/[a-z]{1,}'), follow=True)
    )
    
#def return_items(uid, comment, category , url, rootdomain, publishdate, parsetime, source="newspaper", datadomain):
    
    def parse_item(self, response):
        category = response.xpath('//*[@class="secondary_logo"]/a/span/text()').getall()[0]
        parsed_uri = urlparse(response.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        
        comment_url = "https://www.prothomalo.com/api/comments/get_comments_json/?content_id="+response.url.split("/")[5]
        res = requests.get(url=comment_url)
        jsonresponse = json.loads(res.text)
        for key in jsonresponse.keys():
            uid = jsonresponse[key]["comment_id"]
            comment = jsonresponse[key]["comment"]
            publishdate = jsonresponse[key]["create_time"]
            parsetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = utils.return_items(uid, comment, category, comment_url, domain, publishdate, parsetime)
            yield item
