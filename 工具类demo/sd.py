import cv2
#读取图片，该图在此代码的同级目录下
bgr_img = cv2.imread("/Users/zoujunping/python采集资源/豆瓣排行榜/dwgpic2.png")
#二化值
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
th, binary = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU)
#获取轮廓的点集
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#取最大的边缘轮廓点集
contours = max(contours, key=cv2.contourArea)

#求取轮廓的矩
M = cv2.moments(contours)

#画出轮廓
cv2.drawContours(bgr_img, contours, -1, (0, 0, 255), 3)
bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]

#在图片上画出矩形边框
for bbox in bounding_boxes:
    [x, y, w, h] = bbox
    cv2.rectangle(bgr_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#通过矩来计算轮廓的中心坐标
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(f"({cx},{cy})")
cv2.imshow("name", bgr_img)
cv2.waitKey(0)
# print('坐标点:'cx)
for i in cx:
    print(i)