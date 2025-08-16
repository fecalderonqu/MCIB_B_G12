from flask import jsonify

class RespuestaProcesos:
    def __init__(self, code="COD_OK", result=None, info=None, status=True,):
        self.code = code
        self.result = result if result is not None else {}
        self.info = info if info is not None else {}
        self.status = status
    def toJSON(self):
        try :
            data = {
                "code": self.code,
                "result": self.result,
                "info": self.info,
                "status": bool(self.status),
            }
            return jsonify(data)
        except Exception as e:
            data = {
                "code": "COD_ERROR",
                "result": {},
                "info": f"Error al convertir en JSON: {str(e)}",
                "status": False,
            }
            return jsonify(data)