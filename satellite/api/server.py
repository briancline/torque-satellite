def app(environ, start_response):
    data = 'OK!'

    start_response('200 OK', [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ])
