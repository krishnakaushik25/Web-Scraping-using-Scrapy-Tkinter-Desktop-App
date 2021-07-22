# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class ZillowPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'houseID': item.get('id')}) for x in item.get(self.images_urls_field, [])]
    
    def file_path(self, request, response=None, info=None):
        image_name = request.meta['houseID']
        return 'images/%s.jpg' % (image_name)
