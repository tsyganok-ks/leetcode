import pandas as pd

def selectFirstRows(employees):
    #Get first 3 rows of DF
    return employees.head(3) #built-in
    #return employees[:3] #faster


def main():
    employees = pd.DataFrame(data = [
        [1, 'Richy', 17],
        [2, 'Anthony', 19],
        [3, 'Richy', 17],
        [4, 'Anthony', 19]],
        columns=['employee_id', 'name', 'age'])

    print(selectFirstRows(employees))


if __name__ == '__main__':
    main()