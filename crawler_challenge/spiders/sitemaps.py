# -*- coding: utf-8 -*-
import os
import scrapy
import urlparse


class SitemapsSpider(scrapy.Spider):
    name = 'sitemaps'

    def __init__(self, url=None, *args, **kwargs):
        if url is None:
            return
        super(SitemapsSpider, self).__init__(*args, **kwargs)
        self.url = urlparse.urlparse(url)
        self.allowed_domains = [self.url.netloc]
        self.start_urls = ['{}://{}/'.format(self.url.scheme, self.url.netloc)]
        self.visited = {'/', '#'}
    
    def is_valid(self, url):
        parsed_url = urlparse.urlparse(url)
        url_ext = os.path.splitext(parsed_url.path)[1]
        if (
            'http' not in parsed_url.scheme or 
            parsed_url.netloc not in self.allowed_domains or
            url in self.visited or
            (url_ext and url_ext not in ('.html', '.htm', '.php'))
        ):
            return False
        return True

    def format(self, href):
        if href.startswith('//'):
            return '{}:{}'.format(self.url.scheme, href)
        elif href.startswith('/'):
            return '{}://{}{}'.format(
                self.url.scheme, 
                self.url.netloc, 
                href
            )
        return href

    def parse(self, response):
        for anchor in response.css('a'):
            href = anchor.xpath('@href').extract_first()
            if href and self.is_valid(self.format(href)):
                href = self.format(href)
                yield {'loc': href}
                self.visited.add(href)                
                yield response.follow(href, self.parse)
