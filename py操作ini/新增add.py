from config import *

#新增对应的网页数据文本，如 index、publish、research:包括communication、compression、VAR、perception，以及data_codes(add_data函数) 几个ini文件
file_name = 'VAR.ini'

#打印默认第一条内容，进行新增参考
item_index = -1
print_demo(file_name,item_index)

def add():
    add_context=\
        """<li class="content">
Li Yang, Mai Xu, Xin Deng, Bo Feng. "Spatial Attention-based Non-reference Perceptual Quality Prediction Network for Omnidirectional Images." IEEE International Conference on Multimedia and Expo (ICME'2021).
<br/>|
<a href='../pdf/imce21yl.pdf'>Download PDF</a> <a href='xxx'>Download Code</a> <a href='xxx'>Download Database</a>
|
</li>"""
    add_ini(file_name,add_context)
    # insert_ini(file_name,add_context,43) #插入到key=xx条
    print("ok")

# add()

####################
#修改
def change():
    add_context=\
        """<li><strong>[2020-12-28]</strong>
Our paper entitled "A Viewport-adaptive Rate Control Approach for Omnidirectional Video Coding" has been accepted by Data Compression Conference (DCC)'2021. Well done, Yichen.
</li>"""
    change_ini(file_name,add_context,item_index)
    print("ok")
    print_demo(file_name, item_index)
# change()

#删除
def delete():
    del_ini(file_name,item_index)
    print("ok")
# delete()