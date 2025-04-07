FROM python:3.12

WORKDIR /app

# Install Postgres client (for pg_isready)
RUN apt-get update && apt-get install -y postgresql-client

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

CMD ["bash", "/app/entrypoint.sh"]
