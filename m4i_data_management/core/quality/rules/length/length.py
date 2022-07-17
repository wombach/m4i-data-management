from pandas import DataFrame, Series, isna


def length(data: DataFrame, column_name: str, required_length: int) -> Series:
    """
    Checks if the number of characters of the values in the column with the given `column_name` are equal to the `required_length`. 

    This only works for textual values.
    If a value is not a string, it is converted to a string before comparison.
    
    If the length is equal, or if the value is empty, assigns a score of 1. 
    Otherwise, assigns a score of 0.
    """

    def check(value):

        if isna(value):
            return 1
        # END IF

        is_equal_length = (
            required_length == len(str(value))
        )

        return 1 if is_equal_length else 0
    # END check

    return data[column_name].apply(check)
# END length
