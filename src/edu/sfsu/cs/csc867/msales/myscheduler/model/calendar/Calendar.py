from edu.sfsu.cs.csc867.msales.myscheduler.util.IdentifyableObject import IdentifiableObject
from edu.sfsu.cs.csc867.msales.myscheduler.model.calendar.Event import Event
from edu.sfsu.cs.csc867.msales.myscheduler.model.scheduler.MySchedulerException import MySchedulerException#


class Calendar(IdentifiableObject):
    """
    Calendar represents the entire calendar for a given owner (user) on the system, which is aggregated by
    a set of different events
    """
    
    def __new__(cls, owner, eventList = []):
        cls.__owner = owner
        cls.__eventList = set(eventList)
        
        return super(Calendar, cls).__new__(cls)

    def __init__(self, owner, eventList):
        self.__owner = owner
        self.__eventList = set(eventList)

    def getOwner(self):
        return self.__owner

    def getEventSet(self):
        return self.__eventList
    
    def addEvent(self, event):
        if (type(event) != Event):
            raise MySchedulerException("Event must be an instance of Event class", {"event" : event})
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
        
        for ev in self.getEventSet():
            ev.printAll()
            print "\n"