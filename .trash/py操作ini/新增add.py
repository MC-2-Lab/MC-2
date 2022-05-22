from config import *

#新增对应的网页数据文本，如 1)index、2)publish、3)research:包括 communication、compression、VAR、perception，以及data_codes(add_data函数) 几个ini文件
file_name = 'compression.ini'

#打印默认第一条内容，进行新增参考
item_index = -1
print_demo(file_name,item_index)

def add():
    add_context=\
        """<li class="content">
Tianyi Li, Mai Xu*, Runzhi Tang, Ying Chen, Qunliang Xing. "DeepQTMT: A Deep Learning Approach for Fast QTMT-based CU Partition of Intra-mode VVC." IEEE Transactions on Image Processing (TIP'2021).
<br/>|
<a href='../pdf/TIP2021DeepQTMT.pdf'>Download PDF</a>
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
        """<li class="content">
Xin Deng, Wenzhe Yang, Ren Yang, Mai Xu, Enpeng Liu, Qianhan Feng, Radu Timofte. "Deep Homography for Efficient Stereo Image Compression."  Conference on Computer Vision and Pattern Recognition (CVPR2021).
<br/>|
<a href='../pdf/TIP2021DeepQTMT.pdf'>Download PDF</a>
|
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