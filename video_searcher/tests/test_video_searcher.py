import requests

def test_video_searcher():
    url = 'http://localhost:5001/search'
    files = {'file': open('test_video.mp4', 'rb')}
    response = requests.post(url, files=files)
    assert response.status_code == 200
    assert "filtered_objects" in response.json()
