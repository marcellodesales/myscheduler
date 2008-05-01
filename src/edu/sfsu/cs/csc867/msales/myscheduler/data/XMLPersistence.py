from edu.sfsu.cs.csc867.msales.myscheduler.util.Singleton import Singleton
from edu.sfsu.cs.csc867.msales.myscheduler.util.XMLToDic import XMLToDic
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.UsersFactory import UsersFactory
from edu.sfsu.cs.csc867.msales.myscheduler.data.UserAlreadyExistsException import UserAlreadyExistsException 
from edu.sfsu.cs.csc867.msales.myscheduler.data.UserPasswordNotMatchException import UserPasswordNotMatchException
from edu.sfsu.cs.csc867.msales.myscheduler.data.UserNotFoundException import UserNotFoundException
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.UsersFactory import UsersFactory
from edu.sfsu.cs.csc867.msales.myscheduler.model.calendar.CalendarFactory import CalendarFactory

from xml.dom.minidom import parseString, parse
import xml.dom.ext
from xml.etree import cElementTree as eT

global usersDataSet, calendarsDataSet 
usersDataSet = "/home/marcello/development/workspace-sfsu/MyScheduler/data/users.xml"
calendarsDataSet = "/home/marcello/development/workspace-sfsu/MyScheduler/data/calendars.xml"

