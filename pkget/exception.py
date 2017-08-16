class PkgetError(Exception):
    def __init__(self, message, code, *args):
        self.code = code
        self.message = message
        super().__init__(message, code, *args)

