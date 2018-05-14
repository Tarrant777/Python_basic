from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import os

"""
# 路徑
path = "/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/"

a = os.listdir(path)
file_name = []
directory = []
for i in a:
    if i.endswith(".js"):
        file_name.append(i)
    elif i == "scene":
        for j in os.listdir(path + "scene/"):
            if j.endswith(".js"):
                file_name.append("scene/" + j)
            elif j == "main":
                for k in os.listdir(path + "scene/" + "main/"):
                    if k.endswith(".js"):
                        file_name.append("scene/" + "main/" + k)
                    elif k == "formain":
                        for l in os.listdir(path + "scene/" + "main/" + ""):
                            if l.endswith(".js"):
                                file_name.append("scene/" + "main/" + l)
"""

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
print(time.strftime("%H:%M:%S"))
del_file = ['/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/scene/games/fishing/src/HrFishData/HrFishText.js',
            '/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/scene/games/fishing/src/HrFishLobby/HrLobbyView/HrRoomScrollViewUI/HrRoomListLayer.js',
            '/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/scene/games/fishing/src/HrFishLobby/HrLobbyView/HrRoomScrollViewUI/HrRoomListWithoutRoom1Layer.js',
            '/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/scene/games/fishing/src/Common/ProtoBuf.js',
            '/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/scene/games/fishing/src/Common/ByteBufferAB.js',
            '/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/GameUtil.js',
            '/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/net/SHA256.js',
            '/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/logic/BaseScene.js']


for d in del_file:
    if d in file_name:
        file_name.remove(d)

for x in file_name:
    file = open(x)
    code_origin = file.read()
    os.system("echo '%s' | pbcopy" % code_origin)

    driver = webdriver.Firefox()
    # options = Options()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(firefox_options=options)

    # driver.get("file:///Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/" + x)
    # driver.find_element_by_xpath("//pre[1]").send_keys((Keys.COMMAND, 'a'))
    # driver.find_element_by_xpath("//pre[1]").send_keys((Keys.COMMAND, 'c'))
    # a = driver.find_element_by_xpath("//pre[1]")

    driver.get("http://www.javascriptobfuscator.com/Javascript-Obfuscator.aspx")
    # print(driver.find_element_by_id('ctl00_MainContent_TextBox1').get_attribute('value'))
    # driver.find_element_by_id('ctl00_MainContent_TextBox1').send_keys((Keys.COMMAND, 'a'))
    driver.find_element_by_id('ctl00_MainContent_TextBox1').clear()
    driver.find_element_by_id('ctl00_MainContent_TextBox1').send_keys((Keys.COMMAND, "v"))
    # driver.find_element_by_id('ctl00_MainContent_TextBox1').send_keys(code_origin)
    driver.find_element_by_id('ctl00_MainContent_Button1').click()
    time.sleep(3)
    # print(driver.find_element_by_id('ctl00_MainContent_TextBox2').get_attribute('value'))
    code_after = driver.find_element_by_id('ctl00_MainContent_TextBox2').get_attribute('value')
    if code_after[0:3] == 'var':
        file = open(x, 'w')
        file.write(code_after)
        file.close()
    else:
        print("有問題:",x)
    driver.close()
    print(time.strftime("%H:%M:%S"), x)

