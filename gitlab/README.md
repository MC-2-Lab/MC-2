# gitlab私有化部署-docker方式

## 宿主机路径
/root/gitlab/
```
#修改url
# gitlab.rb文件内容默认全是注释
$ vim /root/gitlab/config/gitlab.rb
#
# 配置http协议所使用的访问地址,不加端口号默认为80
external_url 'http://buaamc2.net:8081'
# 配置ssh协议所使用的访问地址和端口
gitlab_rails['gitlab_ssh_host'] = 'buaamc2.net'
gitlab_rails['gitlab_shell_ssh_port'] = 222 # 此端口是run时22端口映射的222端口
:wq #保存配置文件并退出
```

或
```
docker run \
 -itd  \
 -h gitlab.buaamc2.net\
 -p 222:22 \
 -p 8081:80 \
 -v /usr/local/gitlab/etc:/etc/gitlab  \
 -v /usr/local/gitlab/log:/var/log/gitlab \
 -v /usr/local/gitlab/opt:/var/opt/gitlab \
 --name gitlab \
 gitlab/gitlab-ce
```
