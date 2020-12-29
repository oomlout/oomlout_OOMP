
details = list()
parts = list()




def oompAddDetail(category,code,name,sort="",extra1="",extra2=""):
    details.append(oompDetail(category,code,name,sort,extra1="",extra2=""))

def getDetailFromCode(category,code):
    for x in details:
        if x.category == category:
            if x.code == code:
                return x
    return oompDetail("","","","")

def getPartByID(part):
##    print("     Get Part By ID: " + part)
    for x in parts:
        if x.getTag("oompID").value == part:
            return x     
    return oompItem("")

def getDetailByCode(category, code):    
##    print("     Get Part By ID: " + code)
    for x in details:
        #print("    Matching: " + x.code + " with -- " + code)
        if x.code == code:
            return x     
    return oompDetail("","","","")


def printParts():
    print("OOMP Parts")
    for x in parts:
        print("    Part: " + str(x))

        

class oompItem:

    def __init__(self,index):
        self.tags=list()
        self.index=index
        self.addTag("index", index)

    def __str__(self):
        rv = ""
        rv = rv + self.getName()
        #for x in self.tags:
        #    rv = rv + "    " + str(x)
        return rv
    

    def addTag(self,name,value):
        self.tags.append(oompTag(name,value))

    def getTag(self,name):
        if name == "oompID":
            id = self.getTag("oompType").value + "-" +  self.getTag("oompSize").value + "-" +  self.getTag("oompColor").value + "-" +  self.getTag("oompDesc").value + "-" +  self.getTag("oompIndex").value
            return(oompTag("oompID", id))
        elif name == "hexID":
            hexValue = hex(self.getTag("index").value).replace("0x","").upper()
            return(oompTag("hexID",hexValue))
        elif name == "name":
            name = ""
            #size
            value = getDetailFromCode("size",self.getTag("oompSize").value).name
            if value != "":
                name = name + value + " "

            #desc
            value = getDetailFromCode("desc",self.getTag("oompDesc").value).name
            if value != "":
                name = name + value + " "
                
            #color
            value = getDetailFromCode("color",self.getTag("oompColor").value).name
            if value != "":
                name = name + value + " "
                
            #type
            value = getDetailFromCode("type",self.getTag("oompType").value).name
            if value != "":
                name = name + value + " "
                
            #index
            value = getDetailFromCode("index",self.getTag("oompIndex").value).name
            if value != "":
                name = name + value + " "                      

            name = name.strip()
            return(oompTag("name", name))
        else:
            for x in self.tags:
                if x.name == name:
                    return x
            return oompTag("XXXXX","XXXXX")

    def getName(self):
        return "OOMP Item:    " + self.getTag("oompID").value + " " + self.getTag("name").value

    
class oompTag:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "oompTag " + str(self.name) + " : " + str(self.value) + "\n"

    def getValue(self):
        return self.value

class oompDetail:

    def __init__(self, category, code, name, sort="", extra1="", extra2=""):
        self.category = category
        self.code = code
        self.name = name
        self.sort = sort
        self.extra1 = extra1
        self.extra2 = extra2
    
    
#### import detail lists

import OOMPdetailsType
import OOMPdetailsSize
import OOMPdetailsColor
import OOMPdetailsDesc
import OOMPdetailsIndex

#### import parts

import OOMPparts
        
