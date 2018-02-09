#!/usr/bin/python
#coding: utf8

import sys
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define, options
import driver


tornado.options.define("port", default=80, type=int)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")
	def post(self):
		arg = self.get_argument('k')
		if (arg == 'w'):
			driver.forward(1)
		elif (arg == 's'):
			driver.backward(1)
		elif (arg == 'a'):
			driver.left_forward(0.5)
		elif (arg == 'd'):
			driver.right_forward(0.5)
		else:
			return
		print arg
		self.write(arg)


if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

