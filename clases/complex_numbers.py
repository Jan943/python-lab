class liczbyZespolone:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __addition__(self, number):
        return liczbyZespolone(self.re + number.re, self.im + number.im)
    def __substraction__(self, number):
        return liczbyZespolone(self.re - number.re, self.im - number.im)
    def __multiplication__(self, number):
        return liczbyZespolone(self.re * number.re, self.im * number.im)
    def __division__(self, number):
        return liczbyZespolone(self.re / number.re, self.im / number.im)
    def __format__(self):
        if (self.im >= 0):
            print("{}+{}i".format(self.re, self.im))
        else:
            print("{}-{}i".format(self.re, abs(self.im)))