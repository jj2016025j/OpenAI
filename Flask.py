from flask import Flask
import subprocess
import threading

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return f"<h1>{name}</h1>"

def run_app():
    app.run()

def run_ngrok():
    # 配置 authtoken
    cmd1 = "ngrok config add-authtoken 2TgnwaFJy8Ez0j07UtssJyAHzQp_RSjTnkAWZDrYCWUGM7Qi"
    subprocess.run(cmd1, shell=True)

    # 啟動 ngrok
    cmd2 = "ngrok http 5000 -host-header=localhost:5000"
    subprocess.run(cmd2, shell=True)

# 使用 threading 啟動 Flask 應用和 ngrok
threading.Thread(target=run_ngrok).start()
threading.Thread(target=run_app).start()
