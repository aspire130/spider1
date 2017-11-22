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
        self._values = {'user': '130啊斤', 'password': 'LIUhai@456'}
        self._postdata = urllib.parse.urlencode(self._values).encode('utf-8')
        self._user_agent = r'Mozilla/5.0(X11;Linux x86_64...)\
                             Gecko/20100101 Firefox/57.0'
        self._headers = {
            'User-Agent': self._user_agent,
            'Connection': 'keep-alive'}
        self._cj = http.cookiejar.CookieJar()
        self._opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self._cj))

    def getcookie(self, url):
        """
        登录获取cookie信息
        """
        root_request = urllib.request.Request(
            url, self._postdata, self._headers)
        try:
            self._opener.open(root_request)
        except urllib.request.URLError as error:
            print(error)
            return False
        return True

    def download(self, url):
        """
        下载函数
        """
        print('download')
        if url is None:
            print(str(url) + 'is None')
            return None
        try:
            req = urllib.request.Request(url, headers=self._headers)
            print(req)
            response = self._opener.open(req).decode('utf-8')
            print(response)
        except urllib.request.URLError as error:
            print(error)
            return None
        # print('download OK')
        return response.read()
