FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENV DB_PATH=/app/db

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
