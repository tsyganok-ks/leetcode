import pandas as pd

def changeDatatype(students):
    """
    Change type 'grade' column from float to int
    :param students: pandas DF
    :return: updated DF
    """
    students['grade'] = students['grade'].astype(int)
    return students