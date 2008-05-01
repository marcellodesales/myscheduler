from edu.sfsu.cs.csc867.msales.myscheduler.util.IdentifyableObject import IdentifiableObject
from edu.sfsu.cs.csc867.msales.myscheduler.model.calendar.TimeSlot import TimeSlot
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.User import User
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.Patient import Patient
from edu.sfsu.cs.csc867.msales.myscheduler.model.scheduler.MySchedulerException import MySchedulerException

class Event(IdentifiableObject):
    """ Event holds information about the user who created the event, the time slot chosen for that user, 
    notes for the event and if the event happened or not.
    """
    
    def __new__(cls, user, timeSlot, notes, location="", zipCode="94132", happened=False, id=-1):
        """ Constructs a new instance of an Event
        @param user: is an instance of User
        @param timeSlot: is an instance of TimeSlot
        @param notes: additional notes for the event that must be recorded
        @param happened: defines if the appointment has occurred or not 
        """
        cls.__timeSlot = timeSlot
        cls.__notes = notes.strip()
        cls.__happened = happened
        cls.__location = location
        cls.__zipCode = zipCode
        
        if (type(user) != User and type(user) != Patient):
            raise MySchedulerException("The event must be associated with a user", {"user" : user})
        cls.__user = user
        
        return super(Event, cls).__new__(cls, id)
    
    def __init__(self, user, timeSlot, notes, location, zipCode, happened, id=-1):
        IdentifiableObject.__init__(self, id)
        self.__user = user
        self.__timeSlot = timeSlot
        self.__notes = notes
        self.__happened = happened
        self.__location = location
        self.__zipCode = zipCode
            
    def getUser(self):
        return self.__user
    
    def getTimeSlot(self):
        return self.__timeSlot
    
    def getNotes(self):
        return self.__notes

    def getLocation(self):
        return self.__location

    def getZipCode(self):
        return self.__zipCode
    
    def setNotes(self, notes):
        self.__notes = notes
    
    def hasHappened(self):
        return self.__happened
    
    def happened(self):
        self.__happened = True
    
    def __eq__(self, o):
        if isinstance(o, self.__class__):
            return self.getTimeSlot() == o.getTimeSlot()
    
    def __ne__(self, o):
        return not self == o
    
    def printAll(self):
        print "######### " + self.getId() + ": " + self.getTimeSlot().getFullHumanReadable() + " #############"
        self.getUser().printAll()
        print "Notes: " + self.getNotes()
        print "Has Happened? " + str(self.hasHappened())
        print "########################################################################"

    def __hash__(self):
        return self.getTimeSlot().__hash__()

    def toXML(self):
        namespace = "myscheduler:"
        maintag = "event"
        from string import lower
        return  "<" + namespace + maintag + " happened=\"" + lower(str(self.hasHappened())) + "\" userId=\"" + \
                       str(self.getUser().getId()) + "\">" + \
                       self.getTimeSlot().toXML() + \
                       "<" + namespace + "location zipCode=\"" + self.getZipCode() + "\">" + self.getLocation() + \
                       "</" + namespace + "location>" + \
                       "<" + namespace + "notes>" + self.getNotes() + "</" + namespace + "notes>" + \
                "</" + namespace + maintag + ">"