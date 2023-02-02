import re

content = "I have 100 dogs and 200 cats"
res = re.findall('\d+',content)
print(res)
#['100', '200']   寻找所有数字
#返回的是返回一个列表或元组，所以也不需要group来捕获，如果需要一个一个捕获，用res[0] 或res[1]来一个一个显示捕获的值。

res = re.search('\d+',content) #只会查找第一个数字则直接打印
print(res.group())
#100 查询数字

#re.sub()函数
# 检索和替换
# 用于替换字符串中的匹配项

#
'''
re.sub(pattern, repl, string, count=0, flags=0)
参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配
'''
res = re.sub('\d+','300',content)
print(res)
#原句：  I have 100 dogs and 200 cats
#替换后: I have 300 dogs and 300 cats

# re.compile()函数
# 匹配符封装一下 比较常用
#表达式: re.compile(pattern[, flags])

'''
参数：
pattern : 一个字符串形式的正则表达式

flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：

re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释
'''
res = re.match('^I.*?(\d+)(.*?)and(.*?)$',content,re.S)
print('compile****:',res.group())
print('compile****:',res.groups())  #groups()获取匹配后的字符串
'''
^I.*?(\d+)(.*?)and(.*?)$
^I:从字符I开始检索匹配
.*?：检索所有
\d+ 匹配任意数字，等价于 [0-9]
(.*?) 检索所有 () 匹配括号里面的内容
.代表所有的单个字符，除了 n r
？和{0,1} 一个样，匹配 ？前面 0 次或 1 次
* 和 {0,} 一个样，匹配 * 前面的 0 次或多次。 比如 zo* 能匹配“z”、“zo”以及“zoo”
() 匹配括号里面的内容
I have 100 dogs and 200 cats
('100', ' dogs ', ' 200 cats')
'''