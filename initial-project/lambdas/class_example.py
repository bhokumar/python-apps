class SpecialList:
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return 50


l1 = SpecialList([1, 2, 3, 4])

print(l1.__len__())

print(len(l1))