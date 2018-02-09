def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return '<h1>Hi, Frank! --- %s</h1>' % (environ['PATH_INFO'][1:] or 'web')

