def clearDigits(s):
    """
    Remove all digits and connected 1 left symbol repeatedly
    :param s: string
    :return: resulting string
    """
    list_chars = []
    for chr in s:
        if chr.isdigit():
            if len(list_chars) > 0:
                list_chars.pop()
        elif chr.isalpha():
            list_chars.append(chr)

    return ''.join(list_chars)


def main():
    s = 'cgb34'
    print(clearDigits(s))


if __name__ == '__main__':
    main()