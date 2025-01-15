import pandas as pd

def selectData(students):
    """
    Select name and age of student with student_d = 101
    :param students: pandas DF
    :return: pandas DF with name and age of student
    """
    return students.loc[students.student_id == 101,['name', 'age']]



def main():
    students = pd.DataFrame(data = [
        [101, 'Richy', 17],
        [102, 'Anthony', 19],
        [103, 'Tom', 18],
        [104, 'Mark', 21]],
        columns=['student_id', 'name', 'age'])
    print(selectData(students))

if __name__ == '__main__':
    main()