import math


class Line_Segment:
    def __init__(self):
        self.ptA_x, self.ptA_y = list(map(int, (input("Please enter your FIRST point X_axis and Y_axis \n"
                                                      "separated by white space: ").split())))
        self.ptB_x, self.ptB_y = list(map(int, (input("Please enter your SECOND point X_axis and Y_axis \n"
                                                      "separated by white space: ").split())))

    def endPoint_A(self):
        print(max(self.ptA_x, self.ptA_y))

    def endPoint_B(self):
        print(max(self.ptB_x, self.ptB_y))

    def Length(self):
        print(math.sqrt((self.ptB_x - self.ptA_x) ** 2 + (self.ptB_y - self.ptA_y) ** 2))

    def toString(self):
        print(f"({self.ptA_x},{self.ptA_y})#({self.ptB_x},{self.ptB_y})")

    def isVertical(self):
        if self.ptA_y == self.ptB_y:
            print("Yes the line is parallel to X_axis")
        else:
            print("No, the line isn't parallel to X_axis")

    def isHorizontal(self):
        if self.ptA_x == self.ptB_x:
            print("Yes the line is parallel to Y_axis")
        else:
            print("No, the line isn't parallel to Y_axis")

    def otherPOINT(self):
        self.ptC_x, self.ptC_y = list(map(int, (input("Please enter your FIRST point X_axis and Y_axis \n"
                                                      "separated by white space: ").split())))
        self.ptD_x, self.ptD_y = list(map(int, (input("Please enter your SECOND point X_axis and Y_axis \n"
                                                      "separated by white space: ").split())))

    def isParallel(self):
        self.slop_AB = ((self.ptB_y - self.ptA_y) / (self.ptB_x - self.ptA_x))
        self.slop_CD = ((self.ptD_y - self.ptC_y) / (self.ptD_x - self.ptC_x))

        if self.slop_AB == self.slop_CD:
            print("The lines are parallel")
        else:
            print("The lines aren't parallel")

    def isperpendicular(self):
        if self.slop_AB == -(1 / self.slop_CD) or self.slop_CD == -(1 / self.slop_AB):
            print("the lines are perpendicular. ")
        else:
            print("the lines aren't perpendicular. ")

    def slope(self):
        if self.ptA_y == self.ptB_y:
            return None
        else:
            print(self.slop_AB)

        if self.ptC_y == self.ptD_y:
            return None
        else:
            print(self.slop_CD)

    def shift(self):
        self.xInc = int(input("please enter xInc amount: "))
        self.yInc = int(input("please enter xInc amount: "))

        self.which_line = input("Do u want apply the shift on (AB - CD - Both)")
        if self.which_line == "AB":
            self.ptA_x *= self.xInc
            self.ptB_x *= self.xInc
            self.ptA_y *= self.yInc
            self.ptB_y *= self.yInc
            print(f"({self.ptA_x},{self.ptA_y})#({self.ptB_x},{self.ptB_y})")

        elif self.which_line == "CD":
            self.ptC_x *= self.xInc
            self.ptD_x *= self.xInc
            self.ptC_y *= self.yInc
            self.ptD_y *= self.yInc
            print(f"({self.ptC_x},{self.ptC_y})#({self.ptD_x},{self.ptD_y})")

        else:
            print(f"({self.ptA_x},{self.ptA_y})#({self.ptB_x},{self.ptB_y})")
            print(f"({self.ptC_x},{self.ptC_y})#({self.ptD_x},{self.ptD_y})")

    def midPoint(self):
        self.new_AB_x = ((self.ptB_x + self.ptA_x) / 2)
        self.new_AB_Y = ((self.ptB_y + self.ptA_y) / 2)

        self.new_CD_x = ((self.ptC_x + self.ptD_x) / 2)
        self.new_CD_Y = ((self.ptC_y + self.ptD_y) / 2)

        print(f"{self.new_AB_x} , {self.new_AB_Y}")
        print(f"{self.new_CD_x} , {self.new_CD_Y}")
