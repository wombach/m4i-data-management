import sys

'''
LOGGING CONFIG
'''
logging_config = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'filename': 'log/default.log',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'backupCount': 7,
            'when': 'midnight'
        }
    },
    'loggers': {
        'vox_data_management': {
            'level': 'DEBUG',
            'handlers': ['debug', 'default']
        }
    }
}

'''
CONFLUENT KAFKA CONFIG
'''
confluent_kafka = {
    "bootstrap.servers": "YOUR_BOOTSTRAP_SERVER",
}

'''
ELASTIC CONFIG
'''
elastic = {
    "scheme": "https",
    "port": 9243
}

'''
FTE DATASET CONNECTOR CONFIG
'''
fte_dataset_db = {
    "host": "YOUR_HOST_NAME",
    "port": 1521,
    "service_name": "YOUR_DATABASE_NAME"
}

fte_dataset_index = "YOUR_INDEX_NAME"

fte_dataset_kafka_topic = "YOUR_TOPIC_NAME"

fte_dataset_table = "YOUR_TABLE_NAME"
