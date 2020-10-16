from config import *

#新增对应的网页数据文本，如index、publish、research:包括communication、compression、VAR、perception，以及data_codes(add_data函数) 几个ini文件
file_name = 'publish.ini'

#打印默认第一条内容，进行新增参考
item_index = -8
print_demo(file_name,item_index)

def add():
    add_context=\
        """<li><strong>[2020-10-11]</strong>
Xu, Mai, Lai Jiang, Chen Li, Zulin Wang, and Xiaoming Tao. "Viewport-based CNN: A Multi-task Approach for Assessing 360° Video Quality." IEEE transactions on pattern analysis and machine intelligence, 2020.
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
        """<li class="content">
Zhenyu Guan*, Qunliang Xing, Mai Xu, Ren Yang, Tie Liu and Zulin Wang, "MFQE 2.0: A New Approach for Multi-frame Quality Enhancement on Compressed Video" in IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI 2019), DOI: 10.1109/TPAMI.2019.2944806.
<br/>|
<a href='http://arxiv.org/abs/1902.09707'>Paper (latest on arXiv)</a>
|
<a href="https://github.com/RyanXingQL/MFQEv2.0">Code</a>
|
<a href="../pdf/TPAMI2019MFQE2.pdf">PDF (archived)</a>
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