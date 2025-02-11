import requests

def test_video_processor():
    url = 'http://video_processor:5000/process' 
    files = {'file': open('/app/tests/test.mp4', 'rb')}  # Путь к файлу внутри контейнера
    response = requests.post(url, files=files)
    assert response.status_code == 200
    assert "objects" in response.json()
