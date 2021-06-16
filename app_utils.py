import cv2
import numpy as np

from config import img_size


def preprocess(img):
	img = np.array(img)

	if (img.ndim == 3):
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	else:
		gray = img

	gray = gray / 255
	resized = cv2.resize(gray, (img_size, img_size))
	reshaped = resized.reshape(1, img_size, img_size)
	return reshaped