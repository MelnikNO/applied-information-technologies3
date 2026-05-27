# 1. Базовый образ с Python
FROM python:3.11-slim

# 2. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 4. Копируем код приложения
COPY . .

# 5. Указываем порт, который будет слушать приложение
EXPOSE 8000

# 6. Команда для запуска приложения
CMD ["python", "app.py"]