# pySrun4kpySrun4k_BeihangLogin

## 简介
pySrun4k是一个模仿Srun4k认证客户端协议，用Python3实现的认证客户端。

实现了登录，检查在线状态，登出当前终端，登出所有终端功能。

## Docker版-自动监控保持在线
```
cd docker/
. env.sh user password
build #only once
start
```
后续可以改main_login_regular.py 根据check_online返回的ip地址实现ip更新git

## 更新
docker内已加入并注释校内反向代理到其他服务器的docker，见docker-compose.yml 取消注释并按对应说明操作并启动即可


## 依赖

requests

```pip install requests```

## API

### 登录

```srun4k.do_login(username,pwd,mbytes=0,minutes=0)```

### 检查在线状态

```srun4k.check_online()```

### 登出当前终端

```srun4k.do_logout(username)```

### 登出所有终端

```srun4k.force_logout(username,password)```

## Login.py

可以直接通过命令行调用

### 登录
```python Login.py login <username> <password>```

### 检查在线状态
```python Login.py check_online```

### 登出当前终端
```python Login.py logout <username>```

### 登出所有终端
```python Login.py logout_all <username> <password>```