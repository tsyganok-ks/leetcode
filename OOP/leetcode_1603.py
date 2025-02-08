class ParkingSystem:
    """
    Design of a parking system with a parking lot
    """
    def __init__(self, big: int, medium: int, small: int):
        """
        We have limited parking lots of all types
        """
        self.empty_lot = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        """
        Check if empty lot for particular type of car
        :param carType: big = 1, medium = 2, small = 3
        :return: True or False
        """
        if self.empty_lot[carType] > 0:
            self.empty_lot[carType] -= 1
            return True
        else:
            return False