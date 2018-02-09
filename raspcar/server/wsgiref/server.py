from wsgiref.simple_server import make_server
from mypage import application

# generate a web server, ip:192.168.1.110, port: 8000, handler function: application
httpd = make_server('192.168.1.110', 8000, application)
print "Serving HTTP on port 8000..."

# listen to HTTP request
httpd.serve_forever()

