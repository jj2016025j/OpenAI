import cv2
import tkinter as tk
from PIL import Image, ImageTk
#展示圖片
#finish

# 创建Tkinter窗口
root = tk.Tk()
root.title("Image Viewer")

# 创建Canvas控件
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(side="left", fill="both", expand=True)

# 加载图像
image = cv2.imread("example.png")

# 将图像转换为PIL格式
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)

# 显示图像
photo = ImageTk.PhotoImage(image)
canvas_image = canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# 自动调整图像大小并添加滚动条
def resize_image(event):
    global photo  # 声明photo为全局变量

    # 获取窗口大小
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # 计算缩放比例
    scale = min(width / image.width, height / image.height)

    # 缩放图像
    resized_image = image.resize((int(image.width * scale), int(image.height * scale)))

    # 将缩放后的图像转换为PIL格式
    resized_image = resized_image.convert("RGB")

    # 更新Canvas上的图像
    photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfigure(canvas_image, image=photo)

# 监听窗口大小变化事件
canvas.bind("<Configure>", resize_image)

# 运行Tkinter主循环
root.mainloop()
