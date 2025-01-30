def countKeyChanges(s):
    """
    Count number of changes between letters
    :param s: string
    :return: number of changes
    """
    answ = 0
    s = s.lower()
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            answ += 1
    return answ