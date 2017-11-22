# coding:utf-8
"""
爬虫输出器
"""


class HtmlOutputer(object):
    """
    爬虫输出类
    """

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        """
        收集数据函数
        """
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        """
        输出函数
        """
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<html>\n')
        fout.write('<body>\n')
        fout.write('<table>\n')

        for data in self.datas:
            fout.write('<tr>\n')
            fout.write('<td>%s</td>\n' % data['url'])
            fout.write('<td>%s</td>\n' % data['title'])
            fout.write('</tr>\n')

        fout.write('</table>\n')
        fout.write('</body>\n')
        fout.write('</html>\n')

        fout.close()
