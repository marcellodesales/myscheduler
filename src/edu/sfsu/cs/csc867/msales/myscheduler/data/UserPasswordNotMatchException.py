from edu.sfsu.cs.csc867.msales.myscheduler.model.scheduler.MySchedulerException import MySchedulerException
from edu.sfsu.cs.csc867.msales.myscheduler.util.IdentifyableObject import IdentifiableObject

class UserPasswordNotMatchException(MySchedulerException):
    
    def __new__(cls, message, varsValueDic = {}):
        return super(UserPasswordNotMatchException, cls).__new__(cls, message, varsValueDic)

    def __init__(self, message, varsValueDic = {}):
        IdentifiableObject.__init__(self)
        self.message = message
        self.__varsValueDic = varsValueDic 

if __name__ == '__main__':
    print UserPasswordNotMatchException("message").getId()