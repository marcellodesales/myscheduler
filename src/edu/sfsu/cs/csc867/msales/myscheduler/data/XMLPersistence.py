from edu.sfsu.cs.csc867.msales.myscheduler.util.Singleton import Singleton
from edu.sfsu.cs.csc867.msales.myscheduler.util.XMLToDic import XMLToDic
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.UsersFactory import UsersFactory
from edu.sfsu.cs.csc867.msales.myscheduler.data.UserAlreadyExistsException import UserAlreadyExistsException 
from edu.sfsu.cs.csc867.msales.myscheduler.data.UserPasswordNotMatchException import UserPasswordNotMatchException
from edu.sfsu.cs.csc867.msales.myscheduler.data.UserNotFoundException import UserNotFoundException
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.UsersFactory import UsersFactory


from xml.dom.minidom import parseString, parse
import xml.dom.ext

global usersFile 
usersFile = "/home/marcello/development/workspace-sfsu/MyScheduler/data/Patients.xml"

class XMLPersistence(Singleton):
    
    def save(self, xmlElement, parentElementName, filePath):
        """
        Save the xmlElement as a child of the given parentElementName from the given filePath
        """
        document = parse(filePath)

        rootCollection = document.getElementsByTagName(parentElementName)
        rootElement = rootCollection.item(0)
        rootElement.appendChild(xmlElement)

        xml.dom.ext.PrettyPrint(document, open(filePath, "w"))

    def saveUser(self, user):
        """
        Saves the user on the users database
        @raise UserAlreadyExistsException: if the user already exists with the same email address 
        """
        if (not self.userExists(user)):
            userdoc = parseString(user.toXML())
            userNodeList = userdoc.getElementsByTagName("myscheduler:user")
            userNode = userNodeList.item(0)
            userNode.removeAttribute("xmlns:myscheduler")
            
            self.save(userNode, "myscheduler:patients", usersFile)
        else:
            raise UserAlreadyExistsException("User already exists with the given email!", {'email':user.getEmail()} )

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

    def getUsersDictionary(self):
        """
        Returns the collection of existing users in the system as a dictionary
        """
        r = XMLToDic().getDictionaryFromXMLFile(usersFile)
        return r.patients.user