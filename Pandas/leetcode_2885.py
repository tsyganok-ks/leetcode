import pandas as pd

def renameColumns(students):
    """
    Rename columns
    :param students: pandas DF
    :return: updated DF
    """
    students = students.rename(columns = {'id': 'student_id', 'first' : 'first_name',
                               'last' : 'last_name', 'age' : 'age_in_years'})
    return students
