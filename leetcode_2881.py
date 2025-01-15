import pandas as pd

def createBonusColumn(employees):
    """
    Add a new column - bonus
    :param employees: pandas DF
    :return: updated pandas DF
    """
    employees['bonus'] = employees['salary'] * 2
    return employees


def main():
    employees = pd.DataFrame(data = [
        ['Richy', 200],
        ['Anthony', 350],
        ['Richy', 750],
        ['Anthony', 580]],
        columns=['name', 'salary'])
    print(createBonusColumn(employees))


if __name__ == '__main__':
    main()