from edu.sfsu.cs.csc867.msales.myscheduler.util.Singleton import Singleton
from edu.sfsu.cs.csc867.msales.myscheduler.model.calendar.TimeSlot import TimeSlot
from edu.sfsu.cs.csc867.msales.myscheduler.model.calendar.Event import Event
from edu.sfsu.cs.csc867.msales.myscheduler.model.calendar.Calendar import Calendar
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.UsersFactory import UsersFactory
from edu.sfsu.cs.csc867.msales.myscheduler.model.scheduler.MySchedulerException import MySchedulerException

from datetime import datetime
from datetime import date
from time import strptime 

class CalendarFactory(Singleton):
    """
    CalendarFactory is responsible for the building new instances of the Calendar objects.
    """
    
    def buildNewTimeSlot(self, instance, format, durationValue, durationType):
        """ Builds  new instance of TimeSlot
        @param instance: is a format of the datetime
        @param format: is the format that matches the datetime provided
        @param durationValue: is a positive integer to be added for the duration
        @param durationType: is one of the following: d = day, h = hour, m = minute
        """
        duration = durationValue , durationType
        return TimeSlot(datetime(*strptime(instance, format)[0:6]), duration)

    def buildNewEvent(self, user, instance, format, durationValue, durationType, notes, happened = False):
        """ Builds a new Event instance based on the time slot information and notes
        @param user: an instance of User. Use one of the UsersFactory methods
        @param instance: is a format of the datetime
        @param format: is the format that matches the datetime provided
        @param durationValue: is a positive integer to be added for the duration
        @param durationType: is one of the following: d = day, h = hour, m = minute
        @param notes: notes for the event
        """
        slot = self.buildNewTimeSlot(instance, format, durationValue, durationType)
        return Event(user, slot, notes, happened)
    
    def buildNewEvent(self, user, timeSlot, notes, happened = False):
        """ Builds a new Event instance based on an instance of TimeSlot and notes
        @param user: an instance of User. Use one of the UsersFactory methods
        @param timeSlot: an instance of TimeSlot. Use CalendarFactory.buildNewTimeSlot method
        @param notes: notes for the event
        """
        return Event(user, timeSlot, notes, happened)
    
    def buildNewCalendar(self, owner, eventList = []):
        """ Builds a new Calendar for a given owner with an optional list of events
        @param owner: an instance of User. Use one of the UsersFactory methods
        @param timeSlot: an instance of TimeSlot. Use CalendarFactory.buildNewTimeSlot method
        @param notes: notes for the event
        """
        return Calendar(owner, eventList)

if __name__ == '__main__':
    
    s = "2005-12-06 12:13:00"
    s2 = "2005-12-06 13:14:00"
    f = "%Y-%m-%d %H:%M:%S"
    a = CalendarFactory().buildNewTimeSlot(s, f, 1, TimeSlot.DURATION_HOUR)
    b = CalendarFactory().buildNewTimeSlot(s2, f, 2, TimeSlot.DURATION_HOUR)

    pat = UsersFactory().buildNewPatient("Marcello", "de Sales", "msales@sfsu.edu", date(1979,12,15))
    
    e = CalendarFactory().buildNewEvent(pat, a, "We have to meet at that date...")
    e1 = CalendarFactory().buildNewEvent(pat, b, "To review the options...", True)
    
    doct = UsersFactory().buildNewUser("kevin", "Smith", "ksmith@sfsu.edu")
    
    print a.getShortHumanReadable()
    print b.getShortHumanReadable()
    
    cal = CalendarFactory().buildNewCalendar(doct, [e])
    try:
        cal.addEvent(e1)
    except MySchedulerException, addException:
        print addException.message

    try:
        s = "2005-12-06 17:10:00"
        newEvent = CalendarFactory().buildNewEvent(pat, CalendarFactory().buildNewTimeSlot(s, f, 5, 
                                                    TimeSlot.DURATION_HOUR), "A new different topic...")
        cal.addEvent(newEvent)
    except MySchedulerException, addException:
        print addException.message
    
    cal.printAll()
    
#    cal.printAll()
#    print e.getId()
#    print e.getHumanReadableDateTime()
#    print e.hasHappened()
#    print e.getTimeSlot().getShortHumanReadable()
#    print e.getNotes()
#    print "\n%%%%%%%%%%% Info about the User #############"
#    print e.getUser().printAll()