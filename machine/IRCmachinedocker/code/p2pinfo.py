
# 定义校内其他机器信息
config = {
    "509": "10.135.206.119",
    "401":"10.134.162.193",
    "2080":"10.134.162.90",
    "207":"10.134.162.162",
    "30901":"10.130.157.44",
    "30902":"10.130.158.90",
    "930": "10.134.126.158",
    "220": "183.129.176.220",
    "ali4k": "121.40.238.191",
    "ali8k": "47.96.9.177",
}

# 定义特例账号名-个别服务器账号名特殊，不方便再建新的，如杭研院机器
special_user = {
    "220": "yangwenzhe"
}


# 最终upload-把信息上传vps 方便广域网查看-要求账号密码也一致
remote_ip = "buaamc2.net"
remote_location = "/var/www/upload/"