from vox_data_management import Producer

from .utils import propagate_fte_dataset, retrieve_elastic_data, retrieve_fte_data
from .constants import FTE_DATASET_PRODUCER_NAME

fte_dataset_producer = Producer(
    get_new=retrieve_fte_data,
    get_old=retrieve_elastic_data,
    name=FTE_DATASET_PRODUCER_NAME,
    propagate=propagate_fte_dataset
)
