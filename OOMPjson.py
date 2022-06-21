import OOMP
import os
import json

def generateJson(item,overwrite):
    oompID = item.getTag("oompID").value
    name = item.getTag("name").value
    item.addTag("oompID", oompID)
    item.addTag("name", name)
    jsonFile = item.getFolder() + "json.json"
    if not os.path.isfile(jsonFile) or overwrite:
        jsonText = json.dumps(item,default=lambda o: o.__dict__, sort_keys=True, indent=4)
        f = open(jsonFile,"w")
        f.write(jsonText)
        f.close()

    item.removeTag("oompID")    
    item.removeTag("name")    