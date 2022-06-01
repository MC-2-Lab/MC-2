# IRCmachinedocker
为校内总看板中心机器，此docker用来根据config中的各个机器ip进行逐个的sshpass访问查询CPU/GPU情况，并再通过sshpass方式上传给vps传入对应的状态txt文件(不入库)，从而更新看板信息。所有sshpass的账号密码以环境变量(env.sh)形式运行前给入、保证安全性。


# DockerOfBUAALogin
校内其他服务器的上网认证脚本，目前已改造成以docker形式自动掉线重连形式，账号密码同样以环境变量(env.sh)手动给入保证安全。 后续可以考虑将此docker加入ip上报(ip上报需更新git的config文件, 每个机器放git密钥较麻烦,可以考虑sshpass给中心机, 再定期从中心机git push即可)；以及也可也考虑直接上报自身CPU/GPU情况给vps，相比于中心机轮询更加稳定可靠[前提是机器能够正常上网]。
