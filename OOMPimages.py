import os
from PIL import Image

def generateResolutions(item,overwrite=False):
    oompID = item.getTag("oompID").value
    print("Resolution Check for: " + oompID)
    #if("FOOTPRINT" in oompID):
    if True:
        
        res = [140,450,600]        
        images = item.getFilename("allImagesNames")
        for image in images:
            if item.ifFileExists(image):
                inFile=item.getFilename(image)                    
                for r in res:    
                    basewidth=r            
                    outFile = item.getFilename(image, resolution = r)                    
                    if not os.path.isfile(outFile) or overwrite:                      
                        print("        Generating: " + outFile)
                        img = Image.open(inFile)
                        wpercent = (basewidth / float(img.size[0]))
                        hsize = int((float(img.size[1]) * float(wpercent)))
                        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                        img.save(outFile)
        

