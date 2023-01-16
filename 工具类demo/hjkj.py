import cv2


#dwgpic2.png
#豆瓣排行榜
imgfile = input("请输入图片名：")
txtfile = input("请输入存储文本文件名：")
img = cv2.imread(r"/Users/zoujunping/python采集资源"+imgfile,cv2) #cv2.IMREAD_GRAYSCALE)
print("图像的形状,返回一个图像的(行数,列数,通道数):",img.shape)
print("图像的像素数目:",img.size)
print("图像的数据类型:",img.dtype)
#----------------------------------------------------------------------------
"""
In windows the COLOR->GRAYSCALE: Y = 0.299R+0.587G+0.114B 测试是否三个通道的值是相同的。
某些图像三通道值相同，可以直接读灰度图来代替读单一通道。
"""
# sum = 0
# ans = 0
# for i in range(562):
#     for j in range(715):
#         if not(img[i][j][0] == img[i][j][1] and img[i][j][1] == img[i][j][2]):
#             sum += 1
#         else:
#             ans += 1
# print(ans)
# print(sum)
#-----------------------------------------------------------------------------
"""
将图片数据写入txt文件
格式:
    基础信息
    行号:
        像素值
    行号:
        像素值
    ......
"""
fname = open(r"/Users/zoujunping/python采集资源/豆瓣排行榜/dwgpic2.png"+txtfile,'w')
fname.write("图像的形状,返回一个图像的(行数,列数,通道数):"+str(img.shape)+'\n')#----1
fname.write("图像的像素数目:"+str(img.size)+'\n')#----2
fname.write("图像的数据类型:"+str(img.dtype)+'\n')#----3
Xlenth = img.shape[1]#图片列数
Ylenth = img.shape[0]#图片行数
a = 1#----4
for i in range(Ylenth):
    fname.write(str(a) + ':'+'\n')#----5
    for j in range(Xlenth):
        fname.write(str(img[i][j])+' ')
    a += 1#----6
    fname.write('\n')
fname.close()
#---------------------------------------------------------------------------
"""
将txt文件中的数据读取进blist
并显示为"test"图片框进行测试。
注意进行测试前需要注释掉数据写入模块
中标记的六行代码，要不然读取会出错误。
"""
# blist = []
# split_char = ' '
# with open('C:/Users/Jake/Desktop/test01/'+txtfile, 'r') as bf:
#     blist = [b.strip().split(split_char) for b in bf]
#
##从txt文件读入进来的值类型是char需要转换为int
# for i in range(Ylenth):
#     for j in range(Xlenth):
#         blist[i][j] = int(blist[i][j])
#
# tlist = numpy.array(blist)
# plt.figure()
# plt.imshow(tlist)
# plt.axis('off') # 不显示坐标轴
# pylab.show()
#------------------------------------------------------------------------------
"""
将图片显示在'image'图片框
"""
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#----------------------------------------------------------------------