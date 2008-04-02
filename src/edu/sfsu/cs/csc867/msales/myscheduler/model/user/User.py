from edu.sfsu.cs.csc867.msales.myscheduler.util.IdentifyableObject import IdentifiableObject

class User(IdentifiableObject):
    "The User is a regular user with first name, last name and email address. It's the basic user for any system."
    
    def __new__(cls, firstName, lastName, email):
        cls.__firstName = firstName
        cls.__lastName = lastName
        cls.__email = email
        
        return super(User, cls).__new__(cls)
    
    def __init__(self, firstName, lastName, email):
        IdentifiableObject.__init__(self)
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
    
    def printAll(self):
        print "[" +  str(self.getId()) + "]: " + self.getLastName() + ", " + self.getFirstName() + " (" + self.getEmail() + ")"
        print "Created on " + self.getHumanReadableDateTime()
        
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getEmail(self):
        return self.__email
    
    def __eq__(self, o):
        if isinstance(o, self.__class__):
            return self.getEmail() == o.getEmail()
    
    def __ne__(self, o):
        return not self == o
    
    def __hash__(self):
        return self.getEmail().__hash__()