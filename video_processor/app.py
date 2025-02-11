from flask import Flask, request, jsonify
import cv2

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_video():
    file = request.files['file']
    # Симуляция обработки видео
    results = {"objects": ["машина", "дерево", "человек"]}
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
