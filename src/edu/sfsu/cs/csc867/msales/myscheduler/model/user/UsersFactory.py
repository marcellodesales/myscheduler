from edu.sfsu.cs.csc867.msales.myscheduler.model.user.Patient import Patient
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.User import User
from edu.sfsu.cs.csc867.msales.myscheduler.util.Singleton import Singleton
from edu.sfsu.cs.csc867.msales.myscheduler.util.ObjectDictionary import ObjectDictionary

from datetime import date

class UsersFactory(Singleton):
    
    def buildNewUser(self, firstName, lastName, email, username, password, id=-1):
        return User(firstName, lastName, email, username, password, id)
    
    def buildNewPatient(self, firstName, lastName, email, birthday, id=-1):
        return Patient(firstName, lastName, email, birthday, id)
    
    def buildUserFromDictionary(self, userDic):
        return User(userDic.firstName, userDic.lastName, userDic.email, userDic.username, userDic.password, userDic.id)
    
if __name__ == '__main__':
    
    marcello = UsersFactory().buildNewUser("Marcello", "de Sales", "msales@sfsu.edu", "msales", "1234", 1207548712633)
    marcello.printAll()
    #marcelloClone = UsersFactory().buildNewUser("Marcello", "de Sales", "msales@sfsu.edu", "msales", "1234")
    
    print marcello.toXML()
    
#    marcello.printAll()
#    marcelloClone.printAll()
    #print marcello == marcelloClone
    
    print marcello.__hash__()
    #print marcelloClone.__hash__()
    