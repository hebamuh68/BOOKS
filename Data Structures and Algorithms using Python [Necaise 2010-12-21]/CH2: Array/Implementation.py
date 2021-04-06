1- """Array ADT"""

class Array:

    def Array_size(self, size):
        self.size = size
        self.array = [None] * self.size

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        self.index = index
        return self.array[self.index]

    def __setitem__(self, key, value):
        self.key = key
        self.value = value
        self.array.insert(self.key, self.value)

    def clearing(self, value):
        self.array = [value] * self.size

    def __iter__(self):
        for i in self.array:
            print(i)


________________________________________________________________________________________________________
1- """A two-dimensional array consists of a collection of elements organized into rows
and columns. Individual elements are referenced by specifying the specific row and
column indices (r, c), both of which start at 0."""


from numpy import *

class Array_2D:

    def __init__(self):
        self.rows = int(input("PLease enter ur rows number: "))
        self.cols = int(input("PLease enter ur cols number: "))
        self.Array = array([["None"] * self.cols] * self.rows)

    def numRows(self):
        return self.rows

    def numCols(self):
        return self.cols

    def GetItem(self):
        self.x, self.y = map(int, input("please enter the position of your value (x,y): ").split())
        return self.Array[self.x][self.y]

    def SetItem(self):
        self.x, self.y, self.value = map(int, input("please enter the position of your value (x,y): ").split())
        self.Array[self.x][self.y] = self.value
        return self.Array
________________________________________________________________________________________________________
2- """A matrix is a collection of scalar values arranged in rows and columns as a rectan-
gular grid of a fixed size. The elements of the matrix can be accessed by specifying
a given row and column index with indices starting at 0."""


from numpy import *

class Matrix_ADT:

    def __init__(self):
        self.rows = int(input("PLease enter ur rows number: "))
        self.cols = int(input("PLease enter ur cols number: "))
        self.Matrix = array([[0] * self.cols] * self.rows)

    def numRows(self):
        return self.rows

    def numCols(self):
        return self.cols

    def getItem(self, item):
        self.x, self.y = map(int, input("please enter the position of your value (x,y): ").split())
        return self.Matrix[self.x][self.y]

    def setItem(self, key, value):
        self.x, self.y, self.value = map(int, input("please enter the position of your value (x,y): ").split())
        self.Matrix[self.x][self.y] = self.value
        return self.Matrix

    def scaleBy(self):
        self.scalar = int(input("Please input the scalar: "))
        return self.Matrix* self.scalar

    def transpose(self):
        return self.Matrix.transpose()

    def add(self):
        self.rows = int(input("PLease enter ur rows number: "))
        self.cols = int(input("PLease enter ur cols number: "))
        self.rhsMatrix = array([[0] * self.cols] * self.rows)

        return self.Matrix+self.rhsMatrix

    def subtract(self):
        return self.Matrix - self.rhsMatrix

    def multiply(self):
        return self.Matrix * self.rhsMatrix



