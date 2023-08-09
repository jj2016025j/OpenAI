import cv2
import os

# 載入人臉檢測器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

source_path = r"C:\Users\User\Desktop\tablecloth\other\processed"

image_files = os.listdir(source_path)

# 逐一處理每一張圖片
for file_name in image_files:
    # 讀取圖片檔案
    image_path = os.path.join(source_path, file_name)
    image = cv2.imread(image_path)

    # 將圖片轉為灰階
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 檢測人臉
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # 如果有偵測到人臉，就顯示圖片
    if len(faces) > 0:
        # 繪製人臉矩形框
        for (x, y, w, h) in faces:
                mosaic = image[y:y+h, x:x+w]   # 馬賽克區域
                level = 10                       # 馬賽克程度
                mh = int(h/level)            # 根據馬賽克程度縮小的高度
                mw = int(w/level)            # 根據馬賽克程度縮小的寬度
                mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR) # 先縮小
                mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)  # 然後放大
                image[y:y+h, x:x+w] = mosaic   # 將指定區域換成馬賽克區域

        # 顯示圖片
        cv2.imshow('Detected Faces', image)
        cv2.waitKey(0)

# 關閉視窗
cv2.destroyAllWindows() 