import requests

def test_video_processor():
    url = 'http://localhost:5000/process'
    files = {'file': open('test_video.mp4', 'rb')}
    response = requests.post(url, files=files)
    assert response.status_code == 200
    assert "objects" in response.json()
