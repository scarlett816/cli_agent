from tools.read_file import read_file
from tools.list_files import list_files
from tools.search_code import search_code

TOOLS = {
    "read_file": read_file,
    "list_files": list_files,
    "search_code": search_code
}

#把工具函数放到 TOOLS 字典里，让程序能够根据模型返回的“工具名”自动找到并调用对应的函数。