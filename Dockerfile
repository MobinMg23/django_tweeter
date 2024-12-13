FROM python:latest

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

EXPOSE 8000

CMD ["sh", "-c", "/app/wait-for-it.sh db:3306 -- /app/wait-for-it.sh elasticsearch:9200 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
