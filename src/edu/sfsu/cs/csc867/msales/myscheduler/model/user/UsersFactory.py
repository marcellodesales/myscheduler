from edu.sfsu.cs.csc867.msales.myscheduler.model.user.Patient import Patient
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.User import User
from edu.sfsu.cs.csc867.msales.myscheduler.util.Singleton import Singleton

from datetime import date

class UsersFactory(Singleton):
    
    def buildNewUser(self, firstName, lastName, email):
        return User(firstName, lastName, email)
    
    def buildNewPatient(self, firstName, lastName, email, birthday):
        return Patient(firstName, lastName, email, birthday)
    
if __name__ == '__main__':
    
    marcello = UsersFactory().buildNewPatient("Marcello", "de Sales", "msales@sfsu.edu", date(1979, 12, 15))
    marcello.printAll()
    marcelloClone = UsersFactory().buildNewPatient("Marcello", "de Sales", "msales@sfsu.edu", date(1979, 12, 15))
    
    marcello.printAll()
    marcelloClone.printAll()
    print marcello == marcelloClone
    
    print marcello.__hash__()
    print marcelloClone.__hash__()
    