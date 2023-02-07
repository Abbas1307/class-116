import cv2
img=cv2.imread("butterfly.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("display",gray_img)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
print(img)