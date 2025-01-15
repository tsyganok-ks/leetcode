import pandas as pd

def dropDuplicateEmails(customers):
    """
    Drop duplicates in email except first one
    :param customers: pandas DF
    :return: updated DF
    """
    customers.drop_duplicates(subset = 'email', keep = 'first', inplace = True)
    return customers


def main():
    customers = pd.DataFrame(data = [
        [1, 'Richy', 'a@abc.com'],
        [2, 'Anthony', 'b@abc.com'],
        [3, 'Tom', 'a@abc.com'],
        [4, 'Marc', 'c@abc.com']],
        columns = ['customer_id', 'name', 'email'])

    print(dropDuplicateEmails(customers))


if __name__ == '__main__':
    main()