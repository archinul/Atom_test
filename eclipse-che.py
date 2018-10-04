
class A:
    def __init__(self):
        self.num = 0
        self.max = 11

    def __iter__(self):
        return self

    def __next__(self):
        if self.num == self.max:
            raise StopIteration
        else:
            self.num += 1
            return self.num
        return


a = A()
for i in range(12):
    print(next(a))
