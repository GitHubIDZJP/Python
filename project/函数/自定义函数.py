


#自定义 len() 函数
def my_len(str):
    length = 0
    for c in str:
       length = length + 1
    return length
#调用自定义的 my_len() 函数
length = my_len("http://c.biancheng.net/python/")
print(length) #30

#再次调用 my_len() 函数
length = my_len("http://c.biancheng.net/shell/")
print(length) #29

'''
def 函数名(参数列表):
    //实现特定功能的多行代码
    :return 返回值
'''

#定义个空函数，没有实际意义
def pass_dis():
    pass
#定义一个比较字符串大小的函数
def str_max(str1,str2):
    str = str1 if str1 > str2 else str2
    return str


a = 100
b = 200
v = str_max(a,b)
print(v)

# 比较大小：return 可以直接返回一个表达式
def str_max(str1,str2):
    return str1 if str1 > str2 else str2


#定义函数时，这里的函数参数 obj 就是形式参数
def demo(obj):
    print(obj)

    # 实际参数：在调用函数时，函数名后面括号中的参数称为实际参数，也就是函数的调用者给函数的参数。例如
    a = "C语言中文网"
    # 调用已经定义好的 demo 函数，此时传入的函数参数 a 就是实际参数
    demo(a)

# 实参是如何传递给形参
def demo(obj) :
    obj += obj
    print("形参值为：",obj)#C语言中文网C语言中文网
print("-------值传递-----")
a = "C语言中文网"
print("a的值为：",a)
demo(a)
print("实参值为：",a)
print("-----引用传递-----")
a = [1,2,3]#数组
print("a的值为：",a)#[1, 2, 3, 1, 2, 3]
demo(a)
print("实参值为：",a)#[1, 2, 3, 1, 2, 3]

#位置参数:实参和形参数量必须一致

def girth(width , height):
    return 2 * (width + height)
#调用函数时，必须传递 2 个参数，否则会引发错误
print(girth(3))
#只传了一个参数:
'''
girth() missing 1 required positional argument: 'height'
具体是指 girth() 函数缺少一个必要的 height 参数
'''

print(girth(3,2,4))
#传入3参数:多传了一个参数:
'''
errMsg: girth() takes 2 positional arguments but 3 were given
，girth() 函数本只需要 2 个参数，但是却传入了 3 个参数
'''


#设计一个求梯形面积的函数，并利用此函数求上底为 4cm，下底为 3cm，高为 5cm 的梯形的面积。但如果交互高和下低参数的传入位置，计算结果将导致错误
def area(upper_base,lower_bottom,height):
    return (upper_base+lower_bottom)*height/2
print("正确结果为：",area(4,3,5))
print("错误结果为：",area(4,5,3))

'''
run:

正确结果为： 17.5
错误结果为： 13.5
'''



#函数关键字参数及用法

