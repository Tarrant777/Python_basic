from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import os

"""
# 路徑
# goalPath = "/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/"
goalPath = "/Users/tiffany/Documents/mygame/newtianyu/MyJSGame/src/"
a = os.listdir(goalPath)
file_name = []
directory = []
for i in a:
    if i.endswith(".js"):
        file_name.append(goalPath+i)
    elif i == "scene":
        for j in os.listdir(goalPath + "scene/"):
            if j.endswith(".js"):
                file_name.append(goalPath+"scene/" + j)
            elif j == "main":
                for k in os.listdir(goalPath + "scene/" + "main/"):
                    if k.endswith(".js"):
                        file_name.append(goalPath+"scene/" + "main/" + k)
                    elif k == "formain":
                        for l in os.listdir(goalPath + "scene/" + "main/" + "formain/"):
                            if l.endswith(".js"):
                                file_name.append(goalPath+"scene/" + "main/" + "formain/"+ l)

"""
#  goalPath = "/Users/tarrant/Desktop/Tarrantnew/newtianyu/MyJSGame/src/"
#  goalPath = "/Users/office/Documents/newtianyu/newtianyu/MyJSGame/src/"
goalPath = "/Users/tiffany/Documents/mygame/newtianyu/MyJSGame/src/"
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
del_file = [goalPath + 'scene/games/fishing/src/HrFishData/HrFishText.js',
            goalPath + 'scene/games/fishing/src/HrFishLobby/HrLobbyView/HrRoomScrollViewUI/HrRoomListLayer.js',
            goalPath + 'scene/games/fishing/src/HrFishLobby/HrLobbyView/HrRoomScrollViewUI/HrRoomListWithoutRoom1Layer.js',
            goalPath + 'scene/games/fishing/src/Common/ProtoBuf.js',
            goalPath + 'scene/games/fishing/src/Common/ByteBufferAB.js',
            goalPath + 'GameUtil.js',
            goalPath + 'net/SHA256.js',
            goalPath + 'logic/BaseScene.js',
            goalPath + 'scene/games/game_dzpk/DZPKAPI.js',
            goalPath + 'HrFishGame/HrFishView/HrGameUISkill/HrSkillLayer.js',
            goalPath + 'scene/games/fishing/src/HrFishGame/HrFishView/HrGameMainUI/HrTrumpetShowLayer.js',
            goalPath + 'scene/games/fishing/src/Common/platform.js',
            goalPath + "scene/main/MainLayer.js",
            goalPath + "net/GameSysNet.js",
            goalPath + "scene/views/pay/PayLayer.js",
            goalPath + "scene/views/pay/PayLayer_ios.js",
            goalPath + "scene/share/game/GameEventNotifier.js",
            goalPath + "net/GameNet.js",
            goalPath + "scene/views/bank/BankSaveCashLayer.js"]

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
        print("無法自動:", x)
    driver.close()
    print(time.strftime("%H:%M:%S"), x)
