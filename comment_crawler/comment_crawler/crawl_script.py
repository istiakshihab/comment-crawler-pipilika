from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler

from spiders.prothomalo import ProthomaloSpider

job_defaults = {'max_instances': 3}

process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
            'FEED_URI': 'output_file.csv',
            'FEED_FORMAT': 'csv',
        })

# process = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',

# })
sched = TwistedScheduler(job_defaults=job_defaults)
regular_time = 5
sched.add_job(process.crawl, 'interval', args=[ProthomaloSpider], minutes=0)
sched.start()
process.start(False)
