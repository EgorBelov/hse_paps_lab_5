# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем необходимые системные библиотеки для OpenCV и других зависимостей
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    apt-get clean

# Устанавливаем зависимости для работы с видео
RUN pip install --no-cache-dir opencv-python numpy flask pytest requests

# Копируем исходный код сервиса в контейнер
COPY ./video_processor /app

# Копируем видеофайл в контейнер
COPY ./video_processor/tests/test.mp4 /app/tests/test.mp4

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Открываем порт для работы Flask
EXPOSE 5000

# Команда для запуска сервиса
CMD ["python", "app.py"]
