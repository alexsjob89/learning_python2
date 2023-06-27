from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/reverse', methods=['POST'])
def reverse_text():
    data = request.get_json()
    reversed_text = data['text'][::-1]
    return jsonify({'reversedText': reversed_text})

if __name__ == '__main__':
    app.run(port=5000)

