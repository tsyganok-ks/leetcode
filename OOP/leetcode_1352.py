import math

class ProductOfNumbers:
    """
    Design an algorithm that accepts a stream of integers and
    retrieves the product of the last k integers of the stream.
    """
    def __init__(self):
        self.stack = []

    def add(self, num: int) -> None:
        self.stack.append(num)

    def getProduct(self, k: int) -> int:
        return math.prod(self.stack[-k:])