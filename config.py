import datetime
import logging
from pathlib import Path

import pytz as pytz

import custom_logging_config

img_size = 100

label_dict_category_val = {'Covid19_Negative': 0, 'Covid19_Positive': 1}

label_dict_val_category = {0: 'Covid19_Negative', 1: 'Covid19_Positive'}

MODEL_PATH = 'models/model-015.model'
current_timestamp = datetime.datetime.now(tz=pytz.timezone("Asia/Kolkata"))
MODEL_CHECKPOINT_PATH = f'models/checkpoints/{current_timestamp}'+'model-{epoch:03d}.model'

DATASET_DIR = "data/dataset"

npy_data_path, npy_target_path = "data.npy", "target.npy"

log_dir_path = Path(__file__).parent.absolute()

log: logging.Logger = custom_logging_config.get_logger("chest-xray-analyzer", log_dir_path)
