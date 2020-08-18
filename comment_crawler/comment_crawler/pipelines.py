# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import traceback


class CommentCrawlerPipeline:
    def process_item(self, item, spider):
        item = self.check_item(item)
        if item == "Old News":
            print('duplicate news' * 10)
            return
        try:
          self.es_object.index(index=self.index_name, doc_type='_doc', body=item)
        except:
          traceback.print_exc(limit=10)


