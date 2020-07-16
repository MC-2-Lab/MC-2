from config import *

#新增对应的网页数据文本，如index、publish、research:包括communication、compression、VAR、perception，以及data_codes(add_data函数) 几个ini文件
file_name = 'data_codes.ini'

#打印默认第一条内容，进行新增参考
print_demo(file_name,-1)

def add():
    add_context=\
        """<li class="content">
    Liu Li, Xiaofei Wang, Mai Xu, Ximeng Chen, Hanruo Liu: DeepGF: Glaucoma Forecast Using the Sequential Fundus Images, Medical Image Computing and Computer Assisted Intervention Society (MICCAI), 2020.
    <br/>|
    <a href='../pdf/MICCAI2020DeepGF.pdf'>Download PDF</a>
    |
    <a href="https://github.com/XiaofeiWang2018/DeepGF">Download Database</a>
    |
</li>"""
    add_ini(file_name,add_context)
    print("ok")

# add()

####################
#修改
def change():
    add_context=\
        """<li class="content">
    Liu Li, Xiaofei Wang, Mai Xu, Ximeng Chen, Hanruo Liu: DeepGF: Glaucoma Forecast Using the Sequential Fundus Images, Medical Image Computing and Computer Assisted Intervention Society (MICCAI), 2020.
    <br/>|
    <a href='../pdf/MICCAI2020DeepGF.pdf'>Download PDF</a>
    |
    <a href="https://github.com/XiaofeiWang2018/DeepGF">Download Database</a>
    |
</li>"""
    change_ini(file_name,add_context,-1)
    print("ok")

# change()

#删除
def delete():
    del_ini(file_name,-1)
    print("ok")
# delete()