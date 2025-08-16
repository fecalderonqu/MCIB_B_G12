from flask import jsonify

info_logs = []

class RespuestaLogs:

    def __init__(self, code="COD_OK", result=None, info=None, status=True):
        self.code = code
        self.result = result if result is not None else {}
        self.info = info if info is not None else {}
        self.status = status

    def addLogs(self, data, name):
        info_logs.append({f'{name}': data.info, 'code': data.code, 'status': data.status})
        self.info = info_logs
        self.status = True
        self.code = 'COD_OK'

    def toJSON(self):
        try :
            data = {
                "code": self.code,
                "result": self.result,
                "info": self.info,
                "status": bool(self.status),
                "isAnomalia": bool(self.isAnomalia)
            }
            return jsonify(data)
        except Exception as e:
            data = {
                "code": "COD_ERROR",
                "result": [],
                "info": f"Error al convertir en JSON: {str(e)}",
                "status": False,
                "isAnomalia": False
            }
            return jsonify(data)
    def resetLogs(self):
        info_logs.clear()

        self.info = info_logs
        self.status = True
        self.code = 'COD_OK'