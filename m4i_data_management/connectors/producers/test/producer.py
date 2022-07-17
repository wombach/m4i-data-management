from vox_data_management.core.producer import Producer

from .constants import TEST_PRODUCER_NAME
from .utils import propagate_fte_dataset, retrieve_new_data, retrieve_old_data

test_producer = Producer(
    get_new=retrieve_new_data,
    get_old=retrieve_old_data,
    name=TEST_PRODUCER_NAME,
    propagate=propagate_fte_dataset
)
