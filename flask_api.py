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

@app.route('/api/getInfo', methods=['POST'])
def init():
    response = RespuestaProcesos()
    logs.resetLogs()
    try:
        print("hola")

    except Exception as e:
        response.code = 'COD_ERR'
        response.info = f"Error dentro de init: {str(e)}"
        response.status = False

    return response.toJSON()

import math
@app.route('/api/factorial', methods=['POST'])
def factorial():
    response = RespuestaProcesos()
    logs.resetLogs()
    try:
        numero = int(request.args.get('numero', 1))
        resultado = math.factorial(numero)
        
        response.code = 'COD_OK'
        response.info = "Cálculo del factorial"
        response.status = True
        response.result = {"numero": numero, "factorial": resultado}
        
    except:
        response.code = 'COD_ERR'
        response.info = "Error al calcular el factorial"
        response.status = False
        
    return response.toJSON()

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT'))
    app.run(host=host, port=port, debug=False)