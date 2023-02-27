import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # 创建一个用于显示计算结果的文本框
        self.result_display = tk.Entry(master, width=30)
        self.result_display.grid(row=0, column=0, columnspan=4)

        # 创建按钮
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+"
        ]

        # 将按键添加到GUI中
        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(master, text=button_text, width=7, height=3, command=lambda value=button_text: self.button_click(value))
            button.grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

    # 处理按钮点击事件
    def button_click(self, value):
        if value == "C":
            # 清空计算结果
            self.result_display.delete(0, tk.END)
        elif value == "=":
            # 执行计算操作
            try:
                result = eval(self.result_display.get())
                self.result_display.delete(0, tk.END)
                self.result_display.insert(0, result)
            except:
                self.result_display.delete(0, tk.END)
                self.result_display.insert(0, "Error")
        else:
            # 在文本框中添加按键点击值
            current_value = self.result_display.get()
            self.result_display.delete(0, tk.END)
            self.result_display.insert(0, current_value + value)

# 创建主窗口
root = tk.Tk()

# 创建计算器实例
calculator = Calculator(root)

# 运行窗口
root.mainloop()

