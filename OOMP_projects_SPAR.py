import OOMP
import OOMP_projects_BASE

def createProjects():
    projects = []

    count = 1
    base = {}
    base["oompType"] = "PROJ"
    base["oompSize"] = "SPAR"
    base["format"] = "eagle"
    
    base["github"] = "https://github.com/sparkfun/"

    projects = []

    d = base.copy()
    d["name"] = "Qwiic EEPROM - 512Kbit"
    d["repo"] = "Qwiic_EEPROM_Breakout"
    d["file"] = "Qwiic AHT20 Breakout"
    d["count"] = 18355    
    projects.append(d.copy())



    ###### SparkFun X Projects
    base["github"] = "https://github.com/sparkfunX/"
    d = base.copy()
    d["name"] = "SparkFun Qwiic Humidity AHT20"
    d["repo"] = "Qwiic_Humidity_AHT20"
    d["file"] = "Hardware/Qwiic EEPROM"
    d["count"] = 16618    
    projects.append(d.copy())

    d = base.copy()
    d["name"] = "Qwiic BMP388 Pressure Sensor"
    d["repo"] = d["name"].replace(" ","_")
    d["file"] = "Hardware/" + d["repo"]
    d["count"] = 17001    
    projects.append(d.copy())


    for d in projects:
        OOMP_projects_BASE.makeProjectNew(d)

    count = count +1

