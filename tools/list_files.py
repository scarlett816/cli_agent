import os   #os 是一个标准库模块，提供很多和操作系统交互的功能

WORKSPACE = "test_repo"

def list_files():  

    files = []

    for root, dirs, filenames in os.walk(WORKSPACE): 
    #os.walk() 是一个生成器，它会从指定的WORKSPACE开始，一层层往下探索所有子文件夹
    #root：当前正在访问的文件夹的路径（字符串）
    #dirs：当前文件夹下所有子文件夹的名字列表（不含路径，只有名字）
    #filenames：当前文件夹下所有文件的名字列表（不含路径，只有名字）    
        for filename in filenames:
            full_path = os.path.join(root,filename) #os.path.join() 是专门用来智能拼接路径的函数
            files.append(full_path)

    return files