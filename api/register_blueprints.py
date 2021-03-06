from flask import Flask

from api.prediction_api.predict import prediction_blueprint
from api.training_api.training import training_blueprint


def register_blueprints(app: Flask) -> None:
	'''
		To register blueprints from different modules

	:param app: It is the current flask application
	:return: None
	'''
	with app.app_context():
		blueprints = (
			prediction_blueprint,
			training_blueprint
		)

		for blueprint in blueprints:
			app.register_blueprint(blueprint)
