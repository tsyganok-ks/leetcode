import pandas as pd

def createDataframe(student_data):
    """
    Create pandas DF from 2D list
    :param student_data: with 2 columns 'student_id', 'age'
    :return: pandas DF
    """
    return pd.DataFrame(student_data, columns = ['student_id', 'age'])


def main():
    student_data = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]
    print(createDataframe(student_data))


if __name__ == '__main__':
    main()