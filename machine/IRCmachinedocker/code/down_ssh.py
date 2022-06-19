# run this in .ssh/ and add `Include config.d/*` in .ssh/config first line.
# PS.jump_sever config need to add manually in .ssh/config, which is not keep in online file.
# If you need other user temporarily, you can input: ssh youruser@Host, like: ssh liutie@30901
import requests
import sys, os

youruser = "ywz"

if not os.path.exists("config.d"):
    os.mkdir("config.d")
file = "http://buaamc2.net/machine/IRCmachinedocker/code/config"
save_as = "config.d/BUAAMC2"
os.remove(save_as)
r = requests.get(file)
with open(save_as, 'wb') as f:
    # f.write(r.content)
    f.write(r.content.decode().replace("ywz", youruser).encode()) #替换公用默认账号
    f.close()
