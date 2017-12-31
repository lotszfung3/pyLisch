
class variableNotFoundException(Exception):
    def __str__(self):
        return str(self.args[0])
class invalidArgNumberException(Exception):
    def __str__(self):
        return str(self.args[0])

