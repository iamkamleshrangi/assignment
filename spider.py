import requests
from link_finder import LinkFinder
from main import *
from bs4 import BeautifulSoup
class spider():
    #Class variable among all instances
    project_name =''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self,project_name,base_url,domain_name):
        spider.project_name = project_name
        spider.base_url = base_url
        spider.domain_name = spider.project_name + '\queue.txt'
        spider.crawled_file = spider.crawled_file + '\crawled.txt'
        self.boot()
        self.crawled_page('First_spider',spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(spider.project_name)
        create_data_file(spider.project_name,spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name,page_url):
        if page_url not in spider.crawled:
            print"%s is crawling %s"%(thread_name,page_url)
            print "Queue Size %s || Crawled Size is %s"%(spider.queue,spider.crawled)
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.update_file()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            responce = requests.get(page_url)
            html_string = responce.content
            soup = BeautifulSoup(html_string)
            finder = LinkFinder(soup)
