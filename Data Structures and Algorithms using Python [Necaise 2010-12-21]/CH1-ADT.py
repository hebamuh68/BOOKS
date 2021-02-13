"""1.2 A Grab Bag ADT is similar to the Bag ADT with one difference. A grab
bag does not have a remove() operation, but in place of it has a grabItem()
operation, which allows for the random removal of an item from the bag.
Implement the Grab Bag ADT."""


import random
class Bag():

    def addItems(self):
        self.Items = list(map(int, input("please enter your items: ").split()))
        return self.Items

    def grapItemRandomely(self):
        random_Item = random.choice(self.Items)
        self.Items.remove(random_Item)
        return self.Items
        
   
    def numOF(self):
        return len(self.Items)

__________________________________________________________________________
"""1.3 A Counting Bag ADT is just like the Bag ADT but includes the numOf(item)
operation, which returns the number of occurrences of the given item in the
bag. Implement the Counting Bag ADT and defend your selection of data
structure.

1.4 The use of the Student File Reader ADT makes it easy to extract student
records from a text file no matter the format used to store the data. Implement
a new version of the ADT to extract the data from a text file in which each
record is stored on a separate line and the individual fields are separated by
commas. For example, the following illustrates the format of a sample file
containing three student records:
    
10015, John, Smith, 2, 3.01
10334, Jane, Roberts, 4, 3.81
10208, Patrick, Green, 1, 3.95

1.5 In the chapter, we defined and implemented the Student File Reader ADT for
extracting student records from an external source. We can define and use a
similar ADT for output."""


class StudentFileReader:

    def __init__(self):
        self.my_file = open(input("pleas enter the file name: "), "r+")
        self.lines = self.my_file.readlines()

    def Extract_specic_record(self):
        self.studentName = input("please enter the student name: ")
        for line in self.lines:
            if self.studentName in line:
                print(line)

    def StudentRecord(self):

        self.another_process = input("Do you want to add another record (Y/N): ")
        while self.another_process == "Y":
            self.Studen_ID = input("please enter the student ID: ")
            self.Studen_First_Name = input("please enter the student first name: ")
            self.Studen_Last_Name = input("please enter the student last name: ")
            self.Studen_Grade = input("please enter the student grade: ")
            self.Studen_GPA = input("please enter the student GPA: ")

            RecoreList = [self.Studen_ID, self.Studen_First_Name, self.Studen_Last_Name,
                          self.Studen_Grade, self.Studen_GPA]

            self.my_file.write(", ".join(RecoreList))
            self.my_file.write("\n")

            self.another_process = input("\n Do you want to add another record (Y/N): ")

        else:
            print("The records have written, Thanks! ")
      
__________________________________________________________________________
"""1.6 We can use a Time ADT to represent the time of day, for any 24-hour period,
as the number of seconds that have elapsed since midnight. Given the following
list of operations, implement the Time ADT."""


class Time_ADT:
    def __init__(self):
        self.hours, self.minutes, self.seconds = list(
            map(int, input("Please enter the Hours, Minutes, Seconds. separated by white space \n"
                           "please enter the time in 24 hours format: ").split()))

    def Hours(self):
        print(self.hours)

    def Minutes(self):
        print(self.minutes)

    def Seconds(self):
        print(self.seconds)

    def Num_Seconds(self):
        RestHours = (24 - self.hours) * 60 * 60
        RestSeconds = (self.minutes * 60) + self.seconds + RestHours
        return RestSeconds

    def isAM(self):
        if self.hours == 12:
            print("It's mid day ")
        elif self.hours > 12:
            print("It's morning ")
        else:
            print("It's meridiem ")

    def toString(self):
        if self.hours > 12:
            print("The time now is " + str(self.hours - 12) + ":" + str(self.minutes) + ":" + str(self.seconds))
        else:
            print("The time now is   " + str(self.hours ) + ":" + str(self.minutes) + ":" + str(self.seconds))

__________________________________________________________________________
"""1.8 A line segment is a straight line bounded by two endpoints. The Line Segment
ADT, whose operations are described below, represents a line segment defined
by points in the two-dimensional Cartesian coordinate system. Use the Point
class from Appendix D and implement the Line Segment ADT."""


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
        
__________________________________________________________________________
"""1.10 Anyone who is involved in many activities typically uses a calendar to keep
track of the various activities. Colleges commonly maintain several calendars
such as an academic calendar, a school events calendar, and a sporting events
calendar. We have defined an Activities Calendar ADT below that can keep
track of one activity per day over a given range of dates. Select a data structure
and implement the ADT."""


class Activity_calender_ADT:

    def __init__(self):
        self.file = open("/home/hebaallah/1-MIT/Python/calender.txt", "r+")
        self.lines = self.file.readlines()

    def Add_activity(self):
        self.DateFrom = input(
            "Please enter the date from which you'll start the task\n(day then month,separated by white space): ")
        self.DateTo = input("Please enter the deadline of the task\n(day then month,separated by white space): ")
        self.file.write(f"Date: {self.DateFrom} : {self.DateTo}\n")

        self.new_activity = input("please enter the activity: ")
        self.file.write(f"- {self.new_activity}\n\n")

        self.another_process = input("Do you want to add another record (Y/N): ")
        while self.another_process == "Y":
            self.Add_activity()

    def getActivity(self):
        self.TargetDate = input("PLease enter the date of the activity you want: ")

        for line in range(len(self.lines)):
            self.lines[line] = self.lines[line].split()
            if self.TargetDate in self.lines[line]:
                print(self.lines[line + 1])

    def length(self):
        self.NoneLine = 0
        for Nline in self.lines:
            if Nline.strip():
                self.NoneLine += 1
        print(self.NoneLine // 2)

    def displayMonth(self):
        self.month = input("Please enter the month you want to display its activities: ")

        for line in range(len(self.lines)):
            if not self.lines[line].rstrip():
                continue

            else:
                self.lines[line] = self.lines[line].split()
                self.lineItems = self.lines[line]

                if self.lineItems[0] == "Date:" and self.month == self.lineItems[2]:
                    print(self.lines[line + 1])





