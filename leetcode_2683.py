from functools import reduce

def doesValidArrayExist(self, derived):
    """
    Does the original array exist? It exists only if XOR of all elements = 0
    :param derived: formed array
    :return: True or False
    """
    return reduce(lambda x, y: x^y, derived) == 0