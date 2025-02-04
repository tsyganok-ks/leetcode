import pandas as pd

def consecutive_numbers(logs):
    """
    Find all numbers that appear at least three times consecutively
    :param logs: DataFrame
    :return: new DataFrame
    """
    groups = logs.groupby('num').groups
    answ = []
    for k, group in groups.items():
        if len(group) >= 3:
            for i in range(2, len(group)):
                if group[i-2] + 2 == group[i-1] + 1 == group[i]:
                    answ.append(k)
                    break
    df = pd.DataFrame(answ, columns = ['ConsecutiveNums'])
    return df


def main():
    data = [
        [1, 1],
        [2, 1],
        [3, 1],
        [4, 2],
        [5, 1],
        [6, 2],
        [7, 2]
    ]
    logs = pd.DataFrame(data, columns = ['id', 'num'])

    print(consecutive_numbers(logs))


if __name__ == '__main__':
    main()