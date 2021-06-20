import base64
import io
import os
from os import path, walk

import cv2
import numpy as np
from PIL import Image
from tensorflow.python.keras.utils.np_utils import to_categorical

from config import img_size, log, label_dict_val_category, label_dict_category_val, \
	npy_data_path, npy_target_path


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


def save_images_to_npy(data, target, data_filename, target_filename):
	np.save(data_filename, data)
	np.save(target_filename, target)


def load_data_from_files(npy_data_path, npy_target_path):
	data = np.load(npy_data_path)
	target = np.load(npy_target_path)
	return data, target


def load_data_from_disk(data_dir):
	categories = os.listdir(data_dir)
	img_size = 100
	data, target = [], []

	for category in categories:
		folder_path = os.path.join(data_dir, category)
		img_names = os.listdir(folder_path)

		for img_name in img_names:
			img_path = os.path.join(folder_path, img_name)
			img = cv2.imread(img_path)

			try:
				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				resized = cv2.resize(gray, (img_size, img_size))
				data.append(resized)
				target.append(label_dict_category_val[category])
			except Exception as e:
				log.info(f"Error occurred while preprocessing image, {str(e)}")

	data = np.array(data) / 255.0
	data = np.reshape(a=data, newshape=(data.shape[0], img_size, img_size, 1))
	target = np.array(target)
	new_target = to_categorical(target)

	data_file, target_file = npy_data_path.split(".")[0], npy_target_path.split(".")[0]

	save_images_to_npy(
		data=data,
		target=new_target,
		data_filename=data_file,
		target_filename=target_file
	)
	npy_data, npy_target = load_data_from_files(npy_data_path, npy_target_path)

	return npy_data, npy_target


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
