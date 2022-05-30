# gilab访问及配置概览
## 官方在线版本[gitlab.com](http://gitlab.com)
 配置与下方类似，端口可省略不填  
 官方版本不提供内部仓库，仅区分私有和公开，故需要由仓库owner显示邀请相应人。  
 建议加入[BUAA-MC2群组](https://gitlab.com/buaa-mc2)
## 校内私有化部署版本
以下三种方式殊途同归，可根据自身特点进行选择，域名映射内网ip:  `gitlab.buaamc2.net`=`10.134.162.162`（内网ip 仅限校内访问）
| 方式      | 特点 | 对应网页端 | ssh端 | 
| ----------- | ----------- | ----------- | ----------- |
| 校内直连      | 速度最快, 但需要在校内, 且内网ip可能会变, 适合校内其他服务器配置| http://gitlab.buaamc2.net:8081 |  ssh://git@gitlab.buaamc2.net:8022 |
| 手动本机代理   | 最灵活, 可使用跳板/直连, 以本机ip进行配置, 适合校外访问加速(需运行端口转发命令) | http://127.0.0.1:8081 | ssh://git@127.0.0.1:8022 |
| vps-docker代理   | 最稳定, vps实时代理+跳板内网穿透, 但多了一层vps转发、速度最慢, 适合互相分享链接(ip不会改变) | http://buaamc2.net:8081 (稳定不变) | ssh://git@buaamc2.net:8022 |

# 已有仓库使用私有化部署的gitlab
本功能并不影响原仓库正常使用github/gitee  
首先到gitlab中新建一个仓库并添加ssh密钥  
在原有github/gitee仓库基础上，执行以下步骤  
```
#对系统ssh增加配置（.ssh/config）
# mygitlab.com 替换链接中buaamc2.net:8022
Host mygitlab.com
  HostName buaamc2.net #如果自己进行端口转发则换127.0.0.1 #如校内机器可配置为gitlab.buaamc2.net
  Port 8022
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_rsa.gitlab #可以直接拷贝github/gitee的一对密钥并改名
  # ProxyCommand connect -S 127.0.0.1:10808 -a none %h %p #win-dns解析失败时设置走socks代理
##
测试 ssh -T git@mygitlab.com

#对原仓库路径下.git/config增加一条配置(.git默认隐藏)
[remote "mygitlab"]
url = ssh://git@mygitlab.com/yangwenzhe/mybackup.git #替换成对应的ssh链接, 但127.0.0.1用mygitlab.com代替, 以链接到对应的密钥
fetch = +refs/heads/*:refs/remotes/origin/*
##

#测试
git push mygitlab master
```

使用buaamc2.net时默认直接走内网穿透+境外vps代理，如果觉得速度太慢，可执行：
```
【校外端口转发加速】
ssh -L 8081:gitlab.buaamc2.net:8081 jump1/jump2/xx
ssh -L 8022:gitlab.buaamc2.net:8022 jump1/jump2/xx
其中jump1/jump2/xx为ssh config配置(见首页config文件)
或不需要config文件, 显式使用user@ip:port作为跳板机
```
之后将config中mygitlab对应的HostName由buaamc2.net替换为127.0.0.1
打开浏览器时输入127.0.0.1:8081即可
