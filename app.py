from flask import Flask, render_template
from flask_cors import CORS
from api.register_blueprints import register_blueprints
from config import log

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

@app.route("/")
def index():
	return render_template("index.html")


def create_app() -> app:
	with app.app_context():
		register_blueprints(app)
	app.app_context().push()
	return app

if __name__ == "__main__":
	log.info("Main Called")

	app = create_app()

	app.run(debug=True)
	log.info("Main Call Ended")
