import cv2
import numpy as np

# 打开图像文件
def open_image(file_path):
    img = cv2.imread(file_path)
    return img

# 显示图像
def show_image(img, window_name='Image'):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 存储处理后的图像
def save_image(img, file_path):
    cv2.imwrite(file_path, img)

# 灰度化
def grayscale(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

# 像素值化
def thresholding(img, threshold_value):
    ret, thresh_img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
    return thresh_img

# 3x3 均值滤波
def mean_filter(img):
    kernel = np.ones((3, 3), np.float32) / 9
    filtered_img = cv2.filter2D(img, -1, kernel)
    return filtered_img

# 3x3 中值滤波
def median_filter(img):
    filtered_img = cv2.medianBlur(img, 3)
    return filtered_img

# 拉普拉斯4 领域锐化
def laplacian_sharpen(img):
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], np.float32)
    sharpened_img = cv2.filter2D(img, -1, kernel)
    return sharpened_img

# 边缘检测
def edge_detection(img):
    edges = cv2.Canny(img, 100, 200)
    return edges

# 直方图计算与显示
def histogram(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    cv2.imshow('Histogram', hist)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 示例代码
if __name__ == '__main__':
    # 打开图像文件
    img_path = './img/hero_show_1.png'
    img = open_image(img_path)

    # 显示原始图像
    show_image(img, 'Original Image')

    # 灰度化
    gray_img = grayscale(img)
    show_image(gray_img, 'Grayscale Image')

    # 像素值化
    threshold_value = 127
    thresh_img = thresholding(gray_img, threshold_value)
    show_image(thresh_img, 'Thresholded Image')

    # 3x3 均值滤波
    mean_filtered_img = mean_filter(img)
    show_image(mean_filtered_img, 'Mean Filtered Image')

    # 3x3 中值滤波
    median_filtered_img = median_filter(img)
    show_image(median_filtered_img, 'Median Filtered Image')

    # 拉普拉斯4 领域锐化
    sharpened_img = laplacian_sharpen(img)
    show_image(sharpened_img, 'Sharpened Image')

    # 边缘

