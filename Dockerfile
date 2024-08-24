FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install numpy==2.0.1


EXPOSE 5000

CMD ["python", "app.py"]