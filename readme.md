# IRC-Website  django版

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

1. members相关为纯静态页面，对应改html文件代码即可

2. 网站论文及发表内容均为通过*.ini数据文件进行配置，方便查看和修改：

   修改方法：

   进入py操作ini文件夹，见“新增add.py”脚本，实现对应ini的增删查改，将修改后的ini文件复制到django1/app1/*.ini处，实现数据替换 【怕误操作可提前备份ini文件】



