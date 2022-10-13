import OOMP_modules_BASE

def createModules():
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "POWE"
    d["oompColor"] = "V12R";    d["oompDesc"] = "V33D"
    d["oompIndex"] = "01";    d["hexID"] = "BP123"
    d["name"] = "Power Block About 12 v In, 3.3 v Out"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "SENS"
    d["oompColor"] = "ACCEL";    d["oompDesc"] = "I2C"
    d["oompIndex"] = "01";    d["hexID"] = "BSAI"
    d["name"] = "Sensor Block (Accelerometer) I2C"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)    
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "BCI"
    d["name"] = "Connector Block (I2C)"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "BLOCK";    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C";    d["oompDesc"] = "EXTRA"
    d["oompIndex"] = "01";    d["hexID"] = "BCIE"
    d["name"] = "Connector Block (I2C) Plus Extra Pins"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "POWE"
    d["oompColor"] = "KAP2112K";    d["oompDesc"] = "V33D"
    d["oompIndex"] = "01";    d["hexID"] = "MP21123"
    d["name"] = "Sensor Module ADXL345"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-SENS-ACCEL-I2C-01"])
    d["extraTags"].append(["oompParts","U1,SENS-LG14-X-K345-01"])    
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "SENS"
    d["oompColor"] = "K345";    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01";    d["hexID"] = "MS345"
    d["name"] = "Sensor Module ADXL345"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-SENS-ACCEL-I2C-01"])
    d["extraTags"].append(["oompParts","U1,SENS-LG14-X-K345-01"])    
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "BRBO";    d["oompDesc"] = "IBBC"
    d["oompIndex"] = "SZ01";    d["hexID"] = "MCBI1"
    d["name"] = "Connector Module Breakout Board IBBZ Size 01"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-I2C-EXTRA-01"])
    d["extraTags"].append(["oompParts","J1,HEAD-I01-X-PI06-01"])    
    d["extraTags"].append(["oompParts","J2,HEAD-I01-X-PI06-01"])    
    d["extraTags"].append(["componentModules","M1,MODULE-CONN-I2C-QWIIC-01"]) 
    d["extraTags"].append(["componentModules","M2,MODULE-CONN-I2C-QWIIC-01"]) 
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C";    d["oompDesc"] = "QWIIC"
    d["oompIndex"] = "01";    d["hexID"] = "MCQ"
    d["name"] = "Connector Module I2C QWIIC"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-I2C-STAN-01"])
    d["extraTags"].append(["oompParts","J1,HEAD-JSTSH-X-PI04-RS"])    
    OOMP_modules_BASE.makeModule(d)
    ###### MCUU
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "MCUU"
    d["oompColor"] = "K328";    d["oompDesc"] = "MUR"
    d["oompIndex"] = "01";    d["hexID"] = "MM328M"
    d["name"] = "MCU Module ATMega 328 (MUR)"    
    d["extraTags"] = []
    ###### DADB
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "DADB"
    d["oompColor"] = "MCUU";    d["oompDesc"] = "K328"
    d["oompIndex"] = "01";    d["hexID"] = "MD328M"
    d["name"] = "DADB Module ATMega 328 (MUR)"    
    d["extraTags"] = []
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "DADB"
    d["oompColor"] = "CONN";    d["oompDesc"] = "HEADI01PI15"
    d["oompIndex"] = "01";    d["hexID"] = "MDCI15"
    d["name"] = "DADB Module Connector 2.54mm 15 Pin"    
    d["extraTags"] = []
    OOMP_modules_BASE.makeModule(d)
    d = {}
    d["oompType"] = "MODULE";    d["oompSize"] = "CONN"
    d["oompColor"] = "DADB";    d["oompDesc"] = ""
    d["oompIndex"] = "01";    d["hexID"] = ""
    d["name"] = ""    
    d["extraTags"] = []
    d["extraTags"].append(["componentModules","M1,MODULE-MCUU-K328-MUR-01"]) 
    d["extraTags"].append(["componentModules","M1,MODULE-CONN-DADB-PI03-01"]) 
    d["extraTags"].append(["componentModules","M2,MODULE-CONN-DADB-PI16-01"]) 
    d["extraTags"].append(["componentModules","M3,MODULE-CONN-DADB-PI16-01"]) 
    for x in range(2,21+1):
        dd = d.copy()
        dd["oompDesc"] = "PI" + str(x).zfill(2)
        dd["hexID"] = "MCD" + str(x)
        d["name"] = "Connector Module DADB " + str(x) + " Pins"
        OOMP_modules_BASE.makeModule(dd)
