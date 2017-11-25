# coding:utf-8
"""
爬虫主程序
"""
import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):
    """
    爬虫主程序
    """

    def __init__(self):
        self._urls = url_manager.UrlManager()
        self._downloader = html_downloader.HtmlDownloader()
        self._parser = html_parser.HtmlParser()
        self._outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        """
        爬取函数
        """
        self._downloader.getcookie(root_url)

        count = 1
        self._urls.add_new_url(root_url)
        while self._urls.has_new_url():
            new_url = self._urls.get_new_url()
            # print('craw %d : %s' % (count, new_url))
            html_cont = self._downloader.download(new_url)
            new_urls, new_data = self._parser.parse(new_url, html_cont)
            self._urls.add_new_urls(new_urls)
            self._outputer.collect_data(new_data)
            print(new_data)

            count += 1
            if count >= 45:
                break
        self._outputer.output_html()


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/f?kw=%B6%FE%D5%BD&&fr=itb_favo&fp=favo#'
    obj_spider = SpiderMain()
    obj_spider.craw(url)
