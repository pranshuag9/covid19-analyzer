from flask import Flask, render_template
from flask_cors import CORS
from api.register_blueprints import register_blueprints
from app_utils import get_extra_files_to_watch_for_reload
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
	extra_files = get_extra_files_to_watch_for_reload()
	app.run(debug=True, extra_files=extra_files)
	log.info("Main Call Ended")
