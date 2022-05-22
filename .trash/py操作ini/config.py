import json,os
class config():
    def __init__(self,fileName):
        self.fileName = fileName
        pass
    def readConfig(self,key):
        #if self.fileName in os.listdir():
        try:
            f = open(self.fileName,'r') 
            data = json.loads(f.read())  
            value = data.get(key)       
            f.close()                  
            return value                
        except:
            return 0
        pass
    def readAll(self):
        #if self.fileName in os.listdir():
        try:
            f = open(self.fileName,'r') 
            data = json.loads(f.read())       
            f.close()                  
            return data                
        except:
            return 0            
    def writeConfig(self,dict):
        f = open(self.fileName,'w')     
        data = json.dumps(dict,indent=1) #indent=1可视化显示，不然会一行全放   
        f.write(data)                   
        f.close()                  

####################
#管理相关函数
def clear_ini(path):
    c=config(path)
    c.writeConfig({})
    return "OK"

#按序号添加
def add_ini(path,data):
    c=config(path)
    ret = c.readAll()
    ret[(str)(len(ret.keys()))] = data
    c.writeConfig(ret)
    return "OK"

def insert_ini(path,data,ii):
    c=config(path)
    ret = c.readAll()
    all_ii = len(ret.keys())
    for temp_ii in range(all_ii,ii,-1):
        ret[(str)(temp_ii)] = ret[(str)(temp_ii-1)]
    ret[(str)(ii)] = data
    c.writeConfig(ret)
    return "OK"


def change_ini(path,data,ii):
    c = config(path)
    ret = c.readAll()
    ret[list(ret.keys())[ii]] = data
    c.writeConfig(ret)
    return "OK"

def del_ini(path,ii):
    c = config(path)
    ret = c.readAll()
    ret.pop(list(ret.keys())[ii])
    c.writeConfig(ret)
    return "OK"


# 打印一个
def print_demo(path,ii=0):
    c=config(path)
    ret = c.readAll()
    if len(ret.keys())>0:
        demo = ret[list(ret.keys())[ii]]
        print(demo)
        return demo
    else:
        return None
    
