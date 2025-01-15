def minimizeXor(num1, num2):
    """
    x has the same bit as num 2, and value x XOR num 1 is minimal
    :param num1:
    :param num2:
    :return: x
    """
    counter_bits = bin(num2).count('1')
    num1_bits = bin(num1)
    answ = '0b'
    if counter_bits > len(num1_bits[2:]):   #if num1 has less bits than we need to set
        answ += '1' * (counter_bits - len(num1_bits[2:]))
        counter_bits = counter_bits - (counter_bits - len(num1_bits[2:]))
    for bit in num1_bits[2:]:       #set all bits that we have to change
        if bit == '1' and counter_bits > 0:
            answ += '1'
            counter_bits -= 1
        else:
            answ += '0'
    if counter_bits != 0:       #if we have unused bits, set it
        i = len(answ) - 1
        while counter_bits != 0:
            if answ[i] == '0':
                counter_bits -= 1
                answ = answ[:i] + '1' + answ[i+1:]
            else:
                i -= 1

    return int(answ, 2)


def main():
    num1 = 346
    num2 = 6654
    print(minimizeXor(num1, num2))


if __name__ == '__main__':
    main()