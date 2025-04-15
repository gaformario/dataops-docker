FROM python:3.10-slim

WORKDIR /app

COPY conecta_postgres.py .

RUN pip install psycopg2-binary

CMD ["python", "conecta_postgres.py"]