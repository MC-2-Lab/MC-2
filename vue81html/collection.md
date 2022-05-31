# 脚本工具百宝箱
$$以markdown方式，方便修改提MR到github$$


## 1.重点内容
使用方式根据名称按ctrl+f搜索本文档内容
|名称|备注|
|------|------|
|创建账号||
|docker使用|部署个人Docker文档说明(IRC炼丹专用)|
|校内linux免装v2ray临时/永久配置流量代理||
|命令行认证校园网||
|监控显卡、空闲后邮件通知<br>任意命令结束邮件通知|显卡空闲邮件通知/命令结束提醒|

## 2.重点说明
- 机器数据盘隔离&开机挂载脚本
保证数据安全，尽量全部用机械硬盘而非系统盘，而多块硬盘的挂载命令单独放进脚本，方便重启时一键执行。
```
#开机需执行
sudo sh /mount.sh #内容参考下表"额外机械硬盘配置需求/使用"
#将机械挂载到 /temp_disk2 /temp_disk3 ...
# 如果安装了docker并将docker的目录放到了机械硬盘上，则需要挂载后重启docker(docker restart和docker.sock赋权[见下条]也需要放进/mount.sh)
```
- 账号无docker权限问题
不要暴力赋权，参考“docker使用”节文档，采用对docker.sock文件刷权限(可放进/mount.sh)
`sudo chmod a+rw /var/run/docker.sock #恢复则刷660`



