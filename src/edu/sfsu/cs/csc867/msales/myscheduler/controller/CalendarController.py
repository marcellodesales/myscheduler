from edu.sfsu.cs.csc867.msales.myscheduler.util.Singleton import Singleton
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.UsersFactory import UsersFactory
from edu.sfsu.cs.csc867.msales.myscheduler.data.XMLPersistence import XMLPersistence
from edu.sfsu.cs.csc867.msales.myscheduler.model.calendar.CalendarFactory import CalendarFactory

class CalendarController(Singleton):

    def createNewEvent(self, userId, date, time, durationValue, durationType, notes, location, zipCode):
        """
        Creates a new user in the system
        @param firstName: user's first name
        @param lastName: user's last name
        @param email: user's email address
        @param username: the username used to login. It's an alpha-character
        @param password: the password matching the login provided
        @raise UserPasswordNotMatchException: if the given password doesn't match the user found
        @raise UserNotFoundException: if the given username could not be found on the system
        """
        CalendarFactory().buildNewEvent(user, datetime, durationValue, durationType, notes, location, zipCode)
        
        if (XMLPersistence().userExists(newUser)):
            raise UserAlreadyExistsException("User already exists with the given email!", {'email':user.getEmail()} )
        else:
            XMLPersistence().saveUser(newUser)
        return newUser
    
    def getCalendar(self, calendarId):
        return XMLPersistence().getCalendar(calendarId)

    def getCalendarByOwner(self, ownerId):
        return XMLPersistence().getCalendarByOwner(ownerId)
    
    def saveCalendar(self, calendar):
        XMLPersistence().saveCalendar(calendar)
    
if __name__ == '__main__':
    
    calendar = CalendarController().getCalendar("1208309768316")
    otherCal = CalendarController().getCalendarByOwner("1208309768264")
    print calendar.getId() == otherCal.getId()
    
    s = "2009-12-06 11:03:11"
    f = "%Y-%m-%d %H:%M:%S" 
    ts = CalendarFactory().buildNewTimeSlot(s, f, 1, "h")
    
    e = CalendarFactory().buildNewEventWithTimeSlot(calendar.getOwner(), ts,
                                                     "TEsting online", "10016""Bridge St")
    
    calendar.addEvent(e)
    
    CalendarController().saveCalendar(calendar)
    
    
    
    #calendar.printAll()

    
    
    #marcelloLogged = UserController().doLogin("msales", "utn29oad")
    #marcelloLogged.printAll()
