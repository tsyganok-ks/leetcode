class Solution:
    def checkValid(self, matrix):
        """
        Check if all colls and rows contain all integers (1, n)
        :param matrix: matrix (n,n)
        :return: True or False
        """
        n = len(matrix)
        matrix_t = [[matrix[j][i] for j in range(n)] for i in range(n)]

        for row in (matrix + matrix_t):
            if len(set(row)) != n:
                return False

        return True


def main():
    answ = Solution()
    matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    print(answ.checkValid(matrix))


if __name__ == '__main__':
    main()