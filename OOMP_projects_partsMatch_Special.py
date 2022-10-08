import OOMP
import OOMP_projects_partsMatch

def matchSpecial(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompID=""):  
    partDict = OOMP_projects_partsMatch.loadPartDict(part,project)   

    ######  Full text test
    list = []
    ###### ADXL345
    list.append(["ADXL345","SENS-LG14-X-K345-01"])
    list.append(["ADXL343","SENS-LG14-X-K345-01"])
    ###### QWIIC Connector
    list.append(["JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal","HEAD-JSTSH-X-PI04-RS"])
    list.append(["STEMMA_I2C","HEAD-JSTSH-X-PI04-RS"])
    list.append(["QWIIC","HEAD-JSTSH-X-PI04-RS"])


    for l in list:
        if l[0].upper() in partDict["FULL"].upper():
            oompID = l[1]


    return oompID