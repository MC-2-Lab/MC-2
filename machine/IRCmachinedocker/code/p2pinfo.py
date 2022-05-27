# 机器信息维护在config文件中 其他同学可以直接wget同步config作为跳板配置(如需替换用户名可使用sed命令)
# 最终upload-把信息上传vps 方便广域网查看-要求账号密码也一致
remote_ip = "buaamc2.net"
remote_location = "/var/www/upload/"

config_file = 'code/config'
if __name__ == "__main__":
    config_file = 'config'
f = open(config_file,'r')
context = f.read()
f.close()
context = context.split("\n")
##
config = {}
special_user = {}
special_port = {}
temp_name = ""
for line in context:
    line = line.split("#")[0].strip()
    if line == "":
        continue
    kind = line.split(" ")[0]
    if kind == 'Host':
        temp_name = line.split(" ")[1]
    elif 'jump' in temp_name:
        continue
    elif kind == 'Port' and line.split(" ")[1] != '22':
        special_port[temp_name] = line.split(" ")[1]
    elif kind == 'HostName':
        config[temp_name] = line.split(" ")[1]
    elif kind == 'User':
        special_user[temp_name] = line.split(" ")[1]
if __name__ == "__main__":
    print(config)
    print(special_user)
    print(special_port)


# config = {
#     "509": "10.134.163.12",
#     "401":"10.134.162.193",
#     "2080":"10.134.162.175",
#     "207":"10.134.162.162",
#     "30901":"10.130.157.75",
#     "30902":"10.130.158.90",
#     "930": "10.134.126.158",
#     "220": "183.129.176.220",
#     "ali4k": "47.111.111.29",
#     "ali8k": "47.111.185.214",
# }

# # 定义特例账号名-个别服务器账号名特殊，不方便再建新的，如杭研院机器
# special_user = {
#     "220": "yangwenzhe"
# }

# special_port = {
#     "30901" : '2220',
# }