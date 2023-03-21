FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./backend/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt