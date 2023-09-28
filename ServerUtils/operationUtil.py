import subprocess  # 导入 subprocess 模块，用于执行系统命令
import webbrowser  # 导入 webbrowser 模块，用于打开网页
import numpy as np
import keyboard


# 定义函数 read_config，接收一个文件路径参数 path，用于读取配置文件
def read_config(path):
    # 打开文件，使用 utf-8 编码
    with open(path, 'r', encoding='utf-8') as f:
        # 读取文件内容
        content = f.read()
    # 定义一个空字典，用于存储操作及其对应的参数
    operation_dict = dict()
    # 遍历每个操作，以分号分割
    for operation in content.split(";"):
        # 将操作名和参数以等号分割，并添加到字典中
        operation_dict[operation.split("=")[0]] = operation.split("=")[1]
    # 返回操作字典
    return operation_dict


# 定义函数 do_operation，接收一个命令字符串参数 command_str，用于执行具体的操作
def do_operation(command_str):
    # 从命令字符串中分离出操作和参数
    command_act = str(command_str).split(",")[0]

    # 如果操作是 shutdown，则执行关机命令
    if command_act == "stop":
        # subprocess.run(["shutdown", "/s"])
        print("stop!")
        keyboard.press_and_release('space')
    # 如果操作是 openurl，则打开指定的网页
    elif command_act == "go":
        # webbrowser.open(command_para)
        print("go!")
    # 如果操作是 execute，则执行指定的程序，并传入参数
    elif command_act == "execute":

        command_para = str(command_str).split(",")[1]
        command_args = str(command_str).split(",")[2:]

        # print(np.hstack(([command_para], command_args)))
        # subprocess.Popen(np.hstack(([command_para], command_args)))
        print(command_str)
        print(command_para)
        print(command_args)

# 如果该模块是主模块，则执行以下代码
if __name__ == '__main__':
    # 调用 read_config 函数读取配置文件，获取操作字典
    operations = read_config("./ActionSet.txt")
    # 调用 do_operation 函数执行第一个操作
    do_operation(operations["go"])
