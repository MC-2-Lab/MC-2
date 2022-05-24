```
. env ywz passwd

#若第一次进入
build
site
sh /tmp/build.sh
把所有的ssh连一边建立key
#测试
...

#再封装替换镜像
docker commit xxx xxx


之后重新从镜像创建容器时 start 即可


# 运行日志查看
cat machine.log

```


# 文件说明
```
code/文件夹下为
校内看板跳转机对应代码：
get_user_remote.py 主要程序(docker内执行)
p2pinfo.py为全仓库唯一ip实时更新文件，目的用于：内网查看ip信息；校内看板跳转机逐机器进行CPU/GPU资源查询。

vps远程端代码：
all_external.html为vps端进行公网看板信息的网址
```

# github-Action触发内网机器拉取(需跳板机)
将跳板机信息保存到github的secret保证安全性
命令示例:
```
#测试
sshpass -p ywzbuaamc2 ssh -o StrictHostKeyChecking=no ywz@10.134.162.xxx -p 22  "sshpass -p ywzbuaamc2 ssh -o StrictHostKeyChecking=no ywz@10.134.162.xxx -p 22  \"ls\""

# cmd为github端action配置(或配置到vps端等任何一个机器-注意信息安全,不能直接push到仓库)
cmd = 'sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} -p {}  "sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} -p {}  \"{}\""'.format(jump_passwd, jump_user, jump_ip, jump_port, machine_passwd, machine_user, machine_ip, machine_port, exec_cmd)

# exec_cmd = "cd xx && git fetch --all && docker restart container_name_xx"
```