#jupyter编辑器用于Python人工智能
# 豆瓣网址

url='https://book.douban.com/chart?subcat=F&icn=index-topchart-fictio'
# 请求头：向对方服务器表明自己的身份，阐明自己的要求
#再请求头中把自己伪装成浏览器，而不是爬虫，这样服务器就不会设置阻碍
#人通过浏览器去查看数据，浏览器不会拒绝，因为网站有广告，可以盈利，但是爬虫不会去看广告
'''
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36

这里是包括了所有好几个浏览器的，比如:
Mozilla(火狐浏览器)
Chrome(谷歌浏览器)
Safari(浏览器)

下面的User-Agent值只需要复制上面的一个就行，我这里复制的是谷歌的Chrome/108.0.0.0
'User-Agent':'Chrome/108.0.0.0'



'''
import  openpyxl as op
import pandas as pd
import  requests
import xlwt
# 执行pip install BeautifulSoup4  安装时4一定要带上
from  bs4 import  BeautifulSoup
myHeaders = {
    'User-Agent':'Chrome/108.0.0.0'
}
result=requests.get(url,headers=myHeaders) #HTTP GET POST PUT
# 打印状态码:200则打印请求成功
print(result.status_code)
# 打印网页源代码-HTML
# print(result.text)
html=result.text
# 处理下载后的资源：如果是网页得再次做解析---->页面解析
# 初学者就用BeautifulSoup 容易上手
# xpath更加好用，但是需要熟悉语法
# soup=BeautifulSoup(html,'html.parser') #parser解析器
soup=BeautifulSoup(html,'lxml')#得pip install lxml安装:主要用于解析和提取HTML或者XML格式的数据,它不仅功能非常丰富,而且便于使用,可以利用XPath语法快速地定位特定的元素或节点
# print(soup)
'''
找符合条件的标签:
find  用的最多
find_all 用的最多 
findAll
findNext
findChild
find_all_next (
find_all_previous 
find_next 
find_next_sibling
find_next_siblings 
m find_parent 
'''

# fetch=soup.find('a') #寻找符合条件的a标签
# print(fetch)

#根据class找
#fetch=soup.find('a',class_='fleft') #下面那句跟这句一个意思。一般用这句因为简便，class是保留字，关键字，Python自己用了，变数class属性，class类，class_
# fetch=soup.find('a',attrs={'class':'fleft'}) #跟上面那句等价，要用其他属性时。直接替换里面的class值就行
#fetch=soup.findAll('a',attrs={'class':'fleft'}) #会把a标签的所有fleft元素找出来，以列表形式打印

#print(fetch)

#fetchAll=soup.findAll('a',attrs={'class':'fleft'})

#fetchAll=soup.findAll('p',attrs={'class':'subject-abstract color-gray'})#取书详情: 作者 时间 出版社 价格
# fetchAll=soup.findAll('p',attrs={'class':'subject-abstract color-gray'})  #class值写subject-abstract或者color-gray都行，class值中间有空格随意取一个代表class值就行
# fetchAll=soup.findAll('h2',attrs={'class':'clearfix'})#取所有书名
emptyArr = []
#最外层class值media
fecthAll_Arr=soup.findAll('li',class_='media')
for book in fecthAll_Arr:
#for打印标签元素
    title = book.find('a',class_='fleft').text.strip()
    author = book.find('p',class_='subject-abstract').text.strip()#.strip()去掉空格
    #位于div-span-a
    price = book.find('span',class_='buy-info')#.find('a').text.strip()
    if price:
        price=price.find('a').text
    else:
        price='页面未显示'
    emptyArr.append(title)
    print(title,author,price)
    print('*'*30)
print('数组长度:' + str(len(fecthAll_Arr)))
#'NoneType' object has no attribute 'find' 最后一本书出问题了,所以需要if去判断，当价格没显示的时候自己定义一个未显示页面


'''
soup.find打印:
<a class="fleft" href="https://book.douban.com/subject/36104107/">长安的荔枝</a>
soup.findAll打印：
<a class="fleft" href="https://book.douban.com/subject/36104107/">长安的荔枝</a>, 
<a class="fleft" href="https://book.douban.com/subject/35966120/">始于极限：女性主义往复书简</a>,
<a class="fleft" href="https://book.douban.com/subject/35819419/">可能性的艺术：比较政治学30讲</a>, 
<a class="fleft" href="https://book.douban.com/subject/36073906/">当我们不再理解世界</a>, 
<a class="fleft" href="https://book.douban.com/subject/36152943/">通俗小说</a>, 
<a class="fleft" href="https://book.douban.com/subject/36078195/">一个女人的故事：全新修订版</a>, 
<a class="fleft" href="https://book.douban.com/subject/35776315/">足利女童连续失踪事件</a>, 
<a class="fleft" href="https://book.douban.com/subject/36084340/">命运</a>,
<a class="fleft" href="https://book.douban.com/subject/36085236/">村上T：我喜爱的T恤们</a>, 
<a class="fleft" href="https://book.douban.com/subject/36069426/">大医·破晓篇</a>]
'''




