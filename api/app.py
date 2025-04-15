from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_clientes():
    conn = psycopg2.connect(
        host="db",
        database="postgres",
        user="postgres",
        password="senha123"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes;")
    clientes = cur.fetchall()
    cur.close()
    conn.close()
    return clientes

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = get_clientes()
    return jsonify(clientes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)