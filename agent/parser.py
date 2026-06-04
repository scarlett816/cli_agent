#这段代码定义了一个函数，用来从大模型返回的文本中提取工具名称和参数。
#解析器，让程序看懂大模型要调用什么工具，解析大模型输出的文本
def parse_tool_call(text):

    lines = text.split("\n") #以换行符 \n 为界，把文本切成一个列表

    tool_name = None
    args = None

    for line in lines:  #依次将 lines 里的每个元素赋给 line
        if line.startswith("TOOL:"):
            tool_name = line.replace("TOOL:", "").strip()   
            #.replace(旧, 新) 把字符串中的 "TOOL:" 替换成空字符串 ""，即删掉它
            #.strip()去掉字符串首尾的所有空白字符（空格、制表符等）
        if line.startswith("ARGS:"):
            args = line.replace("ARGS:", "").strip()

    if tool_name:
        return tool_name, args

    return None, None