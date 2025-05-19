from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    if user_message == 'hi':
        response = "Hello!"
    else:
        response = "You said: " + user_message
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
