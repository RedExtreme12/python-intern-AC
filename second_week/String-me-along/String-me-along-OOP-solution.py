class create_message(str):

    def __call__(self, value=None):
        if value is None:
            return self
        return create_message(self + ' ' + value)
