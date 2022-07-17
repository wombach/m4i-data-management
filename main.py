import logging.config

from config import logging_config
from m4i_data_management.connectors.producers.test import test_producer

# Set up the logger
logging.config.dictConfig(logging_config)

# Run the producer
if __name__ == "__main__":
    test_producer.run()
# END MAIN
