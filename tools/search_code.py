import os

WORKSPACE = "test_repo" #只搜索工作区，不然杂乱

def search_code(keyword): #要搜索的关键字(字符串)
    result = []
    for root, dirs, files in os.walk(WORKSPACE):  #从当前工作目录开始，遍历所有文件夹及其子文件夹。
        for file in files:
            if file.endswith(".py"):  #过滤代码文件
                path = os.path.join(root, file)
                try: #打开文件可能会遇到问题，用try不行就pass，不会崩程序
                    with open(path, "r", encoding="utf-8") as f: #打开文件常用格式
                        content = f.read()
                        if keyword in content:  #找代码文件中是否含有关键字
                            result.append(path)
                except:
                    pass
    return result