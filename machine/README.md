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
sshpass -p ywzpasswd ssh -o StrictHostKeyChecking=no ywz@10.134.162.xxx -p 22  "sshpass -p ywzpasswd ssh -o StrictHostKeyChecking=no ywz@10.134.162.xxx -p 22  \"echo ywzpasswd | sudo -S ls\""


# github端action配置(仓库配置secret)
# github-action ${{secrets.JUMP_PASSWORD}} ${{secrets.JUMP_USER}} ${{secrets.JUMP_IP}} ${{secrets.JUMP_PORT}} ${{secrets.MACHINE_PASSWORD}}
sshpass -p ${{secrets.JUMP_PASSWORD}} ssh -o StrictHostKeyChecking=no ${{secrets.JUMP_USER}}@${{secrets.JUMP_IP}} -p ${{secrets.JUMP_PORT}}  "sshpass -p ${{secrets.MACHINE_PASSWORD}} ssh -o StrictHostKeyChecking=no ywz@$10.134.162.162 -p 22  \"echo ${{secrets.MACHINE_PASSWORD}} | sudo -S ls && ls\""
# 全部配置见下文main.yml, 测试通过后ls替换为sh /github_action.sh

#vps端配置(或配置到vps端等任何一个机器-注意信息安全,不能直接push到仓库
jump_user, jump_ip, jump_port, jump_passwd = ["", "", "", ""]
machine_user, machine_ip, machine_port, machine_passwd = ["", "", "", ""]
exec_cmd = "sh /github_action.sh" # exec_cmd是写死在github端/vps端的，尽量简单 eg:"sh xx.sh" #相当于在machine机器上执行此命令
cmd = 'sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} -p {}  "sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} -p {}  \"echo {} | sudo -S {}\""'.format(jump_passwd, jump_user, jump_ip, jump_port, machine_passwd, machine_user, machine_ip, machine_port, machine_passwd, exec_cmd)

# 将真正脚本再次封装成单独文件放在machine机器，eg:/github_action.sh:"cd xx && git fetch --all && git reset --hard origin/master && git pull origin master -f && docker restart container_name_xx"

# 强制更新拉取两种方式
git pull --force; git checkout master
git fetch --all && git reset --hard origin/master && git pull origin master -f #第三步也可以不用
```


github-action配置文件main.yml完整示例(.github/workflow/main.yml 也可自动创建)
```
name: deploy_ssh

on:
  push:
    branches: [master]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: sshpass jump to machine ssh
        run: sshpass -p ${{secrets.JUMP_PASSWORD}} ssh -o StrictHostKeyChecking=no ${{secrets.JUMP_USER}}@${{secrets.JUMP_IP}} -p ${{secrets.JUMP_PORT}}  "sshpass -p ${{secrets.MACHINE_PASSWORD}} ssh -o StrictHostKeyChecking=no ywz@$10.134.162.162 -p 22  \"echo ${{secrets.MACHINE_PASSWORD}} | sudo -S ls && ls\""
```
