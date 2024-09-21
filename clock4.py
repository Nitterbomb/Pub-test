class Clock():
    twelveHourTime = False
    
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def convert_to_12hour(self):
        hours_12 = self.hours % 12
        if hours_12 == 0:
            hours_12 = 12
        if self.hours < 12:
            meridiem = "AM"
        else:
            meridiem = "PM"
        return hours_12, meridiem    

    def displayStyle(self):
        if self.twelveHourTime == True:
            hours_12, meridiem = self.convert_to_12hour()
            return(f"{hours_12}:{self.minutes:02d}:{self.seconds:02d} {meridiem}")
        else:
            return(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
    
    def addTime(self, hours_to_change, minutes_to_change, seconds_to_change):
        self.seconds += seconds_to_change
        if self.seconds >= 60:
            overflow_minutes = self.seconds // 60
            self.seconds %= 60
            self.minutes += overflow_minutes
        
        self.minutes += minutes_to_change
        if self.minutes >= 60:
            overflow_hours = self.minutes // 60
            self.minutes %= 60
            self.hours += overflow_hours
        
        self.hours += hours_to_change
        if self.hours >= 24:
            self.hours %= 24

    def subtractTime(self, hours_to_change, minutes_to_change, seconds_to_change):
        self.seconds -= seconds_to_change
        if self.seconds < 0:
            overflow_minutes = (abs(self.seconds) + 59) // 60
            self.seconds += overflow_minutes * 60
            self.minutes -= overflow_minutes
        
        self.minutes -= minutes_to_change
        if self.minutes < 0:
            overflow_hours = (abs(self.minutes) + 59) // 60
            self.minutes += overflow_hours * 60
            self.hours -= overflow_hours

        self.hours -= hours_to_change
        while self.hours < 0:
            self.hours += 24
    
    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
            elif self.minutes == other.minutes:
                if self.seconds < other.seconds:
                    return True
        return False
    
    def __le__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
            elif self.minutes == other.minutes:
                if self.seconds <= other.seconds:
                    return True
        return False    

    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes > other.minutes:
                return True
            elif self.minutes == other.minutes:
                if self.seconds > other.seconds:
                    return True
        return False
    
    def __ge__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes > other.minutes:
                return True
            elif self.minutes == other.minutes:
                if self.seconds >= other.seconds:
                    return True
        return False

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.hours != other.hours and self.minutes != other.minutes and self.seconds != other.seconds:
            return True
        else:
            return False
        
def main():
    amount_of_time_instances = int(input("How many different times (at least 2) would you like to enter? "))
    times = []
    
    # loop to validate input and create each time instance
    while len(times)  < amount_of_time_instances:
        hours, minutes, seconds = input("Enter time (hrs:mins:secs): ").split(":")
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)
        if (0 <= hours <= 23) and (0 <= minutes <= 59) and (0 <= seconds <= 59):
            times.append(Clock(hours, minutes, seconds))
        else:
            print("Hours must be between 0-23, minutes must be between 0-59, and seconds must be between 0-59")

    # prints times in both 12 and 24 hour formats
    print(f"first time instance in 24 hour: {times[0].displayStyle()}")
    times[1].twelveHourTime = True
    print(f"second time instance in 12 hour: {times[1].displayStyle()}")
    times[1].twelveHourTime = False
    
    # uses operator overloading to compare times
    if times[0] < times[1]:
        print(f"{times[0].displayStyle()} is earlier than {times[1].displayStyle()}")
    elif times[0] > times[1]:
        print(f"{times[0].displayStyle()} is later than {times[1].displayStyle()}")
    else: 
        print(f"{times[0].displayStyle()} is the same time as {times[1].displayStyle()}")

    # add and subtract times
    print("Add time to first time instance")
    times[0].addTime(int(input('Enter hours to add: ')), int(input('Enter minutes to add: ')), int(input('Enter seconds to add: ')))
    print("Subtract time from second time instance")
    times[1].subtractTime(int(input('Enter hours to subtract: ')), int(input('Enter minutes to subtract: ')), int(input('Enter seconds to subtract: ')))
    
    # uses operator overloading to compare the new times
    if times[0] <= times[1]:
        print(f"{times[0].displayStyle()} is earlier or the same as {times[1].displayStyle()}")
    else:
        print(f"{times[0].displayStyle()} is later than {times[1].displayStyle()}")
   
    if times[0] >= times[1]:
        print(f"{times[0].displayStyle()} is later than or the same as {times[1].displayStyle()}")
    else:
        print(f"{times[0].displayStyle()} is earlier than {times[1].displayStyle()}")
    
    if times[0] == times[1]:
        print(f"{times[0].displayStyle()} is the same as {times[1].displayStyle()}")
    
    if times[0] != times[1]:
        print(f"{times[0].displayStyle()} is not the same as {times[1].displayStyle()}")
    
main()

    
