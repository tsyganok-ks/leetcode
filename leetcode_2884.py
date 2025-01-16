import pandas as pd

def modifySalaryColumn(employees):
    """
    Modifying salary column
    :param employees: pandas DF
    :return: updated DF
    """
    employees['salary'] = employees['salary']*2
    return employees