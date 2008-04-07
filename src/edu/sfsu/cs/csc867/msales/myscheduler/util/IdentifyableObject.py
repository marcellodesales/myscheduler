from datetime import datetime
import time
from time import strptime

class IdentifiableObject(object):
    
    def __new__(cls, id=-1):
        cls.__id = id
        return super(IdentifiableObject, cls).__new__(cls)
    
    def __init__(self, id=-1):
        if (id == -1):
            self.__creationDateTime = datetime.today()
        else:
            self.__creationDateTime = datetime.fromtimestamp(long(id) / 1000)

        if (id == -1):
            now = long(time.time() * 1000)
            lasttime = now
            while lasttime == now: 
                time.sleep(.01)
                now = long(time.time() * 1000)
            id = now
        self.__id = str(id)

    def getId(self):
        return self.__id
    
    def getCreationDateTime(self):
        return self.__creationDateTime
    
    def getHumanReadableCreationdateTime(self):
        return self.getCreationDateTime().strftime("Object created on %A, %B %d %Y at %H:%M")
    
if __name__ == '__main__':
    #o = IdentifiableObject()
    o = IdentifiableObject(1207535492344)
    print o.getId()
    print o.getCreationDateTime()
    print o.getHumanReadableCreationdateTime()