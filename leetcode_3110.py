def scoreOfString(s):
    """The score of a string is defined as the sum of
    the absolute difference between the ASCII values of adjacent characters
    """
    return sum([abs(ord(s[x]) - ord(s[x + 1])) for x in range(len(s) - 1)])

