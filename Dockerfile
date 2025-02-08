# Используем официальный образ Python (выберите нужную версию)
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей отдельно для эффективного кеширования слоёв
COPY requirements.txt .

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в рабочую директорию
COPY . .

# Устанавливаем переменную окружения PYTHONPATH, чтобы при импортах from src... 
# Python искал модуль в директории, содержащей каталог src (в данном случае /app)
ENV PYTHONPATH="/app"

# Открываем порт, который будет использоваться приложением (например, 80)
EXPOSE 80

RUN chmod +x entrypoint.sh


ENTRYPOINT ["/app/entrypoint.sh"]
# Запускаем приложение через uvicorn. Предполагается, что в файле main.py определён объект app.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
