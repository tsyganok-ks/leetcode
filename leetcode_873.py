def lenLongestFibSubseq(arr):
    """
    Return the length of the longest Fibonacci-like subsequence of arr.
    If one does not exist, return 0.
    :param arr: array
    :return: len of subsequence
    """
    nums = set(arr)
    answ = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            a = arr[i]
            b = arr[j]
            curr_len = 2

            while a + b in nums:
                a, b = b, a + b
                curr_len += 1

            if curr_len > 2 and curr_len > answ:
                answ = curr_len

    return answ


def main():
    arr = [2,4,7,8,9,10,14,15,18,23,32,50]
    print(lenLongestFibSubseq(arr))


if __name__ == '__main__':
    main()