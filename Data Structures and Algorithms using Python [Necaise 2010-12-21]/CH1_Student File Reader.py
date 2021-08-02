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
