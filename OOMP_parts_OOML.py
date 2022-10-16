import OOMP

import OOMP_parts_BASE

def createParts():
    ##############################
    ######  HEAD
    type = "HEAD";size = "I01";color = "X";desc = "PI2X10";index = "SHRO";hexID = "H2X10SH"

    for x in range(1,10+1):
        desc = "PI2X" + str(x).zfill(2)
        hexID = "H2X" + str(x) + "SH"
        OOMP_parts_BASE.makePart(type,size,color,desc,index, hexID)

    type = "HEAD";size = "I01";color = "X";desc = "";index = "RS";hexID = ""
    datasheet = "sourceDatasheets/HEAD-I01-X-PI2X03-RS.pdf"

    for x in range(2,10+1):
        extraTags = []
        desc = "PI2X" + str(x).zfill(2)
        hexID = "H2X" + str(x) + "RS"
        d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
        OOMP_parts_BASE.makePart(dict = d)


    type = "HEAD";size = "JSTXH";color = "X";desc = "PI01";index = "01";hexID = "JX"

    for x in range(1,20+1):
        desc = "PI" + str(x).zfill(2)
        hexID = "HXH" + str(x)
        OOMP_parts_BASE.makePart(type,size,color,desc,index,hexID)

    type = "HEAD";size = "JSTSH";color = "X";desc = "PI01";index = "SM";hexID = "T35L1"

    for x in range(1,20+1):
        desc = "PI" + str(x).zfill(2)
        hexID = "HSH" + str(x)
        OOMP_parts_BASE.makePart(type,size,color,desc,index,hexID)

    type = "HEAD";size = "JSTSH";color = "X";desc = "PI01";index = "RS";hexID = "T35L1"
    for x in range(1,20+1):
        desc = "PI" + str(x).zfill(2)
        hexID = "HSHR" + str(x)    
        OOMP_parts_BASE.makePart(type,size,color,desc,index,hexID)



    ##############################
    ######  REFU
    parts=[]
    type = "REFU";size = "1812";color = "X"
    parts.append(["A35D","V6"])
    parts.append(["A3","V6"])
    parts.append(["A26D","V8"])
    parts.append(["A2","V8"])
    parts.append(["A16D","V8"])
    parts.append(["A11D","V8"])
    parts.append(["A15D","V6"])
    parts.append(["A35D","V6"])
    parts.append(["A075D","V132D"])
    parts.append(["A5D","V15"])
    parts.append(["A2D","V30"])
    parts.append(["A1D","V60"])
    for part in parts:
        desc = part[0]
        index = part[1]
        hexID = "RF18" + desc.replace("A","")
        OOMP_parts_BASE.makePart(type,size,color,desc,index,hexID)

    ##############################
    ######  RESA
    resistorSmall = ["O102","O103","O220","O222","O472"]

    resaPackages = ["06038","12068"]

    type = "RESA";size = "";color = "X";desc = "";index = "01";hexID = ""
    for size in resaPackages:
        for desc in resistorSmall:
            hexID = "RA" + size.replace("06038","6").replace("12068","12") + desc.replace("O","")
            desc = desc + "X4"            
            OOMP_parts_BASE.makePart(type,size,color,desc,index,hexID)
    

    ##############################
    ######  SENS
    ###### ADXL345
    type = "SENS";size = "LG14";color = "X";desc = "K345";index = "01";hexID = "SEN345"
    OOMP_parts_BASE.makePart(type,size,color,desc,index,hexID)

    ##############################
    ######  TERS
    type = "TERS";size = "35D";color = "L";desc = "PI01";index = "01";hexID = "T35L1"

    for x in range(1,15+1):
        desc = "PI" + str(x).zfill(2)
        hexID = "T35L" + str(x)
        OOMP_parts_BASE.makePart(type,size,color,desc,index,hexID)

    ##############################
    ######  USB
    ######  C31
    type = "USBS";size = "TC";color = "X";desc = "K31";index = "01";hexID = "USCK31"
    extraTags = []
    data = {"companyName" : "LCSC", "companyCode" : "C-LCSC", "partNumber" : "C165948"}
    extraTags.append(OOMP.oompTag("distributorPartNumber",data))
    data = {"companyName" : "Korean Hroparts Elec", "companyCode" : "C-KHRO", "partNumber" : "TYPE-C-31-M-12"}
    extraTags.append(OOMP.oompTag("manufacturerPartNumber",data))
    OOMP_parts_BASE.makePart(type,size,color,desc,index,hexID,extraTags=extraTags)

    ##############################
    ######  VREG
    ######  LD1117
    type = "VREG";size = "";color = "X";desc = "KLD1117";index = "01";hexID = "VR1117"

    list = ["SO223","SO8","DPAK","T220"]
    list2 = ["V12D","V18D","V25D","V33D","V5"]
    for l in list:
        size = l
        for ll in list2:
            index = ll
            hexID = "VR1117" + l.replace("SO","").replace("T","").replace("T","").replace("DPAK","D") + ll.replace("D","").replace("V","")
            OOMP_parts_BASE.makePart(type,size,color,desc,index,hexID)