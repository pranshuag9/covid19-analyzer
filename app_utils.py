import base64
import io
from os import path, walk

import cv2
import numpy as np
from PIL import Image

from config import img_size, log


def get_extra_files_to_watch_for_reload():
	extra_dirs = ['static/', 'templates/']
	extra_files = extra_dirs[:]
	for extra_dir in extra_dirs:
		for dirname, dirs, files in walk(extra_dir):
			for filename in files:
				filename = path.join(dirname, filename)
				if path.isfile(filename):
					extra_files.append(filename)
	return extra_files


def preprocess(img):
	log.info("Intiating image preprocessing")
	img: np.core.multiarray = np.array(img)

	if img.ndim == 3:
		# noinspection PyUnresolvedReferences
		gray: np.core.multiarray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	else:
		gray: np.core.multiarray = img

	gray = gray / 255
	# noinspection PyUnresolvedReferences
	resized = cv2.resize(gray, (img_size, img_size))
	reshaped = resized.reshape(1, img_size, img_size)
	log.info(f"Reshaped image to: {img_size}")
	return reshaped


def get_pil_image_instance(encoded_img):
	decoded_img = base64.b64decode(encoded_img)

	dataBytesIO = io.BytesIO(decoded_img)
	dataBytesIO.seek(0)

	return Image.open(dataBytesIO)
