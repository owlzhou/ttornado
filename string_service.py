import textwrap
import tornado.ioloop
import tornado.web

class ReverseHanlder(tornado.web.RequestHandler):
	def get(self, input):
		self.write(input[::-1])
		
class WrapHanlder(tornado.web.RequestHandler):
	def post(self):
		text = self.get_argument('text')
		width = self.get_argument('width', 40)
		self.write(textwrap.fill(text, width))
		
if __name__ == "__main__":
	app = tornado.web.Application(
		handlers=[
			(r"/reverse/(\w+)", ReverseHanlder),
			(r"/wrap", WrapHanlder),
			])
	app.listen(8000)
	tornado.ioloop.IOLoop.instance().start()