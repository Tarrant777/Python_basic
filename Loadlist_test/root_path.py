import os

# __file__為檔案本身
# 真實檔案位置
rootPath = os.path.realpath(__file__)

# 用/分隔成list, 扣掉檔案名為資料夾,再扣掉一層即為上一層
rootPath = rootPath.split("/")[:-2]
# 利用/加入list中成為檔案位置
rootPath = "/".join(rootPath)
print(rootPath)
