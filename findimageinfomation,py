import cv2
import numpy as np

# 讀取圖片
img = cv2.imread('20221021214894-801485155.png')

# 取得圖片大小
height, width, channels = img.shape

from PIL import Image

with Image.open('20221021214894-801485155.png') as img:
    print(img.info)
    
# 開啟圖片
im = Image.open("20221021214894-801485155.png")

# 讀取元數據
metadata = im.info.get('description')

# 列印元數據
print(metadata)

# 取得檔案大小
filesize = round((len(img.tobytes()) / 1024), 2)

# 取得圖片檔案資訊
params = [cv2.IMWRITE_PNG_COMPRESSION, 9]
_, encoded_img = cv2.imencode('.png', img, params)
metadata = round(len(encoded_img.tobytes()) / 1024, 2)

# 輸出結果
print(f"圖片大小：{width}x{height} pixels，色彩模式：{channels}，檔案大小：{filesize} KB，元資料大小：{metadata} KB")
