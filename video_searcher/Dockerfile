# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем необходимые зависимости для работы с Flask и Requests
RUN pip install --no-cache-dir flask requests pytest

# Копируем исходный код сервиса в контейнер
COPY ./video_searcher /app

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Открываем порт для работы Flask
EXPOSE 5001

# Команда для запуска сервиса
CMD ["python", "app.py"]
