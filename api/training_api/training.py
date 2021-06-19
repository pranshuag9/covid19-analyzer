from flask import Blueprint

from api.decorators.exception_handlers.response_exception_handlers import \
    response_exception_handler
from api.training_api.training_api_handler import handle_train_model_request

training_blueprint = Blueprint("training_blueprint", __name__)

@training_blueprint.route("/train_model", methods=["POST"])
@response_exception_handler
def train_model():
    return handle_train_model_request()