## 3.所有集合
|功能|备注|链接||
|------|------|------|------|
|玩转跳板机|vscode/shell/mobaxterm|https://github.com/ywz978020607/History/tree/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/%E7%8E%A9%E8%BD%AC%E8%B7%B3%E6%9D%BF%E6%9C%BA||
|git推荐配置||https://github.com/ywz978020607/History/blob/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/%E4%B8%AD%E5%BF%83%E5%8C%96%E5%A4%9A%E6%9C%BA%E5%99%A8%E5%BC%80%E5%8F%91%E6%8E%A8%E8%8D%90%E9%85%8D%E7%BD%AE.md||
|tmux鼠标配置、重新适配窗口等||https://github.com/ywz978020607/History/blob/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/tmux%E9%BC%A0%E6%A0%87%E9%85%8D%E7%BD%AE.md||
|linux运维常用命令|<img src=img/5.png width=200>|https://github.com/ywz978020607/History/blob/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/%E5%B8%B8%E7%94%A8linux%E8%84%9A%E6%9C%AC.md||
|服务器集群显卡用户占用情况||https://github.com/ywz978020607/History/tree/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/%E6%9B%B4%E6%96%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%94%A8%E6%88%B7%E5%8D%A0%E7%94%A8%E6%83%85%E5%86%B5||
|显卡驱动卸载与重装|https://cn.download.nvidia.cn/XFree86/Linux-x86_64/510.60.02/NVIDIA-Linux-x86_64-510.60.02.run|https://github.com/ywz978020607/History/blob/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/ubuntu18.04%E6%96%B0%E6%9C%BA%E9%85%8Dcuda%E9%A9%B1%E5%8A%A8.md||
|linux-上传/下载北航云盘文件方法||https://github.com/ywz978020607/History/blob/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/bhpan.py<br>更好方法：https://github.com/xdedss/dist_bhpan||
|win-wsl配置||https://github.com/ywz978020607/History/tree/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/WSL%E7%9B%B8%E5%85%B3%E9%85%8D%E7%BD%AE||
|创建账号|`sudo adduser lep`<br>赋权成为管理员:<br>sudo usermod -a -G adm lep<br>sudo usermod -a -G sudo lep|
|认证校园网|cd /home/ywz/data/pySrun4k_BeihangLogin-master<br>python Login.py login 学号 密码|https://github.com/ywz978020607/History/tree/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/pySrun4k_BeihangLogin-master|||
|查看当前服务器各显卡用户占用情况|<img src=img/13.png width=200>|https://github.com/ywz978020607/History/blob/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/%E6%9B%B4%E6%96%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%94%A8%E6%88%B7%E5%8D%A0%E7%94%A8%E6%83%85%E5%86%B5/sys_user.py||
|额外机械硬盘配置需求/使用|每个机器都有1-2张机械硬盘（内置），需要按顺序挂载到/temp_disk2、/temp_disk3、..<br>可以软链接挂载，也可以用写到/mount.sh脚本中，每次开机执行<br>sudo sh /mount.sh<br>/mount.sh参考脚本链接如下图|https://github.com/ywz978020607/History/blob/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/%E6%8C%82%E8%BD%BD%E7%A1%AC%E7%9B%98%E5%8F%8A%E5%8F%8C%E7%A1%AC%E7%9B%98%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86.md|||
||<img src=img/15.png width=200>|||
|显卡功耗限制||https://nachifur.blog.csdn.net/article/details/120336516?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=2||
|监控显卡、空闲后邮件通知|"#空闲阈值/G接收邮箱显卡号(all)可选追加通知信息<br>python watch_alert.py 4.5 ywzsunny@buaa.edu.cn all xxxx<br>(微信中关注qq邮箱公众号可开启微信提醒)"|https://github.com/ywz978020607/History/tree/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/%E6%9B%B4%E6%96%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%94%A8%E6%88%B7%E5%8D%A0%E7%94%A8%E6%83%85%E5%86%B5|||
|任意命令结束邮件通知|"#可嵌入任何脚本结束追加脚本名(非同级可用绝对路径)、邮箱、追加信息(可选)<br>#eg:[xxx(你的脚本)]&&python /xxxx/watch_alert.py xxxx@qq.com xxxx"|同上|<img src=img/18.png width=200>||
|显卡驱动版本-pytorch|https://www.html.cn/script/python/141467.html|https://pytorch.org/get-started/previous-versions/||
|"校内linux免装v2ray临时/永久配置流量代理,可搭配个人电脑的v2ray(win)使用"|<img src=img/20.png width=200>|https://blog.csdn.net/dieju8330/article/details/86445698||
|显示天气预报（可加入.profile每次打开终端显示）|<img src=img/21.png width=200>|"命令：<br>curl http://wttr.in"|
|显卡风扇转速限制（本地设置）|本地图形界面将显示器接在显卡上，进入NVIDIAXserversettings可以修改|<img src=img/22.png width=200>||
|显卡风扇转速限制（远程设置）|"nvidia-settings-a""[gpu:0]/GPUFanControlState=1""-a""[fan:0]/GPUTargetFanSpeed=99"""|如果nvidia-settings报错，连接不上，可参考右侧链接|Linux上でNVIDIAのGPUのファンをコントロールする–philo式(philosy.com)|
|python动态传参封装-代码参考|有别于每次修改conf文件/设定冗长的parser引入/sys.argv[]严格顺序，改用默认字典自动传参引入，见代码|https://github.com/ywz978020607/History/tree/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/%E5%B0%81%E8%A3%85%E5%BC%8F%E5%8A%A8%E6%80%81%E4%BC%A0%E5%8F%82||
|显示本地真实路径|pwd -P|<img src=img/25.png width=200>||
|查看sudo权限使用记录|cat /var/log/auth.log|||
|docker使用|改造完成，文档已齐全，可随时构建自己的镜像|https://github.com/ywz978020607/History/tree/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/mydocker||
|nfs配置使用|1server对multiclients|https://github.com/ywz978020607/History/tree/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/nfs%E7%BD%91%E7%BB%9C%E5%85%B1%E4%BA%AB%E9%85%8D%E7%BD%AE||
|显卡占用情况集中看板-docker|一台校内机器运行即可，注意首次连接sshgenkey|https://github.com/Archer-Tatsu/MC-2/tree/master/machine/IRCmachinedocker||
|测速|iperf3|https://github.com/ywz978020607/History/blob/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/nfs%E7%BD%91%E7%BB%9C%E5%85%B1%E4%BA%AB%E9%85%8D%E7%BD%AE/ip%E6%B5%8B%E9%80%9F.md||
|ssh密钥登录&别名代替ip地址&vscode|见右边的文件，可以直接改用户名复制到自己的电脑上|config_method.md||
|png图片转gif图(支持透明通道-透明的png转透明的gif)|python convertgit.py|[https://github.com/ywz978020607/History/blob/81d31277998172ed588cf611b3147fc3c5bba215/%E6%97%A5%E5%B8%B8%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7/convergif.py](https://github.com/ywz978020607/History/blob/81d31277998172ed588cf611b3147fc3c5bba215/日常自动化工具/convergif.py)||
|tobefinish|xxx|xxx
|xxx|xxx|xxx
