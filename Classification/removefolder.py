import os
import shutil
import tkinter as tk
from tkinter import messagebox
#移除所有資料夾
#遇到相同的會改名

# Move and rename function
# 移動和重新命名的功能
def move_and_rename(target_path):
    # Loop through all subdirectories in the target path
    # 遍歷目標路徑下的所有子目錄
    for root, dirs, files in os.walk(target_path):
        # Check if the current directory is a subdirectory of the target path
        # 檢查當前目錄是否為子目錄
        if root != target_path:
            # Loop through all files in the current directory
            # 遍歷當前目錄中的所有檔案
            for file in files:
                # Create the full path to the file
                # 建立當前檔案的完整路徑
                file_path = os.path.join(root, file)
                # Check if a file with the same name already exists in the target directory
                # 檢查在目標目錄中是否已存在相同名稱的檔案
                target_file_path = os.path.join(target_path, file)
                i = 1
                while os.path.exists(target_file_path):
                    # Generate a new filename by adding a number suffix
                    # 透過增加數字後綴生成新的檔案名
                    target_file_path = os.path.join(target_path, f"{os.path.splitext(file)[0]}_{i}{os.path.splitext(file)[1]}")
                    i += 1
                # Move the file to the target directory
                # 將檔案移動到目標目錄
                shutil.move(file_path, target_file_path)
            # Remove the subdirectory and all its contents
            # 刪除子目錄及其所有內容
            shutil.rmtree(root)
    #messagebox.showinfo("Info", "Operation completed!")
    print("Finish!")

# GUI function
# 圖形介面的功能
def start_gui():
    # Create a new Tk root widget
    # 創建一個新的Tk根部件
    root = tk.Tk()
    root.title('Move and Rename Files')

    # Create a new Entry widget
    # 創建一個新的Entry部件
    entry = tk.Entry(root, width=50)
    entry.pack()

    # Create a new Button widget
    # 創建一個新的Button部件
    button = tk.Button(root, text="Start", command=lambda: move_and_rename(entry.get()))
    button.pack()

    # Start the Tk event loop
    # 開始Tk的事件迴圈
    root.mainloop()

# Start the GUI
# 開始圖形介面
start_gui()
