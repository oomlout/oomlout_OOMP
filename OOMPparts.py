import OOMP
import os

files = os.listdir()
directory = "parts\\"

for subdir, dirs, files in os.walk(directory):
    for file in files:
        if(file == "details.py" or file == "qrCode.py"  ):
            moduleName = file.replace(".py","") 
            moduleName = subdir.replace("\\",".") + "." + moduleName
            ##print("    moduleName: " + moduleName)
            __import__(moduleName)

print("Parts:")
for part in OOMP.parts:
    print("Loaded: " + part.getTag("oompID").value + "  " +  part.getTag("name").value)
          
