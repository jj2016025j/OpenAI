import openai
from flask import Flask, request, jsonify
import subprocess
import threading
import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
#pip install Flask
#pip install openai  
#pip install line-bot-sdk 

# 用於追踪開發者的printg功能
def printg(message):
    """打印開發者追踪信息"""
    print("[開發者訊息] " + message)

#怎麼樣都讀取有問題
# 讀取配置文件
try:
    with open('config.json', 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    printg("錯誤: 找不到config.json文件")
except json.JSONDecodeError:
    printg("錯誤: config.json的格式不正確")
except Exception as e:
    printg(f"錯誤: {e}")

# 從配置文件取得金鑰
auth_token = config["auth_token"]
access_token = config["access_token"]
secret = config["secret"]
openai_api_key = config["openai_api_key"]

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    """處理LINE機器人的回调"""
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    printg("收到LINE消息")
    
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        msg_type = json_data['events'][0]['message']['type']

        if msg_type == 'text':
            msg = json_data['events'][0]['message']['text']

            # 如果消息以 "hi ai" 開頭，使用OpenAI回答
            if msg.startswith('Hi OpenAI '):
                printg("使用OpenAI生成回复")
                openai.api_key = openai_api_key
                response = openai.Completion.create(
                    model='text-davinci-003',
                    prompt=msg[6:],
                    max_tokens=10,
                    temperature=0.5,
                )
                reply_msg = response["choices"][0]["text"].strip()
            else:
                reply_msg = msg
        else:
            reply_msg = '你傳的不是文字呦～'
            printg("接收到非文字消息")

        line_bot_api.reply_message(tk, TextSendMessage(reply_msg))
    except Exception as e:
        printg(f"錯誤: {e}")
    return 'OK'

@app.route("/<name>", methods=['GET', 'POST'])
def home(name):
    """回應GET或POST請求的簡單路由"""
    if request.method == 'POST':
        printg(f"收到POST請求: {request.json}")
        return jsonify({'message': 'Success'}), 200
    else:
        return f"<h1>{name}</h1>"

def run_app():
    """運行Flask應用程序的函數"""
    printg("啟動Flask應用")
    app.run()

def run_ngrok():
    """啟動ngrok的函數"""
    printg("啟動ngrok")
    cmd1 = f"ngrok config add-authtoken {auth_token}"
    subprocess.run(cmd1, shell=True)
    cmd2 = 'start cmd /k "ngrok http 5000"'
    subprocess.Popen(cmd2, shell=True)

if __name__ == "__main__":
    threading.Thread(target=run_app).start()
    run_ngrok()
