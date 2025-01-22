import re

def hasMatch(s, p):
    """
    Check if string s matching pattern p
    :param s: main string
    :param p: pattern
    :return: True or False
    """
    if len(p) == 1:
        return True
    pattern = p.split('*')
    if '' in pattern:
        pattern.remove('')
    if s.find(pattern[0]) != -1:
        idx_first_part = s.find(pattern[0])
        if len(pattern) == 2 and idx_first_part + len(pattern[0]) < len(s):
            if s[idx_first_part + len(pattern[0]):].find(pattern[1]) != -1:
                return True
            else:
                return False
        elif len(pattern) != 2:
            return True
    else:
        return False

    return False

def hasMatch2(s, p):
    """
    Same function. Simplier to understand, but slower and take more memory
    :param s: string
    :param p: pattern
    :return: True or False
    """
    p = p.replace('*', '.*')
    return True if len(re.findall(p, s)) > 0 else False

def main():
    s = "xxxxqzq"
    p = "qzq*qz"
    print(hasMatch(s, p))


if __name__ == '__main__':
    main()