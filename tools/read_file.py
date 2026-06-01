import os  #os 是一个标准库模块，提供很多和操作系统交互的功能

WORKSPACE = "test_repo"

def read_file(path):
    full_path = os.path.join(WORKSPACE,path)  #只开工作区里面的
    with open(full_path,"r",encoding="UTF-8") as f: #以只读模式和UTF-8编码安全打开path对应的文件
                                               #并将文件对象赋给变量f，离开with块时自动关闭文件
        content=f.read()    #读取文件f的全部文本内容，存入字符串变量content
    return content