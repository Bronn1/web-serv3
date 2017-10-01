def app(environ, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	start_response(status, headers)
	get_option = environ['QUERY_STRING'].split("&")
	get_option = [item + "\n\r" for item in get_option]

	return get_option
