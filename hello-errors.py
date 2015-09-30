import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		greeting = self.get_argument('greeting', 'Hello')
		self.write(greeting + ", friendly user!")
	def write_error(self, status_code, **kwargs):
		self.write("Gosh darnit, user!You caused a %d error." % status_code)
		
		
if __name__ == "__main__":
	app = tornado.web.Application(
		handlers=[
			(r"/",IndexHandler),
			])
	app.listen(8000)
	tornado.ioloop.IOLoop.instance().start()