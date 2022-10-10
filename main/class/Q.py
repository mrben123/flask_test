from distutils.log import error


class Q(object):
    def __init__(self, a, b) -> None:
        if a == None or b == None:
            raise ValueError("something's not right")
        else:
            self.a = a
            self.b = b

    def toCsv(self):
        print('转换数据')

    def goDatabase(self):
        print('数据入库')

    