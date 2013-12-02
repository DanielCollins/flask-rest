import flask
from flask_rest import app

class Resource(flask.views.View):
    methods =['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

    def dispatch_request(self):
        if request.method == 'POST' and request.args.has_key('method'):
	    request.method = request.args.get('method').upper() 
        handler_name = request.method.lower()
	if hasattr(self, handler_name):
	    handler = getattr(self, handler_name)
	    if callable(handler):
	        return handler(self)
        response = flask.make_response('no!', 405)
	response.headers['Allow'] = 'GET, HEAD'
