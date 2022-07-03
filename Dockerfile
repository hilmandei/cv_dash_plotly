FROM python:3.9-slim-buster
COPY . /app
WORKDIR /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt --default-timeout=2000 --no-cache-dir

# Run the application:
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 layotcv:server