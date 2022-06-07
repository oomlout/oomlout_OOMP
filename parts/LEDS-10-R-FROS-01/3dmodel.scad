// Generated by SolidPython 1.1.3 on 2022-06-07 10:36:54
$fn = 48;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [1.2700000000, 0, 0.1000000000]) {
							rotate(a = [0, 0, 0]) {
								color(alpha = 1.0000000000, c = "gray") {
									translate(v = [0, 0, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, -2.0500000000]) {
												cube(center = true, size = [0.6000000000, 0.6000000000, 4.1000000000]);
											}
										}
									}
								}
							}
						}
						translate(v = [-1.2700000000, 0, 0.1000000000]) {
							rotate(a = [0, 0, 0]) {
								color(alpha = 1.0000000000, c = "gray") {
									translate(v = [0, 0, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, -3.0500000000]) {
												cube(center = true, size = [0.6000000000, 0.6000000000, 6.1000000000]);
											}
										}
									}
								}
							}
						}
						translate(v = [0, 0, 8.5000000000]) {
							rotate(a = [0, 0, 0]) {
								color(alpha = 1.0000000000, c = "red") {
									translate(v = [0, 0, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, -3.2500000000]) {
												cylinder(center = true, h = 6.5000000000, r = 5);
											}
										}
									}
								}
							}
						}
						translate(v = [0, 0, 2.0500000000]) {
							rotate(a = [0, 0, 0]) {
								color(alpha = 1.0000000000, c = "red") {
									translate(v = [0, 0, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, -1.0000000000]) {
												cylinder(center = true, h = 2, r = 5.5000000000);
											}
										}
									}
								}
							}
						}
						translate(v = [0, 0, 13.5000000000]) {
							rotate(a = [0, 0, 0]) {
								color(alpha = 1.0000000000, c = "red") {
									translate(v = [0, 0, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, -5]) {
												sphere(r = 5);
											}
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
	}
	union();
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
import subprocess

from solid.objects import *
from solid import scad_render_to_file, scad_render

##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
######  DIMENSION STUFF
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################


mode = "3DPR"
#mode = "LAZE"
#mode = "TURE"
#mode = ""


######  Countersunk
countersunkM = []
WIDTH = 0
DEPTH = 1
countersunkM1width = 0; countersunkM1depth = 0; countersunkM2width = 0; countersunkM2depth = 0
countersunkM3width = 0
countersunkM3depth = 0
countersunkM4width = 0
countersunkM4depth = 0
countersunkM5width = 0
countersunkM5depth = 0
countersunkM6width = 0
countersunkM6depth = 0

######  Holes
holeM = []
holeM1 = 0
holeM2 = 0
holeM3 = 0
holeM4 = 0
holeM5 = 0
holeM6 = 0

######  Nuts
nutM = []
NUTWIDTH = 0
NUTDEPTH = 1
nutM1width = 0
nutM1depth = 0
nutM2width = 0
nutM2depth = 0
nutM3width = 0
nutM3depth = 0
nutM4width = 0
nutM4depth = 0
nutM5width = 0
nutM5depth = 0
nutM6width = 0
nutM6depth = 0

######  OOEB
ooebPinWidth = 0
ooebPinWidthWide = 0


######  Colors
colDefault = "Gold"

colOOEBbase = colDefault

colLEDRed = "red"
colWire = "gray"
    ######  Resistor
colRes = list()
colResistor = "beige"

colResBlack = "black"
colRes.append(colResBlack)
colResBrown = "brown"
colRes.append(colResBrown)
colResRed = "red"
colRes.append(colResRed)
colResOrange = "orange"
colRes.append(colResOrange)
colResYellow = "yellow"
colRes.append(colResYellow)
colResGreen = "green"
colRes.append(colResGreen)
colResBlue = "blue"
colRes.append(colResBlue)
colResPurple = "purple"
colRes.append(colResPurple)
colResGray = "gray"
colRes.append(colResGray)
colResWhite = "white"
colRes.append(colResWhite)





def changeMode(m="3DPR"):
    #print("####################################################      CHANGING MODES TO: " + m)
    global mode
    mode = m
    ######  Countersunk
    global countersunkM, countersunkM1width, countersunkM1depth, countersunkM2width, countersunkM2depth, countersunkM3width, countersunkM3depth, countersunkM4width, countersunkM4depth, countersunkM5width, countersunkM5depth, countersunkM6width, countersunkM6depth
    countersunkM = []
    countersunkM.append([0,0])
    countersunkM1width = 0 if mode== "3DPR" else 0
    countersunkM1depth = 0 if mode== "3DPR" else 0
    countersunkM.append([countersunkM1width,countersunkM1depth])
    countersunkM2width = 0 if mode== "3DPR" else 0
    countersunkM2depth = 0 if mode== "3DPR" else 0
    countersunkM.append([countersunkM2width,countersunkM2depth])
    countersunkM3width = 5.5/2+0.6 if mode== "3DPR" else 5.5/2
    countersunkM3depth = 1.7 if mode== "3DPR" else 1.7
    countersunkM.append([countersunkM3width,countersunkM3depth])
    countersunkM4width = 0 if mode== "3DPR" else 0
    countersunkM4depth = 0 if mode== "3DPR" else 0
    countersunkM.append([countersunkM4width,countersunkM4depth])
    countersunkM5width = 0 if mode== "3DPR" else 0
    countersunkM5depth = 0 if mode== "3DPR" else 0
    countersunkM.append([countersunkM5width,countersunkM5depth])
    countersunkM6width = 0 if mode== "3DPR" else 0
    countersunkM6depth = 0 if mode== "3DPR" else 0
    countersunkM.append([countersunkM6width,countersunkM6depth])
    ######  Holes
    global holeM, holeM1, holeM2, holeM3, holeM4, holeM5, holeM6, holeM7, holeM8
    holeM = []
    holeM1 = 1.2/2 if mode== "3DPR" else 1/2
    holeM2 = 2.3/2 if mode== "3DPR" else 2/2
    holeM3 = 3.4/2 if mode== "3DPR" else 3/2
    holeM4 = 4.4/2 if mode== "3DPR" else 4/2
    holeM5 = 5.4/2 if mode== "3DPR" else 5/2
    holeM6 = 6.5/2 if mode== "3DPR" else 6/2
    holeM7 = 7.5/2 if mode== "3DPR" else 7/2
    holeM8 = 8.6/2 if mode== "3DPR" else 8/2
    holeM.append(0)
    holeM.append(holeM1)
    holeM.append(holeM2)
    holeM.append(holeM3)
    holeM.append(holeM4)
    holeM.append(holeM5)
    holeM.append(holeM6)
    holeM.append(holeM7)
    holeM.append(holeM8)
    #####  Nuts
    global nutM, nutM1width, nutM1depth, nutM2width, nutM2depth, nutM3width, nutM3depth, nutM4width, nutM4depth, nutM5width, nutM5depth, nutM6width, nutM6depth
    nutM = []
    nutM.append([0,0]) 
    #M1 Nut
    nutM1width = 0
    nutM1depth = 0
    nutM.append([nutM1width,nutM1depth])    
    #M2 Nut
    nutM2width = 0
    nutM2depth = 0
    nutM.append([nutM2width,nutM2depth])    
    #M3 Nut
    nutM3width = 6.05 if mode== "3DPR" else 5.5
    nutM3depth = 2.5 if mode== "3DPR" else 2.5
    nutM.append([nutM3width,nutM3depth])    
    #M4 Nut
    nutM4width = 0
    nutM4depth = 0
    nutM.append([nutM4width,nutM4depth])    
    #M5 Nut
    nutM5width = 0
    nutM5depth = 0
    nutM.append([nutM5width,nutM5depth])    
    #M6 Nut
    nutM6width = 11 if mode== "3DPR" else 10
    nutM6depth = 5 if mode== "3DPR" else 5
    nutM.append([nutM6width,nutM6depth])    

    ######  OOEB
    global ooebPinWidth,  ooebPinWidthWide

    ooebPinWidth = 0.6
    if(mode=="3DPR" or mode=="LAZE"):
        ooebPinWidth = 0.6 + 0.6
    ooebPinWidthWide = 1.2
    if(mode=="3DPR" or mode=="LAZE"):
        ooebPinWidthWide = 1.2 + 0.6


changeMode()


""""    
holeM12D = s=="3DPR" ? 1.4/2 : 1.2/2;
holeM16D = s=="3DPR" ? 1.8/2 : 1.6/2;
holeM2 = s=="3DPR" ? 2.3/2 : 2/2;
holeM25D = s=="3DPR" ? 2.8/2 : 2.5/2;
holeM27D = s=="3DPR" ? 3.1/2 : 2.7/2;    
holeM3 = s=="3DPR" ? 3.4/2 : 3/2;
holeM35D = s=="3DPR" ? 3.9/2 : 35/2;
holeM4 = s=="3DPR" ? 4.4/2 : 4/2;
holeM5 = s=="3DPR" ? 5.4/2 : 5/2;
holeM6 = s=="3DPR" ? 6.5/2 : 6/2;
holeM6Minus = s=="3DPR" ? 5.8/2 : 5.9/2;
holeM7 = s=="3DPR" ? 7.5/2 : 7/2;
holeM8 = s=="3DPR" ? 8.6/2 : 8/2;
holeM9 = s=="3DPR" ? 9.6/2 : 9/2;
holeM10 = s=="3DPR" ? 10.6/2 : 10/2;
holeM11 = s=="3DPR" ? 11.6/2 : 11/2;
holeM12 = s=="3DPR" ? 12.6/2 : 12/2;
holeM13 = s=="3DPR" ? 13.6/2 : 13/2;
holeM14 = s=="3DPR" ? 14.6/2 : 14/2;
holeM15 = s=="3DPR" ? 15.6/2 : 15/2;
holeM16 = s=="3DPR" ? 16.6/2 : 16/2;
holeM17 = s=="3DPR" ? 17.6/2 : 17/2;
holeM18 = s=="3DPR" ? 18.6/2 : 18/2;
holeM19 = s=="3DPR" ? 19.6/2 : 19/2;
holeM20 = s=="3DPR" ? 20.6/2 : 20/2;
"""

##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
######  REGULAR STUFF
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################


def setMode(mode="3DPR"):
    changeMode(mode)

def getMode():
    return mode



def saveToScad(fileName, parts):
    file_out = scad_render_to_file(parts, fileName, file_header=f'$fn = 48;')


def saveToDxf(fileIn, fileOut=""):
    if fileOut == "":
        fileOut = fileIn.replace(".scad",".dxf")
    saveToFile(fileIn, fileOut)
    
def saveToPng(fileIn, fileOut="",extra="--render"):
    if fileOut == "":
        fileOut = fileIn.replace(".scad",".png")
    saveToFile(fileIn, fileOut)

def saveToStl(fileIn, fileOut=""):
    if fileOut == "":
        fileOut = fileIn.replace(".scad",".stl")
    saveToFile(fileIn, fileOut)

def saveToFile(fileIn, fileOut,extra=""):
    extra = extra + " --colorscheme Tomorrow"

    launchStr = 'openscad -o "' + fileOut + '"' + extra + ' "' + fileIn + '"'
    print("            saveToFile launch string: " + launchStr)
    subprocess.run(launchStr)
    x=0



def insert(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
    return OPSCInsert(item,pos,x,y,z,ex,size,length,rot,rotX,rotY,rotZ,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)


def OPSCInsert(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,col=colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
    
    """
        color(color,alpha){
            translate([x,y,z]){
                    rotate([rotX,rotY,rotZ]){
    """
    returnValue = ""

    #print(pos)

    if pos[0] != None:
        x=pos[0]
        y=pos[1]
        z=pos[2]
    if rot[0] != None:
        rotX=rot[0]
        rotY=rot[1]
        rotZ=rot[2]
    
    returnValue = color(col)(translate((x,y,z))(
                            rotate((rotX,rotY,rotZ))(
                                OPSCInsertIf(item,pos,x,y,z,ex,size,length,rot,rotX,rotY,rotZ,width,height,depth,rad,rad2,col,alpha,OOwidth,OOheight,holes,negative,name)
                            )
                        ))
                
    

    return returnValue

def OPSCInsertIf(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
    returnValue = cube([10,10,10])

    if size[0] != None:
        width=size[0]
        height=size[1]
        depth=size[2]

    #print("    OPSCInsert item:" + str(item) + " at:[" + str(x) + "," + str(y) + "," + str(z) + "] size: [" + str(width) + "," + str(height) + "," + str(depth) + "]")

    if(item=="cube"):
        returnValue =  translate([0,0,-depth/2])(cube([width,height,depth],center=True))
    elif(item=="cylinder"):        
        returnValue = translate([0,0,-depth/2])(cylinder(r=rad,h=depth,center=True))
    elif(item=="sphere"):        
        returnValue = translate([0,0,-rad])(sphere(r=rad))
    elif(item=="plane"):
        returnValue = insert("cube",size=[1000,1000,0.1],color=color)            
    elif(item=="cubeRounded"):
        if(rad == 0):
                            rad = 5
        returnValue =  translate([0,0,-depth])(
                        linear_extrude(height=depth)(                        
                            offset(r=rad)(
                                square((width-rad*2+.01,height-rad*2+.01),center=True)
                                )
                            )
        )
    ######  Countersunk
    elif(item == "countersunkM1" or item == "csM1" ):
        returnValue = OSPCgetCountersunk(rad=1)
    elif(item == "countersunkM2" or item == "csM2" ):
        returnValue = OSPCgetCountersunk(rad=2)
    elif(item == "countersunkM3" or item == "csM3" ):
        returnValue = OSPCgetCountersunk(rad=3)
    elif(item == "countersunkM4" or item == "csM4" ):
        returnValue = OSPCgetCountersunk(rad=4)
    elif(item == "countersunkM5" or item == "csM5" ):
        returnValue = OSPCgetCountersunk(rad=5)
    elif(item == "countersunkM6" or item == "csM6" ):
        returnValue = OSPCgetCountersunk(rad=6)
    elif(item == "countersunk" or item == "cs"):
        returnValue = OSPCgetCountersunk(rad=rad)


    ######  Holes    
    elif(item == "holeM1"):
        returnValue = OSPCgetHole(rad=1)
    elif(item == "holeM2"):
        returnValue = OSPCgetHole(rad=2)
    elif(item == "holeM3"):
        returnValue = OSPCgetHole(rad=3)
    elif(item == "holeM4"):
        returnValue = OSPCgetHole(rad=4)
    elif(item == "holeM5"):
        returnValue = OSPCgetHole(rad=5)
    elif(item == "holeM6"):
        returnValue = OSPCgetHole(rad=6)
    elif(item == "hole"):
        returnValue = OSPCgetHole(rad=rad)

    ######  Nuts
    elif(item == "nutM1"):
        returnValue = OSPCgetNut(rad=1,depth=depth)
    elif(item == "nutM2"):
        returnValue = OSPCgetNut(rad=2,depth=depth)
    elif(item == "nutM3"):
        returnValue = OSPCgetNut(rad=3,depth=depth)
    elif(item == "nutM4"):
        returnValue = OSPCgetNut(rad=4,depth=depth)
    elif(item == "nutM5"):
        returnValue = OSPCgetNut(rad=5,depth=depth)
    elif(item == "nutM6"):
        returnValue = OSPCgetNut(rad=6,depth=depth)
    elif(item == "nut"):
        returnValue = OSPCgetNut(rad=rad,depth=depth)
    return returnValue

                

def OSPCgetHole(rad):
    return translate([0,0,-250])(cylinder(r=holeM[rad],h=500))

def OSPCgetNut(rad,depth):
    depth = nutM[rad][NUTDEPTH] if depth==100 else depth
    returnValue = OPSChexagon(nutM[rad][NUTWIDTH],depth=depth)
    return returnValue

def OSPCgetCountersunk(rad):
    depth=countersunkM[rad][DEPTH]
    returnValue = translate([0,0,-depth])(cylinder(h=depth,r2=countersunkM[rad][WIDTH],r1=holeM[rad]))
    return returnValue

def OPSChexagon(width,depth):
    cutter = item()
    wid=width*2
    cutter.addPos(insert("cube",pos=[wid/2+width/2,0,0],size=[wid,wid,depth]))
    cutter.addPos(insert("cube",pos=[-wid/2-width/2,0,0],size=[wid,wid,depth]))

    cut = cutter.getPart()
    #print(depth)
    returnValue = difference()(
        translate([0,0,-depth/2])(cube([wid,wid,depth],center=True)),
        cut,
        rotate([0,0,60])(cut),
        rotate([0,0,-60])(cut)
    )

    return returnValue




class item:

    def __init__(self):
        self.posItems=list()
        self.negItems=list()

    def isEmpty(self):        
        testString = scad_render(self.getPart())
        #print("test String length: " + str(len(testString)))
        returnValue = False
        if len(testString) == 270:            
            returnValue = True
        return returnValue

    def addPos(self,part):
        self.posItems.append(part)
    def addNeg(self,part):
        self.negItems.append(part)

    def getPart(self):
        returnValue = difference()(
            union()(self.posItems),
            union()(self.negItems)
        )
        return returnValue

    def getLaser(self,start=0,layers=1,thickness=-3,tileDif=200):
        rv= []

        for x in range(layers):
            rv.append(translate([0,x*tileDif,0])(
                    projection()(
                        intersection()(
                            insert("plane",z=start+x*thickness),
                            self.getPart()
                        )
                    )
            )
            )
        return union()(rv)

    def getSplit(self,start=0,depth=6,tileDif=200):
        rv= []

        rv.append(translate([0,0,0])(
            intersection()(
                insert("cube",size=[100,100,depth],z=start),
                self.getPart()
            )
        )
        )

        rv.append(translate([0,tileDif,depth])(
            intersection()(
                insert("cube",size=[100,100,depth],z=start-depth),
                self.getPart()
            )
        )
        )        
        return union()(rv)


 
 
************************************************/
