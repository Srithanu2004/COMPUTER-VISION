import cv2
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)
cv2.imwrite("edges.jpg", edges) 
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)  
cv2.destroyAllWindows()  
