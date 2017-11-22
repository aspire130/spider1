# coding:utf-8
"""
爬虫解析器
"""
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class HtmlParser(object):
    """
    爬虫解析类
    """

    def _get_new_urls(self, page_url, soup):
        """
        网页添加
        """
        new_urls = set()
        # <a href="/p/54457" title="奇书"
        links = soup.find_all('a', href=re.compile('/p/\d+$'))
        for link in links:
            new_url = link['href']
            # print(new_url)
            new_full_url = urljoin(page_url, new_url)
            # print(new_full_url)
            new_urls.add(new_full_url)
        # print(new_urls)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        数据添加
        """
        res_data = {}
        # url
        res_data['url'] = page_url
        title_node = soup.find('h3', class_=re.compile('core_title_txt'))
        if title_node is None:
            return None
        res_data['title'] = title_node.string
        # print(res_data)
        return res_data

    def parse(self, page_url, html_cont):
        """
        解析函数
        """
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        # print(soup.prettify())
        new_urls = None
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        # print(new_data)
        return new_urls, new_data
