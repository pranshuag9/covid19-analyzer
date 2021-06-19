class ResponseTemplate:
	'''
		Used to generate a standard response with appropriate keys.

		Use instance.__dict__ to get dictionary. Eg: r = ResponseTemplate(message=...)
		return jsonify(r.to_dict())
	'''

	def __init__(self, error=False, success=True, type="None", data=None, message=""):
		self.error = error
		self.success = success
		self.type = type
		self.data = data
		self.message = message

	def to_dict(self):
		return self.__dict__
