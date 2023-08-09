import os
import cv2
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def classify_images():
    source_dir = filedialog.askdirectory(title="選擇資料夾")
    if not source_dir:
        return
    output_dir = filedialog.askdirectory(title="選擇輸出資料夾")
    if not output_dir:
        return
    confirm = messagebox.askyesno(title="確認執行", message="執行此操作會清空原始資料夾，是否繼續？")
    if not confirm:
        return
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                filepath = os.path.join(root, file)
                img = cv2.imread(filepath)
                height, width, _ = img.shape
                if height > width:
                    dst_dir = os.path.join(output_dir, "height_greater_than_width")
                elif height == width:
                    dst_dir = os.path.join(output_dir, "height_equals_width")
                else:
                    dst_dir = os.path.join(output_dir, "height_less_than_width")
                os.makedirs(dst_dir, exist_ok=True)
                shutil.move(filepath, os.path.join(dst_dir, file))
    shutil.rmtree(source_dir)
    messagebox.showinfo(title="完成", message="已完成操作")

root = tk.Tk()
root.title("圖片分類工具")
root.geometry("300x100")

button = tk.Button(root, text="分類圖片", command=classify_images)
button.pack()

root.mainloop()
