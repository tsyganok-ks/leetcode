def sumOfMultiples(n):
    """Return the sum of numbers in range(n), which divisible on 3 or 5 or 7 """
    return sum([x for x in range(n + 1)
                if x % 3 == 0 or x % 5 == 0 or x % 7 == 0])