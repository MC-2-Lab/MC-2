from config import *
import numpy as np

name = 'data' #news
c=config(name+'.ini')
ret = c.readAll()

keys_list = list(ret.keys())
data_list = []
for ii in range(len(ret.keys())):
    temp = ret[str(ii)]
    temp = temp.split('<strong>')[1].split("</strong>")[0]
    data_list.append(temp)
new_ret = {}
index_list = np.argsort(data_list)
for ii in range(len(ret.keys())):
    new_ret[str(ii)] = ret[(str)((int)(index_list[ii])) ]

c.writeConfig(new_ret)
print("ok")

pass