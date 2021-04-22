"""2.1 While Python provides the built-in list type for constructing and managing
mutable sequences, many languages do not provide such a structure, at least
not as part of the language itself. To help in further understanding how
Python’s built-in list works, implement the Vector ADT using the Array class
implemented in the chapter. Your implementation should produce a mutable
sequence type that works like Python’s list structure. When the underlying
array needs to be expanded, the new array should double the size of the
original. The operations that can be performed on the ADT are described
below. Assume the size of the underlying array never decreases."""

class Vector_ADT:
    def __init__(self, size):
        self.size = size
        self.vector = [None] * self.size

    def Display(self):
        print(self.vector)

    def __len__(self):
        return len(self.vector)

    def contains(self):
        self.item = input("Please input the item you searching for: ")

        if self.item in self.vector:
            print("The item exist")
        else:
            print("The item not found")

    def __getitem__(self, index):
        self.index = index
        return self.vector[self.index]

    def __setitem__(self, key, value):
        self.key = key
        self.value = value
        self.vector.insert(self.key, self.value)

    def Append(self, item):
        self.item = item
        return self.vector.append(self.item)

    def Remove(self, item):
        self.item = item
        return self.vector.remove(self.item)

    def indexOf(self, item):
        self.item = item
        return self.vector.index(self.item)

    def othervec(self, size):
        self.size = size
        self.othervec = [None] * self.size
        self.__setitem__()
        self.__getitem__()

    def extend(self):
        self.NewVector = self.vector + self.otherVec
        return self.NewVector

    def subVector(self, From, To):
        self.From = From
        self.To = To
        self.SubVector = self.vector[self.From: self.To + 1]
        return self.SubVector

    def iterator(self):
        return list(reversed(self.vector))

_______________________________________________________________________


