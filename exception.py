class InvalidInput(Exception):
    """
    Exception raised when the given input is incorrect
    """

    def __init__(self, message="Invalid input") -> None:
        self.message = message
        super().__init__(self.message)


class RequestFailException(Exception):
    """
    Exception raised when the given input is incorrect
    """

    def __init__(self, message="Request failed") -> None:
        self.message = message
        super().__init__(self.message)
