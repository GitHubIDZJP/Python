import requests
from lxml import etree
# from pprint import pprint

#这里下载不了 得开通VIP才行
#有Bug

#1 定义类ImageSpider
class ImageSpider(object):
    #初始化函数
    def __init__(self):
        '''准备url'''

        #发送请求获取响应数据函数、解析函数、主函数。
        self.firsr_url="https://www.51miz.com/so-sucai/1789243-13-0-0-default/p_{}/"
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }

    '''2----发送请求  获取响应'''
    def get_page(self,url):
        res=requests.get(url=url,headers=self.headers)
        html=res.content.decode('utf-8')
        return html


    '''3-----解析数据'''
    def parse_page(self,html):
        '''创建解析对象'''
        parse_html=etree.HTML(html)
        '''获取二级页面链接'''
        image_src_list=parse_html.xpath('//a[@class="image-box"]/@href')
        for image_src in image_src_list:
            print(image_src)
            html1=self.get_page(image_src)
            parse_html1=etree.HTML(html1)
            bimg_url = parse_html1.xpath('//img[@class="previewPic previewPic_0 previewPicSmall_0 show"]/@src')[0]
            filename = parse_html1.xpath('//div[@class="title fl lh28"]//h1[@class="iftip"]/text()')[0]
            # 把图片存储在文件夹中
            dirname = "图片1/" + filename + '.jpg'
            html2 = requests.get(url="http:"+bimg_url, headers=self.headers).content
            with open(dirname,'wb') as f:
                f.write(html2)
                print("%s下载成功"%filename)
    #  4 主函数
    def main(self):
        startPage=int(input("起始页:"))
        endPage=int(input("终止页:"))
        for page in range(startPage,endPage+1):
            url = self.firsr_url.format(page)
            html = self.get_page(url)
            #pprint(html)
            print(url,'aaaa')
            self.parse_page(html)
if __name__ == '__main__':
    imageSpider=ImageSpider()
    imageSpider.main()

