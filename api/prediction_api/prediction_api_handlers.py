import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

from api.response_templates.error_response_template.error_response_template import \
	ErrorResponse
from api.response_templates.response_template import ResponseTemplate
from api.response_templates.success_response_template.success_response_template import \
	SuccessResponse
from app_utils import preprocess, get_pil_image_instance
from config import MODEL_PATH, label_dict_val_category, log


def handle_predict_request(request_json) -> tuple[ResponseTemplate, int]:
	try:
		# Get encoded image from request and get it's PIL.Image.Image instance
		encoded_img = request_json['image']
		pil_image: Image = get_pil_image_instance(encoded_img)

		# Preprocess the original image
		test_image = preprocess(pil_image)

		# Load the model
		model = load_model(MODEL_PATH)

		# Get prediction for preprocessed image from loaded model
		prediction = model.predict(test_image)

		# Pick the first maximum value of prediction along horizontal axis
		result = np.argmax(prediction, axis=1)[0]

		# Pick the maximum predicted value
		accuracy = float(np.max(prediction, axis=1)[0])
		log.info(f"Prediction: {prediction}, Result: {result}, Accuracy: {accuracy}")

		label = label_dict_val_category[result]

		resp_msg = "Successfully generated the predictions."
		resp_data = {'result': label, 'accuracy': accuracy}
		return SuccessResponse(message=resp_msg, data=resp_data, type="json"), 200
	except Exception as e:
		error_str = str(e)
		return ErrorResponse(message=f"Error occurred while predicting, {error_str}"), 400
