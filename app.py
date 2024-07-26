import os
from flask import Flask, jsonify, send_from_directory
import oracledb

# Configuración de las variables de entorno
os.environ['NODE_EXTRA_CA_CERTS'] = '/home/ubuntu/blockchain/Wallet_NFTS/ewallet.pem'

app = Flask(__name__, static_folder='public')

# Configuración de la base de datos
db_config = {
    'user': 'ADMIN',  # Usuario de la base de datos
    'password': 'K@rdyan260202cr!',  # Contraseña del usuario de la base de datos
    'dsn': 'nfts_high',  # Usar el alias del tnsnames.ora
    'config_dir': '/home/ubuntu/blockchain/Wallet_NFTS'  # Directorio de configuración
}

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/pacientes', methods=['GET'])
def get_pacientes():
    connection = None
    cursor = None
    try:
        connection = oracledb.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT NOMBRE, FECHANACIMIENTO, GENERO, DIRECCION FROM PACIENTE")
        pacientes = cursor.fetchall()
        return jsonify(pacientes)
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al obtener los pacientes"}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=40000)
