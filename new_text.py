import os

goalPath = "/Users/tarrant/Documents/"




def loadFile(path):
    files = os.listdir(path)
    for file in files:
        allPath = os.path.join(path, file)
        if os.path.isdir(allPath):
            loadFile(allPath)
        elif file.endswith(".js"):
            print(allPath)
            os.system("uglifyjs " + allPath + " -o " + allPath + " -c -m")


loadFile(goalPath)
