import pandas as pd

def fillMissingValues(products):
    """
    Fill NaN as 0, only in column 'quantity'
    :param products: pandas DF
    :return: updated DF
    """
    products['quantity'] = products['quantity'].fillna(0)
    return products