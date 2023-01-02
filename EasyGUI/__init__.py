import easygui

#a = easygui.buttonbox("按钮在下面", "标题", ["按钮1", "按钮2", "按钮3", "按钮4", "按钮5"])

#居于左边速排按钮(列)
# b = easygui.choicebox("选择↓", "标题", ["选择1号", "选择2号", "选择3号", "选择4号", "选择5号"])

#类似iOS的alterview:里面是输入框
# c = easygui.enterbox("文本框在我下面", "标题")  # 将你输入的内容存放在a这个变量

#类似iOS的alterview:里面是输入框:多了个placeHolder:placeHolder
d = easygui.enterbox("文本框在我下面", "标题", "默认输出")  # 将你输入的内容存放在a这个变量里