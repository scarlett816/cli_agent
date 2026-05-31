from ollama import chat

response=chat(
    model='hermes3',
    messages=[         #复数，出现在 chat(...) 函数调用的参数里，是个列表。可以放多条消息，每条消息是个字典
        {
            'role':'user','content':'你好'
        }
    ]
)

print(response['message']['content'])  #单数，模型返回的“最新一条回复”