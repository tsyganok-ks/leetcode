class Solution:
    """
    Solution for task #2661
    """
    def firstCompleteIndex(self, arr, mat):
        """
        Find index of first complete row or col, while watching array arr
        :param arr: order of watching nums
        :param mat: grid of nums
        :return: index of row or col
        """
        rows = len(mat)
        cols = len(mat[0])
        position_map = {mat[r][c]: (r, c) for r in range(rows) for c in range(cols)}
        row_count = [cols] * rows
        col_count = [rows] * cols
        for idx, val in enumerate(arr):
            row, col = position_map[val]
            row_count[row] -= 1
            col_count[col] -= 1
            if row_count[row] == 0 or col_count[col] == 0:
                return idx
        return -1


def main():
    answ = Solution()
    arr = [2,8,7,4,1,3,5,6,9]
    mat = [[3,2,5],[1,4,6],[8,7,9]]
    print(answ.firstCompleteIndex(arr, mat))


if __name__ == '__main__':
    main()