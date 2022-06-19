# run this in .ssh/ and add `Include config.d/*` in .ssh/config first line.
# PS.jump_sever config need to add manually in .ssh/config, which is not keep in online file.
# If you need other user temporarily, you can input: ssh youruser@Host, like: ssh liutie@30901
from imageio import save
import requests
import sys, os
import platform

youruser = "ywz"

if not os.path.exists("config.d"):
    os.mkdir("config.d")
file = "http://buaamc2.net/machine/IRCmachinedocker/code/config"
save_as = "config.d/config"
if platform.system() == "Windows":
    if not os.path.exists(save_as.replace("/","\\")):
        os.system("copy {} {}".format("config", save_as.replace("/","\\")))
else:
    if os.path.exists(save_as):
        os.remove(save_as)
    os.system("cp -p {} {}".format("config", save_as))

r = requests.get(file)
with open("down", 'wb') as f:
    # f.write(r.content)
    f.write(r.content.decode().replace("ywz", youruser).encode()) #替换公用默认账号
    f.close()

if not platform.system() == "Windows":
    os.system("cat {} > {}".format("down", save_as))
else:
    print("手动复制down内容到config.d/配置文件中，解决权限冲突")
