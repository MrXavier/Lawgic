from flask import Flask, jsonify, request
from flask_cors import CORS
from service import get_completion_response, get_chatbot_response

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})


@app.route('/completion', methods=['POST'])
def get_completion():
  data = request.get_json()
  print("request json: ", data)

  messages = data.get('messages')
  
  if messages is None or messages == []:
      return jsonify({"error": "Missing required parameters 'messages'"}), 400
      
  response = get_completion_response("", messages)

  return jsonify({
      "response": response.get('completion'),
      "messages": response.get('messages')
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
