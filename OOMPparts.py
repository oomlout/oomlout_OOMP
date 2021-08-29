import OOMP

for subdir, dirs, files in os.walk(directory):
    for file in files:
        if(file == "details.py" or file == "qrCode.py"  ):
            moduleName = file.replace(".py","")
            moduleName = subdir.replace("\\",".") + "." + moduleName
            ##print("    moduleName: " + moduleName)
            __import__(moduleName)
