import OOMP
import os

files = os.listdir()

##for file in files:
##    if "TAXApart_" in file:
##        #print(file)
##        moduleName = file.replace(".py","")
##        __import__(moduleName)

directory = "parts\\"

for subdir, dirs, files in os.walk(directory):
    for file in files:
        if(file == "details.py"):
            moduleName = file.replace(".py","")
            moduleName = subdir.replace("\\",".") + "." + moduleName
            ##print("    moduleName: " + moduleName)
            print(".",end="")
            __import__(moduleName)

directory = "templates\\diag\\"

for subdir, dirs, files in os.walk(directory):
    for file in files:
        if ".py" in file and "pycache" not in subdir :
            moduleName = file.replace(".py","")
            moduleName = subdir.replace("\\",".") + moduleName
            #print("    moduleName: " + moduleName)
            print(".",end="")
            __import__(moduleName)                    