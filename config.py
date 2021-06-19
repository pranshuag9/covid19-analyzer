import logging
from pathlib import Path

import custom_logging_config

img_size = 100

label_dict = {0: 'Covid19 Negative', 1: 'Covid19 Positive'}

MODEL_PATH = 'model/model-015.model'

log_dir_path = Path(__file__).parent.absolute()

log: logging.Logger = custom_logging_config.get_logger("chest-xray-analyzer", log_dir_path)
