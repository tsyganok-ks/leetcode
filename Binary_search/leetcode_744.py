def nextGreatestLetter(letters, target):
    """
    Binary search approach to find greater letter than target
    :param letters: array
    :param target: target letter
    :return: letter bigger than target
    """
    if target < letters[0] or target > letters[-1]:
        return letters[0]
    low = 0
    high = len(letters) - 1
    while low <= high:
        mid = (low + high) // 2
        if target <= letters[mid]:
            low = mid + 1
        else: #target > letters[mid]
            high = mid - 1

    return letters[low]


def main():
    letters = ["c", "f", "j", "j"]
    target = "j"
    print(nextGreatestLetter(letters, target))


if __name__ == '__main__':
    main()