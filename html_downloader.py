# coding:utf-8
"""
爬虫下载器
"""
import urllib.request
import urllib.parse
import http.cookiejar


class HtmlDownloader(object):
    """
    爬虫下载类
    """

    def __init__(self):
        self._values = {'username': '***', 'password': '***'}
        self._postdata = urllib.parse.urlencode(self._values).encode('utf-8')
        self._user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
        self._headers = {
            'Accept':'*/*',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'User-Agent':self._user_agent,
            'Connection':'keep-alive'
        }
        self._cj = http.cookiejar.CookieJar()
        self._openerC = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self._cj))

    def getcookie(self, url):
        """
        登录获取cookie信息
        """
        root_request = urllib.request.Request(url, self._postdata, self._headers)
        # root_request = urllib.request.Request(url, headers=self._headers)
        try:
            self._openerC.open(root_request)
        except urllib.request.URLError as error:
            print(error)
            return False
        return True

    def download(self, url):
        """
        下载函数
        """
        if url is None:
            print(str(url) + 'is None')
            return None
        try:
            req = urllib.request.Request(url, headers=self._headers)
            response = self._openerC.open(req)
        except urllib.request.URLError as error:
            print(error)
            return None
        ret = response.read()
        response.close()
        return ret
