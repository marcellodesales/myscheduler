from datetime import datetime
import time
from time import strptime

class IdentifiableObject(object):
    
    def __new__(cls):
        return super(IdentifiableObject, cls).__new__(cls)
    
    def __init__(self):
        now = long(time.time() * 1000)
        lasttime = now
        while lasttime == now: 
            time.sleep(.01)
            now = long(time.time() * 1000)
        self.__id = str(now)
        self.__creationDateTime = datetime.today()

    def getId(self):
        return self.__id
    
    def getCreationDateTime(self):
        return self.__creationDateTime
    
    def getHumanReadableCreationdateTime(self):
        return self.getCreationDateTime().strftime("Object created on %A, %B %d %Y at %H:%M")
    
if __name__ == '__main__':
    o = IdentifiableObject()
    print o.getId()
    print o.getCreationDateTime()
    print o.getHumanReadableDateTime()