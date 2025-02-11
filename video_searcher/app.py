from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

VIDEO_PROCESSOR_URL = 'http://video_processor:5000/process'  # Взаимодействие через Docker Compose

@app.route('/search', methods=['POST'])
def search_videos():
    file = request.files['file']
    # Отправляем запрос на Video Processor для распознавания объектов
    response = requests.post(VIDEO_PROCESSOR_URL, files={'file': file})
    results = response.json()
    # Фильтруем результаты (например, только "машины")
    filtered_results = [result for result in results['objects'] if "машина" in result]
    return jsonify({"filtered_objects": filtered_results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
