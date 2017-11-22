# coding:utf-8
"""
网页管理器
"""


class UrlManager(object):
    """
    网页管理类
    """

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        添加一个新网页
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        批量添加新网页
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        """
        判断是否有未爬取网页
        """
        return len(self.new_urls) != 0

    def get_new_url(self):
        """
        获取一个未爬去网页
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
