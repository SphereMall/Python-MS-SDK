
class Meta:

    def __init__(self, count: int = 0, limit: int = 0, offset: int = 0):
        """
        Meta initializer.
        :param count: int
        :param limit: int
        :param offset: int
        """
        self.count = count
        self.limit = limit
        self.offset = offset
