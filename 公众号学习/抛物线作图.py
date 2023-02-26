'''

请输入初速度v:  10
请输入绘制行数h:  10


'''

from matplotlib import pyplot as plt


def pwx(v, h):
    yx = []  # 定义一列表
    # 物体从高处位置为点50米的地方
    g = 9.8
    height = 5  # 这个是常量每运行一行为5米
    hh = 5*v  # 总高度
    for i in range(h):
        y = height
        height = y+5
        x = int(v*(2*y*(1/9.8))**0.5)
        yx.append((hh, x))
        hh -= 5
    return yx


def huaxian(yx):
    plt.title("Parabolic trajectory curve")
    plt.xlabel("x")
    plt.ylabel("y")
    for y, x in yx:
        plt.plot(x, y, "*")
        print(y, x)
    plt.show()


def main():
    v = int(input("请输入初速度v:  "))
    h = int(input("请输入绘制行数h:  "))
    yx = pwx(v, h)
    huaxian(yx)


if __name__ == "__main__":
    main()