import os
import time
from p2pinfo import *
# import psutil

def task1(ip,user,passwd,machine_name,port):
    file_name = '/src/{}.txt'.format(machine_name)
    out_cpu = ""
    out_mem = ""

    # #本机占用
    # out_cpu = psutil.cpu_percent(1)
    # out_mem = psutil.virtual_memory().percent
    #ssh测量
    # cpu> top -bn1 | grep load | awk '{printf "CPU Load: %.2f\n", $(NF-2)}'
    p = os.popen('timeout 5s sshpass -p \"{}\" ssh {}@{} -p {} "top -bn1 | grep load"'.format(passwd,user,ip,port))
    out = p.read()
    out_cpu = out.split()[-3].strip(",")

    # mem> free -m | awk 'NR==2{printf "Memory Usage: %s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'
    p = os.popen('timeout 5s sshpass -p \"{}\" ssh {}@{} -p {} "free -m "'.format(passwd,user,ip,port))
    out = p.read()
    used_mem = float(out.split("\n")[1].split()[2])
    all_mem = float(out.split("\n")[1].split()[1])
    out_mem = "{:.2f}".format(used_mem/all_mem*100)

    nvidia_version = ""
    p = os.popen('timeout 5s sshpass -p "{}" ssh {}@{} -p {} nvidia-smi'.format(passwd,user,ip,port))

    out = p.read()
    # print(out)
    # raise ValueError("stop")
    all_lines = out.split('\n')
    all_data = {}
    gpu_data = []

    flag1 = False
    for ii in range(len(all_lines)):
        if 'NVIDIA-SMI' in all_lines[ii]:
            nvidia_version = all_lines[ii].strip().strip("|").split("Driver Version:")[1].replace("CUDA Version:"," | cuda below:").strip()
            nvidia_version = ' '.join(nvidia_version.split())
            continue

        if 'Default' in all_lines[ii]:
            gpu_data.append([all_lines[ii-1].split('|')[1].strip().split(' ')[0],all_lines[ii].split('|')[2].strip()])

        if ii>2 and 'Process name' in  all_lines[ii-1]:
            flag1 = True
            continue

        if flag1:
            if '------' in all_lines[ii]:
                break
            elif 'C' in all_lines[ii]:
                temp_data = all_lines[ii].split(' ')
                temp_user = []
                for kk in range(len(temp_data)):
                    if temp_data[kk]!='|' and temp_data[kk]!='':
                        temp_user.append(temp_data[kk])
                #获取用户名
                p = os.popen('timeout 5s sshpass -p "{}" ssh {}@{} -p {} ps -f -p'.format(passwd,user,ip,port) + str(temp_user[-4]))
                out = p.read().split('\n')[1].split(' ')[0]

                if temp_user[0] in all_data.keys():
                    if out in all_data[temp_user[0]].keys():
                        all_data[temp_user[0]][out] += (int)(temp_user[-1].split('M')[0])
                    else:
                        all_data[temp_user[0]][out] = (int)(temp_user[-1].split('M')[0])
                else:
                    all_data[temp_user[0]] = {}
                    all_data[temp_user[0]][out] = (int)(temp_user[-1].split('M')[0])

                # all_data.append([temp_user[0],out,temp_user[-1]])

    # print(all_data)
    # print(gpu_data)
    write_out = ""
    #write
    f= open(file_name,'w')
    write_out += (str(time.asctime( time.localtime(time.time()) ))+"\n")
    write_out += ("============================\n")
    write_out += ("Server Name:\t{}\n".format(machine_name))
    write_out += ("============================\n")
    write_out += ("CPU:"+str(out_cpu)+"%\tMEM:"+str(out_mem)+"%\n")
    write_out += ("============================\n")
    for ii in range(len(gpu_data)):
        for jj in range(len(gpu_data[ii])):
            if jj!=0:
                write_out += ('\t')
            write_out += (gpu_data[ii][jj])
        write_out += ('\n')
    write_out += ("============================\n")
    write_out += "{}\n".format(nvidia_version)
    write_out += ("============================\n")
    keys1 = list(all_data.keys())
    for ii in range(len(keys1)):
        write_out += (keys1[ii]+":\n")
        keys2 = list(all_data[keys1[ii]])
        for jj in range(len(keys2)):
            write_out += ('\t'+keys2[jj]+"--"+str(all_data[keys1[ii]][keys2[jj]])+"MiB\n")
        write_out += ("----------------------------\n")
    f.write(write_out)
    f.close()
    # print(write_out)
############

user = os.environ["user"]
passwd = os.environ["passwd"]

if __name__ == "__main__":
    #gen-key
    for server in config:
        print(server)
        try:
            if server in special_user.keys():
                temp_user = special_user[server]
            else:
                temp_user = user
            if server in special_port.keys():
                port = special_port[server]
            else:
                port = '22'

            os.system('timeout 5s ssh-keygen -f "/root/.ssh/known_hosts" -R "{}"'.format(config[server]))
            os.system('timeout 5s sshpass -p "{}" ssh -q -o StrictHostKeyChecking=no {}@{} -p {} &'.format(passwd,temp_user,config[server],port))
        except:
            print("ssh ken gen error for {}".format(server))
    try:
        os.system('timeout 5s ssh-keygen -f "/root/.ssh/known_hosts" -R "{}"'.format(remote_ip))
        os.system('timeout 5s sshpass -p "{}" ssh -q -o StrictHostKeyChecking=no {}@{} &'.format(passwd,temp_user,remote_ip))
    except:
        print("remote vps connect fail")
    while 1:
        for server in config:
            print("{} starting:".format(server))
            try:
                if server in special_user.keys():
                    temp_user = special_user[server]
                else:
                    temp_user = user

                if server in special_port.keys():
                    port = special_port[server]
                else:
                    port = '22'

                task1(config[server], temp_user, passwd, server, port)
                print("server {} task1 done".format(server))
            except:
                print(server + " can not connect.")
            time.sleep(1)
        try:
            p = os.popen('timeout 30s sshpass -p \"{}\" scp  -o StrictHostKeyChecking=no /src/*.txt {}@{}:{}'.format(passwd,user,remote_ip,remote_location))
            print("remote vps transport ok")
        except:
            print("remote vps transport fail")
        print(str(time.asctime( time.localtime(time.time()) )))

# def debug(server="509"):
#     if server in special_user.keys():
#         temp_user = special_user[server]
#     else:
#         temp_user = user
#     task1(config[server], temp_user, passwd, server)
