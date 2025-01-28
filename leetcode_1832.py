def checkIfPangram(sentence):
    """
    Check if sentence consist at least 1 each symbol Eng alphabet
    :param sentence: string
    :return: True or False
    """
    if len(sentence) < 26:
        return False
    return len(set(list(sentence))) == 26