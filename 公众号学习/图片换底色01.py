import cv2

# 打开图像文件
img = cv2.imread('girl.png')

# 显示图像
cv2.imshow('Original Image', img)

# 转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 显示灰度图像
cv2.imshow('Grayscale Image', gray_img)

# 二值化处理
thresh = 100  # 阈值可调
max_value = 255
ret, bin_img = cv2.threshold(gray_img, thresh, max_value, cv2.THRESH_BINARY)

# 显示二值化图像
cv2.imshow('Binary Image', bin_img)

# 3x3均值滤波
kernel = (3, 3)
avg_img = cv2.blur(img, kernel)

# 显示3x3均值滤波后的图像
cv2.imshow('3x3 Averaging Image', avg_img)

# 3x3均值滤波
kernel = (3, 3)
avg_img = cv2.blur(img, kernel)

# 显示3x3均值滤波后的图像
cv2.imshow('3x3 Averaging Image', avg_img)

# 拉普拉斯4领域锐化
laplacian_img = cv2.Laplacian(gray_img, cv2.CV_64F, ksize=3)

# 显示拉普拉斯锐化后的图像
cv2.imshow('Laplacian Image', laplacian_img)

# 边缘检测
canny_img = cv2.Canny(gray_img, 100, 200)

# 显示边缘检测后的图像
cv2.imshow('Canny Image', canny_img)

# 计算图像的直方图
hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

# 显示图像的直方图
import matplotlib.pyplot as plt
plt.plot(hist)

# 等待用户按下任意按键
cv2.waitKey(0)

# 保存处理后的图像
cv2.imwrite('processed_image.jpg', canny_img)

# 关闭所有窗口
cv2.destroyAllWindows()
