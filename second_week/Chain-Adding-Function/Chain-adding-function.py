class add(int):

    def __call__(self, value):
        """We make the class callable"""
        return add(self + value)
