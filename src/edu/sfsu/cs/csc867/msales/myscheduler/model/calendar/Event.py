from edu.sfsu.cs.csc867.msales.myscheduler.util.IdentifyableObject import IdentifiableObject
from edu.sfsu.cs.csc867.msales.myscheduler.model.calendar.TimeSlot import TimeSlot
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.User import User
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.Patient import Patient
from edu.sfsu.cs.csc867.msales.myscheduler.model.scheduler.MySchedulerException import MySchedulerException

class Event(IdentifiableObject):
    """ Event holds information about the user who created the event, the time slot chosen for that user, 
    notes for the event and if the event happened or not.
    """
    
    def __new__(cls, user, timeSlot, notes, happened=False):
        """ Constructs a new instance of an Event
        @param user: is an instance of User
        @param timeSlot: is an instance of TimeSlot
        @param notes: additional notes for the event that must be recorded
        @param happened: defines if the appointment has occurred or not 
        """
        cls.__timeSlot = timeSlot
        cls.__notes = notes
        cls.__happened = happened
        
        if (type(user) != User and type(user) != Patient):
            raise MySchedulerException("The event must be associated with a user", {"user" : user})
        cls.__user = user
        
        return super(Event, cls).__new__(cls)
    
    def __init__(self, user, timeSlot, notes, happened):
        IdentifiableObject.__init__(self)
        self.__user = user
        self.__timeSlot = timeSlot
        self.__notes = notes
        self.__happened = happened
    
    def getUser(self):
        return self.__user
    
    def getTimeSlot(self):
        return self.__timeSlot
    
    def getNotes(self):
        return self.__notes
    
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

