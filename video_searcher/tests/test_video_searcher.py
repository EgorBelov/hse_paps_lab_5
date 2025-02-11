import requests

def test_video_searcher():
    url = 'http://video_searcher:5001/search'  
    files = {'file': open('/app/tests/test.mp4', 'rb')}  # Путь к файлу внутри контейнера
    response = requests.post(url, files=files)
    assert response.status_code == 200
    assert "filtered_objects" in response.json()
