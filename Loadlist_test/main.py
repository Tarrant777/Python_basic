import os

# 真實檔案位置
#rootPath = os.path.realpath(__file__)

# 用/分隔成list, 扣掉檔案名為資料夾,再扣掉一層即為上一層
#rootPath = rootPath.split("/")[:-2]
# 利用/加入list中成為檔案位置
#rootPath = "/".join(rootPath)



# goalPath = rootPath+"/MyJSGame/src"
goalPath = "/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/"
file_name = []

def loadFile(path):
    files = os.listdir(path)
    for file in files:
        allPath = os.path.join(path, file)
        if os.path.isdir(allPath):
            loadFile(allPath)
        elif file.endswith(".js"):
            file_name.append(allPath)
            # os.system("uglifyjs " + allPath + " -o " + allPath + " -c -m")

loadFile(goalPath)
print(file_name)
print(len(file_name))