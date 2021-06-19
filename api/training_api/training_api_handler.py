from api.response_templates.error_response_template.error_response_template import \
    ErrorResponse


def handle_train_model_request():
    return ErrorResponse(message="Couldn't finish training!! Please try again later"), 400
