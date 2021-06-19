from api.response_templates.response_template import ResponseTemplate


class ErrorResponse(ResponseTemplate):
	def __init__(self, message="", data=None, type="None"):
		self.message = message
		self.data = data
		self.type = type
		super().__init__(
			error=True,
			success=False,
			type=self.type,
			data=self.data,
			message=self.message
		)
