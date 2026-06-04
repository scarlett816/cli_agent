from agent.agent_loop import run_agent

while True:  # 表示“永远执行下面的代码块”，直到程序内部主动退出。

    user_input = input("\n用户：")

    if user_input.lower() == "exit": #把用户输入的字符串全部转成小写字母。
        break

    run_agent(user_input)