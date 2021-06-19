import logging
from logging.config import dictConfig


def get_logger(logger, dir_path) -> logging.Logger:
	logging_config = {
		"version": 1,
		"disable_existing_loggers": False,
		"formatters": {
			"default": {
				"format": "%(asctime)s: [%(filename)s:%(lineno)s in %(funcName)s()] %(message)s",
			},
			"info": {
				"format": "[%(asctime)s]: %(message)s", "datefmt": "%H:%M:%S"
			},
		},
		"handlers": {
			'debugfilehandler': {
				'level': 'DEBUG',
				'class': 'logging.FileHandler',
				'filename': dir_path / 'log.log',
				'formatter': 'default'
			},
		},
		"loggers": {
			"chest-xray-analyzer": {
				'handlers': ['debugfilehandler'],
				'level': 'DEBUG',
				'propogate': True,
			},
		}
	}
	dictConfig(logging_config)
	custom_log = logging.getLogger(logger)
	return custom_log