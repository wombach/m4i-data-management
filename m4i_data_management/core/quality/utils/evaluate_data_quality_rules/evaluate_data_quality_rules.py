import logging
from datetime import datetime
from typing import Iterable, Tuple
from uuid import uuid4 as uuid

from pandas import DataFrame

from ..run_quality_check import run_quality_check

log = logging.getLogger(__name__)


def annotate_results(data: DataFrame, run_id: str, run_date: str):
    result = data.copy()

    result["run_id"] = run_id
    result["run_date"] = run_date

    return result
# END annotate_reults


def evaluate_data_quality_rules(data: DataFrame, rules: DataFrame) -> Iterable[Tuple[DataFrame, DataFrame, DataFrame]]:
    """
    Evaluates the given data quality `rules` over the given `data` and returns the test results as Pandas DataFrame.
    """
    def run_checks():
        for _, rule in rules.iterrows():

            if rule['active'] == 0:
                log.info(f"Skipping inactive business rule {rule['id']}")
                continue
            # END IF

            yield run_quality_check(data, rule)
        # END LOOP
    # END run_checks

    run_id = uuid()
    run_date = datetime.now().isoformat()

    for summary, compliant, non_compliant in run_checks():
        results = DataFrame([summary]), compliant, non_compliant

        yield map(lambda result: annotate_results(result, run_id, run_date), results)
    # END LOOP
# END evaluate_data_quality_rules
