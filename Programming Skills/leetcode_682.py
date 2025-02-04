def calPoints(operations):
    """
    Return the sum of all the scores on the record after applying all the operations
    :param operations: list of scores and operations
    :return: sum
    """
    sums = []
    if operations[0].isdigit() or operations[0][0] == '-':
        sums.append(int(operations[0]))
    if len(operations) != 1:
        for i in range(1, len(operations)):
            if operations[i].isdigit() or operations[i][0] == '-':
                sums.append(int(operations[i]))
            elif operations[i] == '+':
                sums.append(sums[-1] + sums[-2])
            elif operations[i] == 'D':
                sums.append(sums[-1] * 2)
            elif operations[i] == 'C':
                sums.pop()
    return sum(sums)


def main():
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(calPoints(ops))


if __name__ == '__main__':
    main()