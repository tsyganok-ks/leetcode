def gridGame(grid):
    """
    Find the maximum of points, which can collect
    the second robot after the first robot
    :param grid: array (2, n)
    :return: maximum points
    """
    sum_first_row = sum(grid[0])
    sum_second_row = 0
    minimum_sum = float('inf')
    for turn in range(len(grid[0])):
        sum_first_row -= grid[0][turn]
        # Find the minimum sum value, because maximum sum uses first robot
        minimum_sum = min(minimum_sum, max(sum_first_row, sum_second_row))
        sum_second_row += grid[1][turn]
    return minimum_sum


def main():
    grid = [[2,5,4],[1,5,1]]
    print(gridGame(grid))


if __name__ == '__main__':
    main()