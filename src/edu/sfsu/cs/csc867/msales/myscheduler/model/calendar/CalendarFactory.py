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
    
    def buildNewTimeSlot(self, datetimeInst, format, durationValue, durationType):
        """ Builds  new instance of TimeSlot
        @param datetimeInst: is a format of the datetime
        @param format: is the format that matches the datetime provided
        @param durationValue: is a positive integer to be added for the duration
        @param durationType: is one of the following: d = day, h = hour, m = minute
        """
        duration = int(durationValue) , durationType
        return TimeSlot(datetime(*strptime(datetimeInst, format)[0:6]), duration)

    def buildNewEvent(self, user, datetime, durationValue, durationType, notes, location = "", zipCode = "94132", 
                      happened = False):
        """Builds a new Event instance based on the time slot information and notes
        @param user: an instance of User. Use one of the UsersFactory methods
        @param datetime: is a format of the datetime
        @param format: is the format that matches the datetime provided
        @param durationValue: is a positive integer to be added for the duration
        @param durationType: is one of the following: d = day, h = hour, m = minute
        @param notes: notes for the event
        """
        slot = self.buildNewTimeSlot(datetime, TimeSlot.DEFAULT_DATETIME_FORMAT, durationValue, durationType)
        return Event(user, slot, notes.strip(), location.strip(), "94132" if zipCode == "" else zipCode, happened)
    
    def buildNewEventWithTimeSlot(self, user, timeSlot, notes, location = "", zipCode = "94132", happened = False, id=-1):
        """ Builds a new Event instance based on an instance of TimeSlot and notes
        @param user: an instance of User. Use one of the UsersFactory methods
        @param timeSlot: an instance of TimeSlot. Use CalendarFactory.buildNewTimeSlot method
        @param notes: notes for the event
        """
        notes = notes.strip() if (notes != "") else notes
        
        try:
            loc = location.value.strip()
        except Exception:
            loc = ""
            
        try:
            zipC = "94132" if location.zipCode == "" else location.zipCode
        except Exception:
            zipC = "94132"
            
        return Event(user, timeSlot, notes, loc, zipC, happened, id)
    
    def buildNewCalendar(self, owner, eventList = []):
        """ Builds a new Calendar for a given owner with an optional list of events
        @param owner: an instance of User. Use one of the UsersFactory methods
        @param timeSlot: an instance of TimeSlot. Use CalendarFactory.buildNewTimeSlot method
        @param notes: notes for the event
        """
        return Calendar(owner, eventList)
    
    def buildEventFromDictionary(self, eventDic):
        from edu.sfsu.cs.csc867.msales.myscheduler.controller.UserController import UserController
        
        dateTime = eventDic.timeSlot.date + " " + eventDic.timeSlot.time
        timeSlot = self.buildNewTimeSlot(dateTime, TimeSlot.DEFAULT_DATETIME_FORMAT, int(eventDic.timeSlot.duration[0]), 
                                         eventDic.timeSlot.duration[1])
        user = UserController().getUser(eventDic.userId)
        return self.buildNewEventWithTimeSlot(user, timeSlot, eventDic.notes,
                                              eventDic.location, eventDic.location.zipCode, eventDic.happened, eventDic.id)

    def buildCalendarFromDictionary(self, calendarDic):
        if (len(calendarDic.event) == 1):
            event = self.buildEventFromDictionary(calendarDic.event)
            events = [event]
        else:
            events = []
            for event in calendarDic.event:
                events.append(self.buildEventFromDictionary(event))
        
        from edu.sfsu.cs.csc867.msales.myscheduler.controller.UserController import UserController
        owner = UserController().getUser(calendarDic.ownerId)
        return Calendar(owner, events, calendarDic.id)

if __name__ == '__main__':
    
    s = "2005-12-06 12:13:00"
    s2 = "2005-12-06 13:14:00"
    f = "%Y-%m-%d %H:%M:%S" 
    a = CalendarFactory().buildNewTimeSlot(s, f, 1, TimeSlot.DURATION_HOUR)
    b = CalendarFactory().buildNewTimeSlot(s2, f, 2, TimeSlot.DURATION_HOUR)

    pat = UsersFactory().buildNewUser("Marcello", "de Sales", "msales@sfsu.edu", "msales", "1234")
    
    e = CalendarFactory().buildNewEvent(pat, a, "We have to meet at that date...", "81 Woodrow St")
    e1 = CalendarFactory().buildNewEvent(pat, b, "To review the options...", "", "", True)
    
    print e.toXML()
    print ""
    print e1.toXML()
    
    doct = UsersFactory().buildNewUser("kevin", "Smith", "ksmith@sfsu.edu", "kevin", "223")
    
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
    
    print cal.toXML()
    
#    cal.printAll()
#    print e.getId()
#    print e.getHumanReadableDateTime()
#    print e.hasHappened()
#    print e.getTimeSlot().getShortHumanReadable()
#    print e.getNotes()
#    print "\n%%%%%%%%%%% Info about the User #############"
#    print e.getUser().printAll()