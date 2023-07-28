import os
import shutil
import tkinter as tk
from PIL import Image
import imagehash

# 比較圖片相似性的函數
def is_similar(img1_path, img2_path):
    # 使用imagehash庫生成圖片的哈希值
    hash0 = imagehash.average_hash(Image.open(img1_path)) 
    hash1 = imagehash.average_hash(Image.open(img2_path)) 
    print(hash0)
    print(hash1)
    # 如果兩圖片哈希值相同，則視為相同圖片
    return hash0 == hash1

# 處理圖片的函數
def handle_images(target_path):
    # 遍歷目標路徑下的所有子目錄
    for root, dirs, files in os.walk(target_path):
        # 檢查當前目錄是否為子目錄
        if root != target_path:
            # 遍歷當前目錄中的所有檔案
            for file in files:
                # 建立當前檔案的完整路徑
                file_path = os.path.join(root, file)
                # 檢查在目標目錄中是否已存在相同名稱的檔案
                target_file_path = os.path.join(target_path, file)
                if os.path.exists(target_file_path):
                    # 如果找到相同的檔案，並且兩者的內容也相同
                    if is_similar(file_path, target_file_path):
                        # 刪除當前檔案
                        os.remove(file_path)
                else:
                    # 將當前檔案移動到目標目錄
                    shutil.move(file_path, target_file_path)
        # 刪除子目錄及其所有內容
        shutil.rmtree(root)

# 圖形介面的功能
def start_gui():
    # 創建一個新的Tk根部件
    root = tk.Tk()
    root.title('Handle Images')

    # 創建一個新的Entry部件
    entry = tk.Entry(root, width=50)
    entry.pack()

    # 創建一個新的Button部件
    button = tk.Button(root, text="Start", command=lambda: handle_images(entry.get()))
    button.pack()

    # 開始Tk的事件迴圈
    root.mainloop()

# 開始圖形介面
start_gui()
