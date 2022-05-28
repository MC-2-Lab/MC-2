# 已有仓库使用私有化部署的gitlab
本功能并不影响原仓库正常使用github/gitee  
首先到gitlab中新建一个仓库并添加ssh密钥  
在原有github/gitee仓库基础上，执行以下步骤  
```
#对系统ssh增加配置（.ssh/config）
# gitlab
Host gitlab.com
  HostName buaamc2.net #如果自己进行端口转发则换127.0.0.1
  Port 8022
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_rsa.gitlab #可以直接拷贝github/gitee的一对密钥并改名
##

#对原仓库路径下.git/config增加一条配置(.git默认隐藏)
[remote "gitlab"]
url = ssh://git@gitlab.com/yangwenzhe/mybackup.git #替换成对应的ssh链接, 但127.0.0.1用gitlab.com代替, 以链接到对应的密钥
fetch = +refs/heads/*:refs/remotes/origin/*
##

#测试
git push gitlab master
```
