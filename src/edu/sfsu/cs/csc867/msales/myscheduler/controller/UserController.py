from edu.sfsu.cs.csc867.msales.myscheduler.util.Singleton import Singleton
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.UsersFactory import UsersFactory
from edu.sfsu.cs.csc867.msales.myscheduler.data.XMLPersistence import XMLPersistence

class UserController(Singleton):

    def createNewUser(self, firstName, lastName, email, username, password):
        newUser = UsersFactory().buildNewUser(firstName, lastName, email, username, password)
        XMLPersistence().saveUser(newUser)
        return newUser
    
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
    
    marcelloCon = UserController().createNewUser("Marcello", "de Sales", "marcello.sales@gmail.com", "marcellosales", "utn29oad")
    marcelloCon.printAll()
    
    #marcelloLogged = UserController().doLogin("msales", "utn29oad")
    #marcelloLogged.printAll()
