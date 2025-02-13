import heapq

def minOperations(nums, k):
    """
    Return the minimum number of operations needed
    so that all elements of the array are greater than or equal to k
    :param nums: array
    :param k: threshold
    :return: number of steps
    """
    steps = 0
    heapq.heapify(nums)
    while len(nums) >= 2:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)

        if x >= k: #all numbers >= k
            break

        heapq.heappush(nums, x*2 + y)
        steps += 1
    return steps


def main():
    nums = [2, 11, 10, 1, 3]
    k = 10
    print(minOperations(nums, k))


if __name__ == '__main__':
    main()