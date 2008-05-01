from edu.sfsu.cs.csc867.msales.myscheduler.util.Singleton import Singleton
from edu.sfsu.cs.csc867.msales.myscheduler.model.user.UsersFactory import UsersFactory
from edu.sfsu.cs.csc867.msales.myscheduler.util.ObjectDictionary import ObjectDictionary

import xml.etree.ElementTree as ET
import string

def __getTagWithoutNamespace(tagString):
    return tagString.split("}")[1] if string.find(tagString, "}") != -1 else tagString

def __parse_node(node):
    
    tmp = ObjectDictionary()
    # save attrs and text, hope there will not be a child with same name
    if node.text:
        tmp['value'] = node.text
    for (k,v) in node.attrib.items():
        tmp[k] = v

    for ch in node.getchildren():
        cht = __getTagWithoutNamespace(ch.tag)
        chp = __parse_node(ch)

        if cht not in tmp: # the first time, so store it in dict
            tmp[cht] = chp
            continue

        old = tmp[cht]
        if not isinstance(old, list):
            tmp.pop(cht)   
            tmp[cht] = [old] # multi times, so change old dict to a list       
        tmp[cht].append(chp) # add the new one      

    return  tmp

def xmlStringToDictionary(s):
    """parse a string"""
    t = ET.fromstring(s)
    return ObjectDictionary({__getTagWithoutNamespace(t.tag) : __parse_node(t)})

def xmlFileToDictionary(file):
    """parse a xml file to a dict"""
    f = open(file, 'r')
    t = ET.parse(f).getroot()
    return ObjectDictionary({__getTagWithoutNamespace(t.tag) : __parse_node(t)})

def xmlElementToDictionary(xmlElement):
    return ObjectDictionary({__getTagWithoutNamespace(xmlElement.tag) : __parse_node(xmlElement)})

class XMLToDic(Singleton):
    
    def getDictionaryFromXMLFile(self, file):
        return xmlFileToDictionary(file)

    def getDictionaryFromXMLString(self, string):
        return xmlStringToDictionary(string)
    
    def getDictionaryFromXMLElement(self, xmlElement):
        return xmlElementToDictionary(xmlElement)
    
if __name__ == '__main__':

    usersFile = "/home/marcello/development/workspace-sfsu/MyScheduler/data/Patients.xml"

    marcello = UsersFactory().buildNewUser("Marcello", "de Sales", "msales@sfsu.edu", "msales", "1234")
    marcDic = XMLToDic().getDictionaryFromXMLString(marcello.toXML())
    print marcDic
    patients = XMLToDic().getDictionaryFromXMLFile(usersFile)
    print patients
