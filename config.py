import datetime
import logging
import tensorflow as tf
from pathlib import Path

import pytz as pytz

import custom_logging_config

training_type = "GPU" if tf.test.gpu_device_name() else "CPU"
training_time = 5 if tf.test.gpu_device_name() else 32

current_timestamp = datetime.datetime.now(
	tz=pytz.timezone("Asia/Kolkata")
).strftime('%Y-%m-%d-%H-%M-%S')

img_size = 100

label_dict_category_val = {'negative': 0, 'positive': 1}

label_dict_val_category = {0: 'negative', 1: 'positive'}

MODEL_PATH = 'models/checkpoints/2021-06-24-01-13-18/model-008.model'

MODEL_CHECKPOINT_PATH = f'models/checkpoints/{current_timestamp}/'+'model-{epoch:03d}.model'

DATASET_DIR = "data/dataset"

npy_data_path, npy_target_path = "data.npy", "target.npy"

log_dir_path = Path(__file__).parent.absolute()

log: logging.Logger = custom_logging_config.get_logger("chest-xray-analyzer", log_dir_path)
