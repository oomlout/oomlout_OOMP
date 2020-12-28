
details = list()

def oompAddDetail(category,code,name,sort="",extra1="",extra2=""):
    details.append(oompDetail(category,code,name,sort,extra1="",extra2=""))

def getDetailFromCode(category,code):
    for x in details:
        if x.category == category:
            if x.code == code:
                return x
    return oompDetail("","","","","","")
    

class oompItem:

    def __init__(self,index):
        self.tags=list()
        self.index=index
        self.addTag("index", index)

    def __str__(self):
        rv = ""
        rv = rv + self.getName()
        for x in self.tags:
            rv = rv + "    " + str(x)
        return rv
    

    def addTag(self,name,value):
        self.tags.append(oompTag(name,value))

    def getTag(self,name):
        if name == "oompID":
            id = self.getTag("oompType").value + "-" +  self.getTag("oompSize").value + "-" +  self.getTag("oompColor").value + "-" +  self.getTag("oompDesc").value + "-" +  self.getTag("oompIndex").value
            return(oompTag("oompID", id))
        if name == "name":
            name = ""
            #size
            value = getDetailFromCode("size",self.getTag("oompSize").value).name
            name = name + value
            if value != "":
                name = name + " "

            #desc
            value = getDetailFromCode("desc",self.getTag("oompDesc").value).name
            name = name + value
            if value != "":
                name = name + " "

            #color
            value = getDetailFromCode("color",self.getTag("oompColor").value).name
            name = name + value
            if value != "":
                name = name + " "

            #type
            value = getDetailFromCode("type",self.getTag("oompType").value).name
            name = name + value
            if value != "":
                name = name + " "

            #index
            value = getDetailFromCode("index",self.getTag("oompIndex").value).name
            name = name + value
            
            return(oompTag("name", name))
        else:
            for x in self.tags:
                #print(x)
                if x.name == name:
                    return x
            return oompTag("XXXXX","XXXXX")

    def getName(self):
        print(self.getTag("name"))
        return "OOMP Item " + self.getTag("name").value + " " + self.getTag("oompID").value + "\n"

    
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
    
    
        
