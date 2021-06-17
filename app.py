from flask import Flask, render_template, request, jsonify
from keras.models import load_model
import numpy as np
import base64
from PIL import Image
import io

from app_utils import preprocess
from config import MODEL_PATH, label_dict

app = Flask(__name__)

model = load_model(MODEL_PATH)

@app.route("/")
def index():
	return (render_template("index.html"))


@app.route("/predict", methods=["POST"])
def predict():
	print('Initiating Prediction')
	try:
		request_json = request.get_json(force=True)
		encoded_img = request_json['image']
		decoded_img = base64.b64decode(encoded_img)

		dataBytesIO = io.BytesIO(decoded_img)
		dataBytesIO.seek(0)

		image = Image.open(dataBytesIO)

		test_image = preprocess(image)

		prediction = model.predict(test_image)
		result = np.argmax(prediction, axis=1)[0]
		accuracy = float(np.max(prediction, axis=1)[0])

		label = label_dict[result]

		print(prediction, result, accuracy)

		response = {
			"message": "Successfully generated the predictions.",
			"prediction": {
				'result': label,
				'accuracy': accuracy
			},
			"error": False,
			"success": True,
			"type": "json"
		}

		return jsonify(response), 200
	except Exception as e:
		error_str = str(e)
		response = {
			"message": f"Error occurred while predicting, {error_str}",
			"error": True,
			"success": False,
			"data": None,
			"type": None
		}
		return response, 400


app.run(debug=True)

# <img src="" id="img" crossorigin="anonymous" width="400" alt="Image preview...">
