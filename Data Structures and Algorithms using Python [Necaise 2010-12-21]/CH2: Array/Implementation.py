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

    def rhsMatrix(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.othMatrix = [[5 for i in range(cols)] for j in range(rows)]
        return self.othMatrix

    def add(self):

        resMatrix = [[0 for i in range(self.cols)] for j in range(self.rows)]
        for i in range(len(self.Matrix)):
            for j in range(len(self.Matrix[0])):
                resMatrix[i][j] = self.Matrix[i][j] + self.othMatrix[i][j]
        return resMatrix


    def subtract(self):

        resMatrix = [[0 for i in range(self.cols)] for j in range(self.rows)]
        for i in range(len(self.Matrix)):
            for j in range(len(self.Matrix[0])):
                resMatrix[i][j] = self.Matrix[i][j] - self.othMatrix[i][j]
        return resMatrix

    def miltible(self):

        resMatrix = [[0 for i in range(self.cols)] for j in range(self.rows)]
        for i in range(len(self.Matrix)):
            for j in range(len(self.Matrix[0])):
                resMatrix[i][j] = self.Matrix[i][j] * self.othMatrix[i][j]
        return resMatrix

