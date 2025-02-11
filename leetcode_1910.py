def removeOccurrences(s, part):
    """
    Repeatedly removes all occurrences of string part
    :param s: main string
    :param part: template to remove
    :return: clean string
    """
    answ = []
    for chr in s:
        answ.append(chr)
        if len(answ) >= len(part):
            if ''.join(answ[-len(part):]) == part:
                for _ in range(len(part)):
                    answ.pop()

    return ''.join(answ)

def main():
    s = "daabcbaabcbc"
    part = 'abc'

    print(removeOccurrences(s, part))


if __name__ == '__main__':
    main()