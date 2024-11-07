from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})


@app.route('/completion', methods=['POST'])
def get_completion():
  # deserilize the body in a boject
  data = request.get_json()
  print(data)

  model = data.get('model')
  messages = data.get('messages')

  return jsonify({
      "completion": "Sample completion response",
      "model": model,
      "messages": messages
  })

@app.route('/chatbot', methods=['POST']) 
def chat_with_bot():
    data = request.get_json()
    print(data)

    message = data.get('message')

    return jsonify({
        "reply": "Sample chatbot response",
        "message": message
    })



if __name__ == '__main__':
    app.run(debug=True)
# POST /completion
# body: {
#   "model": "string",
#   "messages": [
#     {
#       "role": "system",
#       "content": "You are a helpful assistant."
#     },
#     {
#       "role": "user",
#       "content": "Hello!"
#     }
#   ]
# }

# POST /chatbot
# body: {
#   "message": "string"
# }