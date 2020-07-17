from config import *

#新增对应的网页数据文本，如index、publish、research:包括communication、compression、VAR、perception，以及data_codes(add_data函数) 几个ini文件
file_name = 'publish.ini'

#打印默认第一条内容，进行新增参考
print_demo(file_name,-1)

def add():
    add_context=\
        """<li class="content">
    Jianyi Wang, Mai Xu, Xin Deng, Congyong Chen, Yuhang Song, Liquan Shen, "MW-GAN: Multi-level Wavelet-based Generative Adversarial Network for Perceptual Quality Enhancement of Compressed Video" in European Conference on Computer Vision (ECCV 2020).
    <br/>|
    <a href=''>Paper</a>
    |
    <a href="">Code</a>
    |
</li>"""
    add_ini(file_name,add_context)
    print("ok")

# add()

####################
#修改
def change():
    add_context=\
        """<li><strong>[2020-07-02]</strong>
Our paper entitled "DeepGF: Glaucoma Forecast Using the Sequential Fundus Images"  has been accepted by Medical Image Computing and Computer Assisted Intervention Society (MICCAI'20). Congratulation, Liu Li and Xiaofei. 
</li>"""
    change_ini(file_name,add_context,-2)
    print("ok")

# change()

#删除
def delete():
    del_ini(file_name,-1)
    print("ok")
# delete()