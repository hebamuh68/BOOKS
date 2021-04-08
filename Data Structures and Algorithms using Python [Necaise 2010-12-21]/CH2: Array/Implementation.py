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

class Array_2D:

    def Array(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.Array= [[0 for i in range(cols)] for j in range(rows)]

        return self.Array

    def numRows(self):
        return self.rows

    def numCols(self):
        return self.cols

    def GetItem(self, i, j):
        return self.Array[i][j]

    def SetItem(self, i, j, value):
        self.Array[i][j] = value
        return self.Array


________________________________________________________________________________________________________
2- """A matrix is a collection of scalar values arranged in rows and columns as a rectan-
gular grid of a fixed size. The elements of the matrix can be accessed by specifying
a given row and column index with indices starting at 0."""

class Matrix_ADT:

    def Matrix(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.Matrix = [[7 for i in range(cols)] for j in range(rows)]
        return self.Matrix

    def numRows(self):
        return self.rows

    def numCols(self):
        return self.cols

    def getItem(self, x, y):
        self.x = x
        self.y = y
        return self.Matrix[self.x][self.y]

    def setItem(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value
        self.Matrix[self.i][self.j] = self.value
        return self.Matrix

    def scaleBy(self, scalar):
        self.scalar = scalar
        for i in range(self.rows):
            for j in range(self.cols):
                self.Matrix[i][j] *= scalar

        return self.Matrix


    def transpose(self):
        self.MatrixT = zip(*self.Matrix)
        for row in self.MatrixT:
            print(row)
