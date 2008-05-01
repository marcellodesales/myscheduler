from edu.sfsu.cs.csc867.msales.myscheduler.util.Singleton import Singleton
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.UsersFactory import UsersFactory
from edu.sfsu.cs.csc867.msales.myscheduler.data.XMLPersistence import XMLPersistence

class UserController(Singleton):

    def createNewUser(self, firstName, lastName, email, username, password):
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
        newUser = UsersFactory().buildNewUser(firstName, lastName, email, username, password)
        if (XMLPersistence().userExists(newUser)):
            raise UserAlreadyExistsException("User already exists with the given email!", {'email':user.getEmail()} )
        else:
            XMLPersistence().saveUser(newUser)
        return newUser
    
    def getUser(self, userId):
        return XMLPersistence().getUser(userId)
    
    def doLogin(self, username, password):
        """
        Returns an instance of User that matches the given username and password
        @param username: the username used to login. It's an alpha-character
        @param password: the password matching the login provided
        @raise UserPasswordNotMatchException: if the given password doesn't match the user found
        @raise UserNotFoundException: if the given username could not be found on the system
        """
        return XMLPersistence().getUserByLogin(username, password)

if __name__ == '__main__':
    
    marcello = UserController().getUser('1207535492344')
    marcello.printAll()

    
    
    #marcelloLogged = UserController().doLogin("msales", "utn29oad")
    #marcelloLogged.printAll()
