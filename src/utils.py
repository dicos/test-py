from fastapi.responses import JSONResponse

class CJsonResp:
    def success(self, msg: dict|str, code: int = 200):
        return self.res(msg, True, code)

    def error(self, msg: dict|str, code: int = 200):
        return self.res(msg, False, code)

    def res(self, msg: dict|str, status: bool, code: int):
        data = msg if (type(msg) is dict) else {}
        prepare = {
            'success': status,
            'message': '' if (type(msg) is dict) else msg
        } | data

        return JSONResponse(status_code=code, content=prepare)

jsonResp = CJsonResp()