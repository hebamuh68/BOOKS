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
    def __init__(self):
        self.vector = list(map(int, input("please enter the numbers of "
                                          "the list separated be a space: ").split()))

    def Display(self):
        print(self.vector)

    def Length(self):
        return len(self.vector)

    def contains(self):
        self.item = input("Please input the item you searching for: ")

        if self.item in self.vector:
            print("The item exist")
        else:
            print("The item not found")

    def getItem(self):
        self.ndxDis = int(input("Please enter the index of the item you want: "))
        return self.vector[self.ndxDis]

    def setItem(self):
        self.item_to_insert, self.ndx = int(input("Please enter the item, "
                                                  "and its index separated by a space: "))

        return self.vector.insert(self.ndx, self.item_to_insert)

    def Append(self):
        self.item_to_append = int(input("Please enter the index of the item you want: "))
        return self.vector.append(self.item_to_append)

    def Remove(self):
        self.item_to_remove = int(input("Please enter the index of the item you want: "))
        return self.vector.remove(self.item_to_remove)

    def indexOf(self):
        self.item_to_disIndex = int(input("Please enter the index of the item you want: "))
        return self.vector.index(self.item_to_disIndex)

    def extend(self):
        self.otherVector = list(map(int, input("please enter the numbers of "
                                               "the list separated be a space: ").split()))

        self.NewVector = self.vector + self.otherVector
        return self.NewVector

    def subVector(self):
        self.From, self.To = map(int, input("please enter ( from , to)"
                                            " separated by a space: ").split())
        self.SubVector = self.vector[self.From: self.To + 1]
        return self.SubVector

    def iterator(self):
        return list(reversed(self.vector))

_______________________________________________________________________


