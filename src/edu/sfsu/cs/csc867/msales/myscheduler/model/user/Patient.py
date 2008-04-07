from edu.sfsu.cs.csc867.msales.myscheduler.model.user.User import User
from edu.sfsu.cs.csc867.msales.myscheduler.model.scheduler.MySchedulerException import MySchedulerException#

from datetime import date

class Patient(User):
    "Patient is a User that has a birthday attribute."
    
    def __new__(cls, firstName, lastName, email, birthday, id=-1):
        "Constructs a new Patient with the all the information from a User, plus the birthday date"
        
        if (not isinstance(birthday, date)):
            birthType = type(birthday)
            raise MySchedulerException("Birthday attribute of Patient must be an instance of Date", 
                                       {"birthday": birthType})
        cls.__birthday = birthday
        return super(Patient, cls).__new__(cls, firstName, lastName, email, id)
    
    def __init__(self, firstName, lastName, email, birthday, id=-1):
        User.__init__(self, firstName, lastName, email, id)
        self.__birthday = birthday
        
    def getBirthDay(self):
        """
        Returns an instance of Date representing the birthday of the patient
        """
        return self.__birthday
    
    def printAll(self):
        User.printAll(self)
        print "Birthday: "  + str(self.getBirthDay())
    
    def __eq__(self, o):
        if isinstance(o, self.__class__):
            return User.__eq__(self, o)
    
    def __ne__(self, o):
        return not self == o
