from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'your-api-key-here'

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/message/<message>", methods=['GET','POST'])
def message(message):
    return message

@app.route('/generate-text', methods=['GET','POST'])
def generate_text():
    data = request.json
    response = openai.Completion.create(engine="davinci", prompt=data['prompt'], max_tokens=50)
    return jsonify(response.choices[0].text)

if __name__ == "__main__":
    app.run(debug=True)
