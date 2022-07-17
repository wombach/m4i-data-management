from pandas import DataFrame


def get_documents_from_elastic_search_result(search_result: dict) -> DataFrame:
    """
    Returns the document hits from the given ElasticSearch query result as a Pandas DataFrame
    """

    fields = map(lambda hit: hit['_source'], search_result['hits']['hits'])

    data = DataFrame(fields)

    return data
# END get_documents_from_elastic_search_result
