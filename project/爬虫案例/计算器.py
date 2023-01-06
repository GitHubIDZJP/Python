class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(0, 0)  # 设置窗口不可拉伸
        self.master.geometry('320x420')  # 设置主窗口的初始尺寸

        self.result = StringVar()  # 用于显示结果的可变文本
        self.equation = StringVar()  # 显示计算方程
        self.result.set(' ')
        self.equation.set('0')
        # 显示框
        self.show_result_eq = Label(self.master, bg='white', fg='black',
                                    font=('Arail', '16'), bd='0',
                                    textvariable=self.equation, anchor='se')
        self.show_result = Label(self.master, bg='white', fg='black',
                                 font=('Arail', '20'), bd='0',
                                 textvariable=self.result, anchor='se')
        # 按钮
        self.button_back = Button(self.master, text='<-', bg='DarkGray', command=self.back)  # 返回
        self.button_lbracket = Button(self.master, text='(', bg='DarkGray', command=lambda: self.getNum('('))  # 左括号
        self.button_rbracket = Button(self.master, text=')', bg='DarkGray', command=lambda: self.getNum(')'))  # 左括号
        self.button_division = Button(self.master, text='÷', bg='DarkGray', command=lambda: self.getNum('÷'))  # 除号
        # 7 8 9 4 5 6 1 2 3
        self.button_7 = Button(self.master, text='7', bg='DarkGray', command=lambda: self.getNum('7'))  # 7号
        self.button_8 = Button(self.master, text='8', bg='DarkGray', command=lambda: self.getNum('8'))  # 8号
        self.button_9 = Button(self.master, text='9', bg='DarkGray', command=lambda: self.getNum('9'))  # 9号
        self.button_multiplication = Button(self.master, text='*', bg='DarkGray',
                                            command=lambda: self.getNum('*'))  # 乘号
        # 按钮的command参数,是回调函数。lambda函数是为了可以传参数给回调函数
        self.button_4 = Button(self.master, text='4', bg='DarkGray', command=lambda: self.getNum('4'))  # 4号
        self.button_5 = Button(self.master, text='5', bg='DarkGray', command=lambda: self.getNum('5'))  # 5号
        self.button_6 = Button(self.master, text='6', bg='DarkGray', command=lambda: self.getNum('6'))  # 6号
        self.button_minus = Button(self.master, text='-', bg='DarkGray', command=lambda: self.getNum('-'))  # -号

        self.button_1 = Button(self.master, text='1', bg='DarkGray', command=lambda: self.getNum('1'))  # 1号
        self.button_2 = Button(self.master, text='2', bg='DarkGray', command=lambda: self.getNum('2'))  # 2号
        self.button_3 = Button(self.master, text='3', bg='DarkGray', command=lambda: self.getNum('3'))  # 3号
        self.button_plus = Button(self.master, text='+', bg='DarkGray', command=lambda: self.getNum('+'))  # +号
        # 控制按钮 0 .
        self.button_MC = Button(self.master, text='MC', bg='DarkGray', command=self.clear)  # MC
        self.button_0 = Button(self.master, text='0', bg='DarkGray', command=lambda: self.getNum('0'))  # 0
        self.button_dot = Button(self.master, text='.', bg='DarkGray', command=lambda: self.getNum('.'))  # .
        self.button_eq = Button(self.master, text='=', bg='DarkGray', command=self.run)  # =

        # Layout布局
        self.show_result_eq.place(x='10', y='10', width='300', height='50')
        self.show_result.place(x='10', y='60', width='300', height='50')

        self.button_back.place(x='10', y='150', width='60', height='40')
        self.button_lbracket.place(x='90', y='150', width='60', height='40')
        self.button_rbracket.place(x='170', y='150', width='60', height='40')
        self.button_division.place(x='250', y='150', width='60', height='40')
        self.button_7.place(x='10', y='205', width='60', height='40')
        self.button_8.place(x='90', y='205', width='60', height='40')
        self.button_9.place(x='170', y='205', width='60', height='40')
        self.button_multiplication.place(x='250', y='205', width='60', height='40')

        self.button_4.place(x='10', y='260', width='60', height='40')
        self.button_5.place(x='90', y='260', width='60', height='40')
        self.button_6.place(x='170', y='260', width='60', height='40')
        self.button_minus.place(x='250', y='260', width='60', height='40')

        self.button_1.place(x='10', y='315', width='60', height='40')
        self.button_2.place(x='90', y='315', width='60', height='40')
        self.button_3.place(x='170', y='315', width='60', height='40')
        self.button_plus.place(x='250', y='315', width='60', height='40')

        self.button_MC.place(x='10', y='370', width='60', height='40')
        self.button_0.place(x='90', y='370', width='60', height='40')
        self.button_dot.place(x='170', y='370', width='60', height='40')
        self.button_eq.place(x='250', y='370', width='60', height='40')

