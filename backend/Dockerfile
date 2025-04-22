FROM python:3.12-alpine

WORKDIR /app

RUN apk add --no-cache postgresql-client bash

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]