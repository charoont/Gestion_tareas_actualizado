FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt clean

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 9999

CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]
