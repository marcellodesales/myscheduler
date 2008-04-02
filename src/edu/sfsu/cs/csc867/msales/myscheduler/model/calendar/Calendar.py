from edu.sfsu.cs.csc867.msales.myscheduler.util.IdentifyableObject import IdentifiableObject
from edu.sfsu.cs.csc867.msales.myscheduler.model.calendar.Event import Event
from edu.sfsu.cs.csc867.msales.myscheduler.model.scheduler.MySchedulerException import MySchedulerException#


class Calendar(IdentifiableObject):
    """
    Calendar represents the entire calendar for a given owner (user) on the system, which is aggregated by
    a set of different events
    """
    
    def __new__(cls, owner, eventList = []):
        return super(Calendar, cls).__new__(cls)

    def __init__(self, owner, eventList):
        IdentifiableObject.__init__(self)
        self.__owner = owner
        self.__eventList = set(eventList)

    def getOwner(self):
        return self.__owner

    def getEventSet(self, date=-1):
        if (date == -1):
            return self.__eventList
        else:
            return self.__eventList
    
    def addEvent(self, event):
        if (not isinstance(event, Event)):
            eT = type(event)
            print eT
            a = {"event" : eT}
            raise MySchedulerException("Event must be an instance of Event class", a)
        
        startDate = event.getTimeSlot().getStartDateTime()
        endDate = event.getTimeSlot().getEndDateTime()
        for existingEvent in sorted(self.getEventSet(startDate.date)):
            exStartDate = existingEvent.getTimeSlot().getStartDateTime()
            exEndDate = existingEvent.getTimeSlot().getEndDateTime()
            if (startDate  < exStartDate):
                if (endDate >= exStartDate):
                    raise MySchedulerException("New event conflicts with the start time of an existing one at " + str(exStartDate), {"event" : event})
            if (startDate >= exStartDate and startDate <= exEndDate):
                raise MySchedulerException("New event conflicts with the duration of an existing one at " + 
                                           str(exStartDate), {"event" : event})
            print str(existingEvent.getId()) + "New event doesn't conflict with event at " + str(exStartDate) + " " + str(exEndDate)
        self.__eventList.add(event)
    
    def containsStartDateTimeSet(self):
        sDTset = set([])
        for ev in self.getEventSet():
            sDTset.add(ev.getStartDateTime())
        return sDTset
    
    def hasEvent(self, event):
        return event in self.__eventList
    
    def removeEvent(self, event):
        self.__eventList.discard(event)
    
    def __eq__(self, o):
        if isinstance(o, self.__class__):
            return self.getOwner() == o.getOwner()

    def __ne__(self, o):
        return not self == o
    
    def __hash__(self):
        return self.getOwner().__hash__()
    
    def printAll(self):
        
        print "Owner Information -------- "
        print "Number of events: " + str(len(self.getEventSet()))
        self.getOwner().printAll()
        
        for ev in sorted(self.getEventSet()):
            ev.printAll()
            print "\n"