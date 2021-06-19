from flask import Blueprint, request

from api.decorators.exception_handlers.response_exception_handlers import \
	response_exception_handler
from api.prediction_api.prediction_api_handlers import handle_predict_request
prediction_blueprint = Blueprint("prediction_blueprint", __name__)


@prediction_blueprint.route("/predict", methods=["POST"])
@response_exception_handler
def predict():
	request_json = request.get_json(force=True)
	return handle_predict_request(request_json)
