import time
from loading_bar import Context
import requests

def control_block(choosing_list):
    choice_list = set([str(n) for n in range(len(choosing_list))])
    while True:
        choice = input("请输入选择：")
        if choice in choice_list:
            print("所选择选项为：", '【'+choosing_list[int(choice)]+'】')
            return int(choice)
        elif choice == 'quit':
            with Context(text="正在退出...", finish_text='退出成功!'):
                time.sleep(2)
            break
        else:
            print("无效输入！请重新输入选择")
    return None



