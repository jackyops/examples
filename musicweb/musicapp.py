# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/12/19 21:45'

# pip install tornado

from tornado import web,httpserver,ioloop
from musicweb.functions import get_music_info_by_name


class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        # self.write('Hello Jacky')
        self.render('index.html')

class GetMusicInfoHandler(web.RedirectHandler):
    def post(self, *args, **kwargs):
        query = self.get_argument('query')
        # print(query)

        #爬取数据
        music_info = get_music_info_by_name(query)
        self.render('music.html',music=music_info)

#路由 分机号

application = web.Application([
    (r"/aaa",MainPageHandler),
    (r"/query",GetMusicInfoHandler),
])

# socket服务前台
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8000)
    ioloop.IOLoop.current().start()