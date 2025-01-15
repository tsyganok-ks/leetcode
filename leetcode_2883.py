import pandas as pd

def dropMissingData(students):
    """
    Drop rows with None in column name
    :param students: pandas DF
    :return: new DF
    """
    #return students[students.name.isnull() == False]
    return students.dropna(subset = 'name')


def main():
    students = pd.DataFrame(data = [
        [101, 'Richy', 17],
        [102, 'Anthony', 19],
        [103, None, 18],
        [104, 'Mark', 21]],
        columns = ['students_id', 'name', 'age'])

    print(dropMissingData(students))


if __name__ == '__main__':
    main()