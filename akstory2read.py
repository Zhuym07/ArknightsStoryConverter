import re
import os
import tkinter as tk
import pyperclip

def parse_dialogue(text):
    # 匹配人物名称和对话内容
    pattern = r'\[name="(.+?)"\](.+?)\n'
    matches = re.findall(pattern, text)
    
    # 输出人物对话
    result = ""
    for match in matches:
        name, dialogue = match
        result += f'{name}：{dialogue.strip()}\n'
    return result

def button_click():
    # 获取用户输入内容
    text = input_text.get("1.0", "end-1c")
    # 解析对话内容并展示在GUI界面下方
    result = parse_dialogue(text)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)
    # 将内容写入剪贴板
    pyperclip.copy(text)
    
# 创建GUI界面
root = tk.Tk()
root.geometry("400x400")
root.title("明日方舟剧情文本转换器")

# 创建文本框

input_text = tk.Text(root, height=12)
output_text = tk.Text(root, height=12)
input_text.pack()
output_text.pack()

# 创建确认按钮
button = tk.Button(root, text="转换", command=button_click, padx=10, pady=10)
button.pack()

# 运行GUI界面
root.mainloop()
