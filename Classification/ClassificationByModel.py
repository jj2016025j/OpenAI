from PIL import Image
import os
import shutil
from PIL import Image, UnidentifiedImageError

#finish
#依圖片模型分類，僅限StableDiffution

# 定義原始路徑和目標路徑
source_path = r"C:\Users\User\Desktop\tablecloth\classification"
target_path = r"C:\Users\User\Desktop\tablecloth\classification"

# 確認目標路徑是否存在，如果不存在就創建一個
if not os.path.exists(target_path):
    os.mkdir(target_path)

# 計數器，用來記錄處理了多少個檔案
count = 0

# 遍歷目標路徑及其子目錄中的所有檔案
#for filename in os.listdir(source_path):
#for root, dirs, files in os.walk(source_path):
#    for filename in files:
model_name = None

for filename in os.listdir(source_path):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        try:
                # 打開圖片並取得模型名稱
            with Image.open(os.path.join(source_path, filename)) as img:
                img_info_str = str(img.info)
                model_index = img_info_str.find('Model:')
                if model_index != -1:
                    model_name = img_info_str[model_index:].split(',')[0].strip().replace("Model: ", "")
                    print(model_name)
                else:
                    print("Model information not found.")

            # 確認模型名稱是否存在
            if model_name:
                # 根據模型名稱建立目標資料夾
                target_folder = os.path.join(target_path, model_name)
                if not os.path.exists(target_folder):
                    os.mkdir(target_folder)

                # 移動檔案到目標資料夾
                shutil.move(os.path.join(source_path, filename), os.path.join(target_folder, filename))
                print(f"Moved file {filename} to {target_folder}")

                # 記錄處理了多少個檔案
                count += 1
            
            else:
                # 根據模型名稱建立目標資料夾
                target_folder = os.path.join(target_path, "other")
                if not os.path.exists(target_folder):
                    os.mkdir(target_folder)

                # 移動檔案到目標資料夾
                shutil.move(os.path.join(source_path, filename), os.path.join(target_folder, filename))
                print(f"Moved file {filename} to {target_folder}")

                # 記錄處理了多少個檔案
                count += 1
        except (OSError, UnidentifiedImageError):
            print(f"Skipped file {filename}: Unidentified image format")
    else:
        print(f"Skipping file {filename}: Invalid image format")

# 輸出處理了多少個檔案
print(f"Processed {count} files.")
