# gitlab私有化部署-docker方式

## 宿主机路径
/root/gitlab/
```
启动: 
docker-compose up -d
#修改url
# gitlab.rb文件内容默认全是注释
$ vim /root/gitlab/config/gitlab.rb
# 配置http协议所使用的访问地址,不加端口号默认为80

#external_url 'http://buaamc2.net:8081'  #修改后注意外面的docker-compose要改成8081:8081 不然打不开
# 配置ssh协议所使用的访问地址和端口
gitlab_rails['gitlab_ssh_host'] = 'buaamc2.net'
gitlab_rails['gitlab_shell_ssh_port'] = 222 # 此端口是run时22端口映射的222端口
#保存配置文件并退出
docker restart gitlab
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

## 首次进入
```
# 进入容器内部
docker exec -it gitlab /bin/bash

# 进入控制台
gitlab-rails console -e production

# 查询id为1的用户，id为1的用户是超级管理员
user = User.where(id:1).first
# 修改密码为123456
user.password='123456'
# 保存
user.save!
```