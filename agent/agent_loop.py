from ollama import chat

from agent.parser import parse_tool_call
from agent.tool_registry import TOOLS

SYSTEM_PROMPT = """
你是一个代码分析Agent。
你拥有以下工具：

1. read_file(path)
作用：读取文件内容
2. list_files()
作用：列出所有文件
3. search_code(keyword)
作用：搜索代码关键字

重要规则：

如果用户问：
login函数在哪里
你必须调用：
TOOL: search_code
ARGS: login

如果用户要求读取文件：
你必须调用：
TOOL: read_file
ARGS: 文件名

调用工具时：
只能输出：
TOOL: 工具名
ARGS: 参数
不要解释。
不要聊天。
不要说“请提供文件”。
不要说“我需要更多信息”。

如果已经获得足够信息回答问题：

直接输出最终答案。
"""

MAX_STEPS = 5

def run_agent(user_input):

    messages = [
        {"role": "system","content": SYSTEM_PROMPT},
        {"role": "user","content": user_input}
    ]

    for step in range(MAX_STEPS):

        print("\n=================") #换行后再在屏幕上打出分割线
        print(f"Step {step + 1}") 
        #f-string可以在字符串里直接嵌入变量或表达式，用大括号{}包起来，会变成实际的值。
        print("=================")

        response = chat(model="hermes3",messages=messages)

        reply = response["message"]["content"]

        print("\nHermes输出：")
        print(reply)

        tool_name, args = parse_tool_call(reply)

        # 没有工具调用
        if tool_name is None:

            print("\n最终答案：")
            print(reply)

            return reply

        # 找工具
        tool = TOOLS.get(tool_name)

        if tool is None:

            print("未知工具")
            return

        # 执行工具
        try:

            if args:
                tool_result = tool(args)
            else:
                tool_result = tool()

        except Exception as e:

            tool_result = f"工具执行失败: {e}"

        print("\n工具结果：")
        print(tool_result)

        messages.append({"role": "assistant","content": reply})
        # 保存LLM回复。
        # 把模型刚才的输出作为助手的发言，添加到 messages 列表末尾。
        # 这样模型在下一步就能看到自己说过什么。

        messages.append({"role": "user","content":f"工具结果:\n{tool_result}"})
        # Observation
        # 把工具执行的结果包装成一条“用户”消息，也追加到 messages 末尾。
        # Ollama 的 API 规定，工具的输出必须假装是用户说的，这样模型才会阅读它。

    print("达到最大推理步数")

    return None