from config import *

#新增对应的网页数据文本，如index、publish、research:包括communication、compression、VAR、perception，以及data_codes几个ini文件
file_name = 'compression.ini'

#打印默认第一条内容，进行新增参考
print_demo(file_name)

def add():
    add_context=\
        """<li><strong>[2020-04-15]</strong>
    Dr. Xin Deng, our previous master student has obtained her PhD degree from Imperial College, and joined our group as a research associate professor. Welcome back, Dr Deng.
    </li>"""
    add_ini(file_name,add_context)
    print("ok")

# add()


