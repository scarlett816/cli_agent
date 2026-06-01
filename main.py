from ollama import chat

from agent.agent_loop import SYSTEM_PROMPT
from agent.parser import parse_tool_call

from agent.tool_registry import TOOLS

user_input = input("用户：")

response = chat(
    model="hermes3",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)

reply = response["message"]["content"]

print("\nHermes输出：")
print(reply)

tool_name, args = parse_tool_call(reply)

if tool_name:  #如果有tool_name时执行
    tool = TOOLS[tool_name]
    if args:
        result = tool(args)   #result=函数(参数)
    else:
        result = tool()   #可能会存在没有参数的情形，这个时候就采用默认值

    print("\n工具结果：") #要调用工具才会print这两个
    print(result)