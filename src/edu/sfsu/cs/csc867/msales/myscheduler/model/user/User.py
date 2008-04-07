from edu.sfsu.cs.csc867.msales.myscheduler.util.IdentifyableObject import IdentifiableObject

class User(IdentifiableObject):
    "The User is a regular user with first name, last name and email address. It's the basic user for any system."
    
    def __new__(cls, firstName, lastName, email, username, password, id=-1):
        cls.__firstName = firstName
        cls.__lastName = lastName
        cls.__email = email
        cls.__username = username
        cls.__password = password
        
        return super(User, cls).__new__(cls, id)
    
    def __init__(self, firstName, lastName, email, username, password, id=-1):
        IdentifiableObject.__init__(self, id)
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__username = username
        self.__password = password
            
    def printAll(self):
        print "[" +  str(self.getId()) + "]: " + self.getLastName() + ", " + self.getFirstName() + " (" + self.getEmail() + ")"
        print "Created on " + self.getHumanReadableCreationdateTime()
        
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getEmail(self):
        return self.__email
    
    def getUsername(self):
        return self.__username
    
    def getPassword(self):
        return self.__password
    
    def __eq__(self, o):
        if isinstance(o, self.__class__):
            return  self.getUsername() == o.getUsername()
    
    def __ne__(self, o):
        return not self == o
    
    def __hash__(self):
        return self.getEmail().__hash__()
    
    
    def toXML(self):
        namespace = "myscheduler:"
        return  "<" + namespace + "user id=\"" + self.getId() + "\" username=\"" + self.getUsername() \
                   + "\" password=\"" + self.getPassword() + "\" xmlns:myscheduler=\"http://cs.sfsu.edu/csc867/myscheduler\">" \
                  "<" + namespace + "firstName>" + self.getFirstName() +"</" + namespace + "firstName>" \
                  "<" + namespace + "lastName>" + self.getLastName() + "</" + namespace + "lastName>" \
                  "<" + namespace + "email>" + self.getEmail() + "</" + namespace + "email>" \
                "</" + namespace + "user>"