import easygui as e
import sys

while True:
    e.msgbox("嗨，欢迎进入小游戏")
    msg = "请问你希望学到什么知识呢？"
    title = "游戏小互动"
    choices = ["点赞", "投币", "加关注", "施主，记得三联哦"]
    choices = e.choicebox(msg, title, choices)

    e.msgbox("您的选择是：" + str(choices), "结果")
    msg = "你希望重新开始小游戏吗？"
    title = "请选择"
    if e.ccbox(msg, title):
        pass
    else:
        sys.exit(0)