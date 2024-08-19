class InvalidInputException(Exception):
    """
    Exception raised when the given input is incorrect
    """

    def __init__(self, message="Invalid input") -> None:
        self.message = message
        super().__init__(self.message)


class NegativeNumberException(Exception):
    """
    Exception raised when the difference in input time and current timt
    is negative
    """

    def __init__(self, message="Invalid input") -> None:
        self.message = message
        super().__init__(self.message)
