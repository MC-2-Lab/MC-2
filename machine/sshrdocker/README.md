# pySrun4kpySrun4k_BeihangLogin

## 简介
pySrun4k是一个模仿Srun4k认证客户端协议，用Python3实现的认证客户端。

实现了登录，检查在线状态，登出当前终端，登出所有终端功能。

## Docker版-自动监控保持在线、添加校园网反向代理至外网服务器实现内网穿透
ssh至外网采用密钥登录模式，放在docker内保证一定安全性
```
cd docker/
. env.sh txypasswd netusr netpasswd
build #only once
start
```
后续可以改main_login_regular.py 根据check_online返回的ip地址实现ip更新git

注意需要在云服务器上修改/etc/ssh/sshd_config中的GatewayPorts（改为yes）
## 更新
docker内已加入并注释校内反向代理到其他服务器的docker，见docker-compose.yml 取消注释并按对应说明操作并启动即可

## 登录
ssh -p 2242 root@cn.buaamc2.net
输入该跳板docker的root密码即可

