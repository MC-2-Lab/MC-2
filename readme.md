# IRC-Website4.0 : django版&git+docker部署

# 1.服务器部署
## version
1.0 纯静态文件  
2.0 express-nodejs版  
3.0 django+nginx+sqlite3  
4.0(*) git+docker+nginx+django+sqlite3  

## 使用git+docker配置部署(推荐):
首先安装docker和docker-compose 可直接apt安装
```
apt install docker
apt install docker.io
apt install docker-compose

mkdir /var/www/upload
chmod -R 777 /var/www/upload #用来接收校内的看板信息

```
项目部署
```
git pull origin master
cd docker
. env.sh
build

start
```
日志文件位于docker/log/django.log中  
后续更新时,直接git pull更新即可，不需要手动传新文件


## 不使用docker配置部署:

例：将此django文件夹放于/var/www/django处：

文件结构：/var/www/django/ ...  [readme.md,(django1),(html),*.html,...]

1. 部署django环境，测试运行

   在django1/下运行python3 manage.py runserver 0.0.0.0:8050 测试 ctrl+c退出

2. 安装nginx，按照nginx文件夹里备份进行配置

3. 安装supervisor，按照nginx文件夹里备份进行配置，目的是自动运行django脚本

(4. 配置81后台网站需要的认证模块

   sudo apt search htpasswd

   sudo apt install apache2-utils

   mkdir /usr/local/nginx

   touch /usr/local/nginx/passwd.db

   htpasswd -c /usr/local/nginx/passwd.db admin

   #输入密码-----

   chmod 400 /usr/local/nginx/passwd.db

   chown nginx  /usr/local/nginx/passwd.db

   cat /usr/local/nginx/passwd.db
)
   

# 2. 更新修改数据

1. members相关为纯静态页面，对应改html文件代码即可，包括修改照片等信息


2. 网站论文及发表内容均通过sqlite3数据库文件修改，可以参考根目录下的操作视频，使用DBMS软件可视化操作

3. git提交

# 3. IRC内部网站建设
## version
### 1.0 vue+nginx加账号密码版
见vue81html文件夹
### 2.0(*) 在线文档版
使用飞书在线excel进行加密，备份文件见vue81html/内部网站2.0在线文档版/excel文件


# 4.0 看板docker配置及更新
```
cd machine/IRCmachinedocker

# 如果没有镜像则进行编译，后续修改代码不需要重新编译
build

# 配置运行
. env.sh user password # 使用所有机器共有的账号，特例见code/get_user_remote.py最后
# 如果ip有变动，修改code/get_user_remote.py 200行左右的ip地址字典
# 修改后git push  机器端git pull 再docker restart即可

# 启动
start
```
