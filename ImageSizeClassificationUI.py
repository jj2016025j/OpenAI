import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image

def classify_images(input_folder, output_folder):
    # 檢查輸入的文件夾是否存在
    if not os.path.exists(input_folder):
        print("Error: input folder does not exist")
        return

    # 檢查輸出的文件夾是否存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍歷文件夾中的所有文件
    for filename in os.listdir(input_folder):
        # 檢查文件是否為圖像格式
        if not filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            continue

        # 加載圖像
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # 確定圖像的大小並分類
        width, height = img.size
        if width > 2000 or height > 2000:
            output_path = os.path.join(output_folder, 'large', filename)
        else:
            output_path = os.path.join(output_folder, 'small', filename)

        # 將圖像保存到相應的文件夾中
        img.save(output_path)

    print("Image classification complete.")



class App:
    def __init__(self, master):
        self.master = master
        master.title("圖片分類")

        self.src_path = ""
        self.dest_path = ""

        self.src_button = tk.Button(master, text="選擇來源路徑", command=self.select_src_path)
        self.src_button.pack()

        self.dest_button = tk.Button(master, text="選擇輸出路徑", command=self.select_dest_path)
        self.dest_button.pack()

        self.confirm_button = tk.Button(master, text="確認", command=self.confirm)
        self.confirm_button.pack()

    def select_src_path(self):
        self.src_path = filedialog.askdirectory()
        print("選擇的來源路徑：", self.src_path)

    def select_dest_path(self):
        self.dest_path = filedialog.askdirectory()
        print("選擇的輸出路徑：", self.dest_path)

    def confirm(self):
        print("開始分類圖片...")
        # 輸入和輸出文件夾的路徑
        input_folder = self.src_path
        output_folder = self.dest_path

        # 分類圖像
        classify_images(input_folder, output_folder)


root = tk.Tk()
app = App(root)
root.mainloop()
