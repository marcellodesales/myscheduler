from edu.sfsu.cs.csc867.msales.myscheduler.model.scheduler.MySchedulerException import MySchedulerException

from datetime import datetime
from datetime import date
from datetime import time
from time import strptime

class TimeSlot(object):
    "TimeSlot represents the date and time slot for a given calendar. It has information about date, time, duration." 

    DURATION_HOUR = "h"
    DURATION_MINUTE = "m"
    DURATION_DAY = "d"
    
    def __new__(cls, dateTime="null",  duration=(1,"h")):
        """
        Constructs a new TimeSlot instance with a date, time and duration
        @param dateTime: is an instance of datetime
        @param duration: (X,[s|m|h]) is tuple that consists of a positive integer indicating the duration of this
        time slot and a char representing the type of duration. Use the constants defined on this class.
        """
        if (dateTime == "null"):
            now = datetime.today().timetuple()
            cls.__dateTime = datetime(now[0], now[1], now[2], now[3], now[4], now[5], now[6]) 
        else:
            cls.__dateTime = dateTime
        if (type(duration) != tuple):
            raise MySchedulerException("The duration must be ", varsValueDic)
        cls.__duration = duration
        
        return super(TimeSlot, cls).__new__(cls)
    
    def __init__(self, dateTime, duration):
        self.__dateTime = dateTime
        self.__duration = duration

    def getDate(self):
        return self.__dateTime.date()

    def getStartDateTime(self):
        return self.__dateTime

    def getDurationTuple(self):
        '''Duration is a tuple consisting of a positive integer and a char representing hour or minute. If not provided, 
        the duration will be added to the hour'''
        return self.__duration
    
    def getDurationString(self):
        duration = self.getDurationTuple()
        
        if (duration[1] == "d"):
            what = "days" if duration[0] > 1 else "day"
        if (duration[1] == "h"):
            what = "hours" if duration[0] > 1 else "hour"
        if (duration[1] == "m"):
            what = "minutes" if duration[0] > 1 else "minute"
        
        return str(duration[0]) + " " + what

    def getEndDateTime(self):
        app = self.getStartDateTime()
        duration = self.getDurationTuple()
        if (duration[1] == "d"):
            return datetime(app.year, app.month, app.day + duration[0], app.hour, app.minute, app.second)
        if (duration[1] == "h"):
            return datetime(app.year, app.month, app.day, app.hour + duration[0], app.minute, app.second)
        if (duration[1] == "m"):
            return datetime(app.year, app.month, app.day, app.hour, app.minute + duration[0], app.second)
        else:
            return datetime(app.year, app.month, app.day, app.hour + 1, app.minute, app.second)

    def getFullHumanReadable(self):
        day = self.getStartDateTime().strftime("%A, %B %d, %Y")
        start = self.getStartDateTime().strftime("%H:%M")
        end = self.getEndDateTime().strftime("%H:%M")
        
        if (self.getDurationTuple()[1] == "d"):
            end = self.getEndDateTime().strftime("%A, %B %d, %Y %H:%M")
        
        return day + " for " + self.getDurationString() + ": [" + start + " -> " + end + "]"

    def getShortHumanReadable(self):
        start = self.getStartDateTime().strftime("%H:%M")
        end = self.getEndDateTime().strftime("%H:%M")
        return start + " -> " + end
    
    def conflicts(self, o):
        selfStartDateTime = self.getStartDateTime()
        oStartDateTime = o.getStartDateTime()
        if (selfStartDateTime.year == oStartDateTime.year and \
            selfStartDateTime.month == oStartDateTime.month and \
            selfStartDateTime.day == oStartDateTime.day):
            if (selfStartDateTime.hour == oStartDateTime.hour and selfStartDateTime.minute == oStartDateTime.minute):
                return true
            return false
            
        else:
            return false
        
    
    def __eq__(self, o):
        if isinstance(o, self.__class__):
            selfStartDateTime = self.getStartDateTime()
            oStartDateTime = o.getStartDateTime()
            selfEndDateTime = self.getEndDateTime()
            oEndDateTime = o.getEndDateTime()
            
            return selfStartDateTime.year == oStartDateTime.year and \
                   selfStartDateTime.month == oStartDateTime.month and \
                   selfStartDateTime.day == oStartDateTime.day and \
                   selfStartDateTime.hour == oStartDateTime.hour and \
                   selfStartDateTime.minute == oStartDateTime.minute and \
                   selfEndDateTime.year == oEndDateTime.year and \
                   selfEndDateTime.month == oEndDateTime.month and \
                   selfEndDateTime.day == oEndDateTime.day and \
                   selfEndDateTime.hour == oEndDateTime.hour and \
                   selfEndDateTime.minute == oEndDateTime.minute
    
    def __ne__(self, o):
        return not self == o

    def __hash__(self):
        return self.getStartDateTime().__hash__() + self.getEndDateTime().__hash__()

if __name__ == '__main__':
    
    s = "2005-12-06 12:13:14"
    f = "%Y-%m-%d %H:%M:%S"
    
    
    
    stotA.getFullHumanReadable()
    
#    >>> s = "2005-12-06T12:13:14"
#    >>> from datetime import datetime
#    from time import strptime
#    >>> datetime(*strptime(s, "%Y-%m-%dT%H:%M:%S")[0:6])
#    from datetime import date
#    now = datetime.today()
#    print now.strftime("%m-%d-%Y. %b %d, %Y is a %A on the %d day of %B.")
#    
#    print datetime(*strptime(s, f)[0:6]).strftime("%A, %b %d, %Y is a on the %d day of %B. %H:%M:%S")
    
    
#    print now

#    from datetime import date
#    now = datetime.today().timetuple()
#    app = datetime(now[0], now[1], now[2], now[3], now[4], now[5], now[6]) 
#    duration = 23,"h"