class XMLPersistence(Singleton):
    
    def add(self, xmlElement, parentElementName, filePath):
        """
        Save the xmlElement as a child of the given parentElementName from the given filePath
        """
        document = parse(filePath)

        rootCollection = document.getElementsByTagName(parentElementName)
        rootElement = rootCollection.item(0)
        rootElement.appendChild(xmlElement)

        xml.dom.ext.PrettyPrint(document, open(filePath, "w"))
        
    def updateUser(self, user):
        document = parse(usersDataSet)
        
        rootCollection = document.getElementsByTagName("myscheduler:user")
        
        for userNode in rootCollection: 
            
            xml.dom.ext.PrettyPrint(document, a)
            
            userDic = XMLToDic().getDictionaryFromXMLString(a)
            if (userDic.id == user.getId()):
                document.removeChild(userNode)
                newUserElement = parseString(user.toXML())
                newUserElement.removeAttribute("xmlns:myscheduler")
                document.appendChild(newUserElement)
        
        xml.dom.ext.PrettyPrint(document, open(usersDataSet, "w"))

    def updateCalendar(self, calendar):
        document = parse(calendarsDataSet)
        
        rootCollection = document.getElementsByTagName("myscheduler:calendars").getroot()
        
        for calNode in rootCollection.get:
            userDic = XMLToDic().getDictionaryFromXMLString(calNode.toxml())
            print calNode.toxml()
            print ""
            print document.toxml()
            if (calDic.id == calendar.getId()):
                
                document.removeChild(calNode)
                newCalElement = parseString(calendar.toXML())
                newCalElement.removeAttribute("xmlns:myscheduler")
                document.appendChild(newCalElement)
        
        xml.dom.ext.PrettyPrint(document, open(calendarsDataSet, "w"))

    def saveUser(self, user):
        """
        Saves the user on the users database
        @raise UserAlreadyExistsException: if the user already exists with the same email address 
        """
        if (not self.userExists(user)):
            userdoc = parseString(user.toXML())
            userNodeList = userdoc.getElementsByTagName("myscheduler:user")
                    

            userNode.removeAttribute("xmlns:myscheduler")
            self.add(userNode, "myscheduler:patients", usersFile)

    def getUserByLogin(self, username, password):
        """
        Returns an instance of User that matches the given username and password
        @param username: the username used to login. It's an alpha-character 
        @param password: the password matching the login provided
        @raise UserPasswordNotMatchException: if the given password doesn't match the user found
        @raise UserNotFoundException: if the given username could not be found on the system
        """
        users = self.getUsersDictionary()
        for existingUser in users:
            if (username == existingUser.username):
                if (password == existingUser.password):
                    return UsersFactory().buildUserFromDictionary(existingUser)
                else:
                    raise UserPasswordNotMatchException("Wrong password provided!", {'password' : password})
        raise UserNotFoundException("User not found with the provided username!", {'username' : username})

    def userExists(self, user):
        """
        Verifies if a given instance of User exists in the database by email
        """
        users = self.getUsersDictionary()
        for savedUser in users:
            if (user.getEmail() == savedUser.email):
                return True
        return False
    
    def saveCalendar(self, calendar): 

        et = eT.parse(open(calendarsDataSet))
        import string
        mainNS=string.Template("{http://cs.sfsu.edu/csc867/myscheduler}$tag")
        userTag = mainNS.substitute(tag="calendar")
        xPath = "//"+userTag
        for cal in et.findall(xPath):
            print cal.tostring()
            calDic = XMLToDic().getDictionaryFromXMLString(cal.toxml())
            if (calDic.calendar.id == calID):
                et.remove(cal)
                et.append()
        return None
                            #Document                    #NodeList                                  #Element
        caldocToSave = parseString(calendar.toXML()).getElementsByTagName("myscheduler:calendar").item(0)
        calDocumentToDelete = self.getCalendarDocument(calendar.getId())
        et.write(calendarsDataSet)

    def getCalendarDocument(self, calID):
        et = eT.parse(open(calendarsDataSet))
        import string
        mainNS=string.Template("{http://cs.sfsu.edu/csc867/myscheduler}$tag")
        userTag = mainNS.substitute(tag="calendar")
        xPath = "//"+userTag
        for cal in et.findall(xPath):
            calDic = XMLToDic().getDictionaryFromXMLElement(cal)
            if (calDic.calendar.id == calID):
                return cal
        return None
    
    def getUser(self, userID):
        et = eT.parse(open(usersDataSet))
        import string
        mainNS=string.Template("{http://cs.sfsu.edu/csc867/myscheduler}$tag")
        userTag = mainNS.substitute(tag="user")
        xPath = "//"+userTag
        for user in et.findall(xPath):
            userDic = XMLToDic().getDictionaryFromXMLElement(user)
            if (userDic.user.id == userID):
                return UsersFactory().buildUserFromDictionary(userDic.user)
        return None

    def getCalendar(self, calID):
        et = eT.parse(open(calendarsDataSet))
        import string
        mainNS=string.Template("{http://cs.sfsu.edu/csc867/myscheduler}$tag")
        userTag = mainNS.substitute(tag="calendar")
        xPath = "//"+userTag
        for cal in et.findall(xPath):
            calDic = XMLToDic().getDictionaryFromXMLElement(cal)
            if (calDic.calendar.id == calID):
                return CalendarFactory().buildCalendarFromDictionary(calDic.calendar)
        return None

    def getCalendarByOwner(self, ownerID):
        et = eT.parse(open(calendarsDataSet))
        import string
        mainNS=string.Template("{http://cs.sfsu.edu/csc867/myscheduler}$tag")
        userTag = mainNS.substitute(tag="calendar")
        xPath = "//"+userTag
        for cal in et.findall(xPath):
            calDic = XMLToDic().getDictionaryFromXMLElement(cal)
            if (calDic.calendar.ownerId == ownerID):
                return CalendarFactory().buildCalendarFromDictionary(calDic.calendar)
        return None

    def getUsersDictionary(self):
        """
        Returns the collection of existing users in the system as a dictionary
        """
        r = XMLToDic().getDictionaryFromXMLFile(usersDataSet)
        return r.users.user
    
    def getCalendarsDictionary(self):
        """
        Returns the collection of existing calendars in the system as a dictionary
        """
        r = XMLToDic().getDictionaryFromXMLFile(calendarsDataSet)
        return r.calendars.calendar