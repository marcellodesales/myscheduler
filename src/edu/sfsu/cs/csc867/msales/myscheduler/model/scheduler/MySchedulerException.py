from edu.sfsu.cs.csc867.msales.myscheduler.util.IdentifyableObject import IdentifiableObject

class MySchedulerException(Exception, IdentifiableObject):
    
    def __new__(cls, message, varsValueDic = {}):
        return super(MySchedulerException, cls).__new__(cls)

    def __init__(self, message, varsValueDic = {}):
        IdentifiableObject.__init__(self)
        self.message = message
        self.__varsValueDic = varsValueDic 
        
    def __str__(self):
        return self.__class__.__name__ + " (" + self.getHumanReadableCreationdateTime() + ")" + ": " + self.message

    def getAttributeValesDictionary(self):
        return self.__varsValueDic

if __name__ == '__main__':
    print MySchedulerException("It's wrong here!!!").getId()
    print MySchedulerException("It'sdsd wrong here!!!").getId()
    print MySchedulerException("It's wrsdsdong here!!!").getId()