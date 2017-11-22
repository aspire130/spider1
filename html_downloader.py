# coding:utf-8
import  urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            #print(str(url) + 'is None')
            return None
        try:
            response = urllib.request.urlopen(url)
        except urllib.request.URLError as e:
            print(e)
            return None
        if response.getcode() != 200:
            #print(response.getcode())
            return None
        #print('download OK')
        return response.read()
