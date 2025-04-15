import psycopg2
import time

time.sleep(5)

conn = psycopg2.connect(
    host="db",
    database="postgres",
    user="postgres",
    password="senha123"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50)
);
""")

conn.commit()


cur.execute("INSERT INTO clientes (nome) VALUES ('Alice');")
cur.execute("INSERT INTO clientes (nome) VALUES ('Bob');")
conn.commit()

cur.close()
conn.close()