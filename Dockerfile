FROM python:3.14-slim

WORKDIR /shop

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

COPY templates ./templates

COPY static ./static

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
