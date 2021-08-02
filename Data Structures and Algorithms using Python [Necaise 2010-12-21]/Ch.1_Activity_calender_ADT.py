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
