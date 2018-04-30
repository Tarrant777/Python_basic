
import os

path = "/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/"

a = os.listdir(path)
file_name = []
directory = []
for i in a:
    if i.endswith(".js"):
        file_name.append(i)
    elif i == "scene":
        for j in os.listdir(path+"scene/"):
            if j.endswith(".js"):
                file_name.append("scene/"+j)
            elif j == "main":
                for k in os.listdir(path+"scene/"+"main/"):
                    if k.endswith(".js"):
                        file_name.append("scene/"+"main/" + k)
                    elif k == "formain":
                        for l in os.listdir(path + "scene/" + "main/"+""):
                            if l.endswith(".js"):
                                file_name.append("scene/" + "main/" + l)


print(file_name)
print(len(file_name))



