def areAlmostEqual(s1, s2):
    """
    Check if it is possible to make both strings equal
    by performing at most one string swap on exactly one of the strings
    :param s1: str 1
    :param s2: str 2
    :return: True or False
    """
    if len(s1) != len(s2):
        return False
    elif s1 == s2:
        return True
    else:
        diff1 = {}
        diff2 = {}
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff1[i] = s1[i]
                diff2[i] = s2[i]
            if len(diff1) > 2:
                return False
        if set(diff1.values()) == set(diff2.values()):
            return True
        else:
            return False


def main():
    s1 = "bank"
    s2 = "kanb"
    print(areAlmostEqual(s1, s2))


if __name__ == '__main__':
    main()