from ollama import chat

def calculator(expression):
    return eval(expression) #eval(expression) 是 Python 内置的函数，它会把字符串当作 Python 代码来执行，并返回计算结果。
                            #更好的做法是用 ast.literal_eval 或自己写解析器
user_input="25*4是多少"

response=chat(
    model='hermes3',
    messages=[         #复数，出现在 chat(...) 函数调用的参数里，是个列表。可以放多条消息，每条消息是个字典
        {
            'role':'system',
            'content':'''
你是一个AI助手。
如果用户需要计算，
请返回：
TOOL: calculator
ARGS: 数学表达式
'''
        },
        {'role':'user','content':user_input}  #键值对之间是冒号不是等号
    ]
)

reply=response['message']['content']

print("LLM回复: ")
print(reply)

if "TOOL: " in reply:
    #expression=reply.split("ARGS: ")[1].strip() 
    #从模型回复中切出 "ARGS: " 后面的内容，并去掉头尾空白，得到要计算的表达式字符串。
    #如果怎么写，会导致模型太“热情”，提前把答案也说了，使 eval 吃进了中文，报错
    for line in reply.splitlines(): #字符串的 .splitlines() 方法会按换行符把字符串切成一个列表，每个元素是原来的一行内容。
        if line.startswith("ARGS:"): #line.startswith("ARGS:") 检查这一行是不是 "ARGS: ..." 的形式。
            expression = line.split("ARGS:")[1].strip()
            result=calculator(expression)
            print("工具执行结果: ")
            print(result)
            break