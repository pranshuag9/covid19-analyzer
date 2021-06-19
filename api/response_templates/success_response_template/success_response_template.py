from api.response_templates.response_template import ResponseTemplate


class SuccessResponse(ResponseTemplate):
	def __init__(self, message="", data=None, type="None"):
		self.message = message
		self.data = data
		self.type = type
		super().__init__(
			error=False,
			success=True,
			type=self.type,
			data=self.data,
			message=self.message
		)
