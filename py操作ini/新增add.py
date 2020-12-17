from config import *

#新增对应的网页数据文本，如index、publish、research:包括communication、compression、VAR、perception，以及data_codes(add_data函数) 几个ini文件
file_name = 'publish.ini'

#打印默认第一条内容，进行新增参考
item_index = -1
print_demo(file_name,item_index)

def add():
    add_context=\
        """<li class="content">
Xiaofei Wang, Mai Xu, Jicong Zhang, Lai Jiang, Liu Li. "Deep Multi-Task Learning for Diabetic Retinopathy Grading in Fundus Images." AAAI Conference on Artificial Intelligence (AAAI, 2021).
<br/>|
<a href='../pdf/xxxx.pdf'>Download PDF</a>
|
</li>"""
    add_ini(file_name,add_context)
    print("ok")

# add()

####################
#修改
def change():
    add_context=\
        """<li><strong>[2020-12-05]</strong>
Our paper entitled "Deep Multi-Task Learning for Diabetic Retinopathy Grading in Fundus Images" has been accepted by AAAI'2021. Well done, Xiaofei.
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