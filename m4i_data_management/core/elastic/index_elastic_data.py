import logging

from pandas import DataFrame, notnull

from .utils import make_elastic_connection

log = logging.getLogger(__name__)

from elasticsearch.helpers import bulk 

def index_elastic_data(data: DataFrame, index: str):
    """
    Writes the given data to the Elasticsearch index with the given name.
    Uses the index of the rows as ids.
    """

    elastic = make_elastic_connection()

    def rows():
       for id, row in data.iterrows():
            row_data = row.where(notnull(row), None).to_dict()
            message = {
                "_id": id,
                "_index": index,
                **row_data
            } 
            log.debug(message)
            yield message
        # END LOOP
    # END rows

    try:
        bulk(elastic, rows())
    except Exception as e:
        log.exception(e)
    finally:
        elastic.close()
    # END TRY
# END index_elastic_data
