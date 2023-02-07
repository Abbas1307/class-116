import cv2
img=cv2.imread("poster.jpg")

rocket=img[120:360,400:500]
img[0:240,500:600]=rocket
text="hello how are you"
cv2.putText(img,text,(20,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(98,57,25))
cv2.imshow("display",img)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
print(img)

