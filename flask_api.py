import requests
from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
import os
from dotenv import load_dotenv
import json

from respuestaLogs import RespuestaLogs
from respuestaProcesos import RespuestaProcesos
# Cargar variables de entorno
load_dotenv()

# Configuración de la aplicación
app = Flask(__name__)
auth = HTTPBasicAuth()

logs = RespuestaLogs()

@app.route('/api/getInfoIp', methods=['POST'])
def init():
    response = RespuestaProcesos()
    logs.resetLogs()
    try:
        ip = request.json.get('ip', '127.0.0.1')
        result = requests.get(f"http://ip-api.com/json/{ip}", json=request.json).json()
        response.result = result
        response.code = 'COD_OK'
        response.info = f"Información obtenida para la IP: {ip}"
        response.status = True

    except Exception as e:
        response.code = 'COD_ERR'
        response.info = f"Error dentro de init: {str(e)}"
        response.status = False

    return response.toJSON()

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT'))
    app.run(host=host, port=port, debug=False)