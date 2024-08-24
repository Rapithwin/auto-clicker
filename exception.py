class InvalidInputException(Exception):
    """
    Exception raised when the given input is incorrect
    """

    def __init__(self, message="Invalid input") -> None:
        self.message = message
        super().__init__(self.message)


