# IRC-Website3.0 : django版

不同于纯静态版（1.0）和express-nodejs版（2.0），django版搭配nginx更加灵活、便于部署和迁移



例：将此django文件夹放于/var/www/django处：

文件结构：/var/www/django/ ...  [readme.md,(django1),(html),*.html,...]



1. 部署django环境，测试运行

   在django1/下运行python3 manage.py runserver 0.0.0.0:8050 测试 ctrl+c退出

2. 安装nginx，按照nginx文件夹里备份进行配置

3. 安装supervisor，按照nginx文件夹里备份进行配置，目的是自动运行django脚本

4. 配置81后台网站需要的认证模块

   sudo apt search htpasswd

   sudo apt install apache2-utils

   mkdir /usr/local/nginx

   touch /usr/local/nginx/passwd.db

   htpasswd -c /usr/local/nginx/passwd.db admin

   #输入密码-----

   chmod 400 /usr/local/nginx/passwd.db

   chown nginx  /usr/local/nginx/passwd.db

   cat /usr/local/nginx/passwd.db

   

## 更新修改数据

1. members相关为纯静态页面，对应改html文件代码即可，包括修改照片等信息

~~2. 网站论文及发表内容均为通过*.ini数据文件进行配置，方便查看和修改：~~

2. 网站论文及发表内容均通过sqlite3数据库文件修改，可以参考根目录下的操作视频，使用DBMS软件可视化操作


# 内部网站

## 1.0 vue+nginx加账号密码版
见vue81html文件夹

## 2.0 在线文档版
使用飞书在线excel进行加密，备份文件见vue81html/内部网站2.0在线文档版/excel文件
