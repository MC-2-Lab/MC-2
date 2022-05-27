# 配置http协议所使用的访问地址,不加端口号默认为80
external_url 'http://buaamc2.net:8081'
# 配置ssh协议所使用的访问地址和端口
gitlab_rails['gitlab_ssh_host'] = 'buaamc2.net'
gitlab_rails['gitlab_shell_ssh_port'] = 222 # 此端口是run时22端口映射的222端口