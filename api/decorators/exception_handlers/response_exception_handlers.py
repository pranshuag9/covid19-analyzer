from functools import wraps

from flask import jsonify

from api.response_templates.error_response_template.error_response_template import \
	ErrorResponse


def response_exception_handler(function):
	@wraps(function)
	def decorated_function(*args, **kwargs):
		try:
			response_template, statuscode = function(*args, **kwargs)
			return jsonify(response_template.to_dict()), statuscode
		except Exception as e:
			ErrorResponse(message=str(e))
	return decorated_function
