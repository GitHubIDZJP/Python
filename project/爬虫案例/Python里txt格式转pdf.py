from fpdf import FPDF
import os
import  re
# import Workbook
import csv

i = 1
    # //以列表的方式打开所有txt文件的路径
# for filename in os.listdir("news.txt"):
for filename in os.listdir(fr'/Users/zoujunping/python采集资源/小说采集01/'):
    print("第%d开始" % i)
    pdf = FPDF()
    pdf.add_page()
    #写的绝对路径
    pdf.add_font('fireflysung', '', '/Users/zoujunping/Python/ResourcePack/freetype-gl/fonts/fireflysung.ttf', uni=True)

    pdf.set_font('fireflysung',size=12)
    pdf.output("改变格式.pdf", 'F')

    # //打开txt文本
    with open(fr'/Users/zoujunping/python采集资源/小说采集01/' + filename, encoding='utf-8') as f:
        ms = re.sub(r'.txt', '.pdf', filename)
        try:
            for line in f.readlines(): #毒区第一行
                str=line
                num=len(str)
                temp=45
                # print('文字123' + str)
                for j in range(0,num,temp):
                    if(j+temp<num):
                        data=str[j:j+temp]
                    else:
                        data=str[j:num]
                    pdf.cell(0, 5, data, ln=1)
                    print('数据:--->',data)
                f.close()

        except Exception as e:
             print(e)
        print('哈哈哈哈:---->',ms)
        maMsg = pdf.output("/Users/zoujunping/python采集资源/豆瓣排行榜/" + ms)

        # print('打印:' + maMsg.read)
    print("第%d完成" % i)
    i = i + 1
    print('执行完毕')
# if __name__ == '__main__':
#     txtToPdf()

