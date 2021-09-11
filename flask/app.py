from flask import Flask, request, make_response, jsonify

class UnvalidRequestBody(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return self.message


def helloworld_valid(request_body):
    '''
    /helloworld api 파라미터 유효성 검사

    : 유효성 검사 실패시 예외발생
    '''

    missing_fiedls = {
        'hello'
    }

    # step1. 필수 파라미터 존재 검사
    missing_fields = missing_fiedls - request_body.keys()
    if len(missing_fields) > 0:
        raise UnvalidRequestBody(f"필수 필드 {missing_fields}가 없습니다.")

    # step2. 타입 검사
    if not isinstance(request_body['hello'], str):
        raise UnvalidRequestBody(f"hello 필드가 string이 아닙니다.")

    # step3. 값이 비어있는지 검사 ...
    # stepN ...


def create_app():
    app = Flask(__name__)

    @app.route("/helloworld", methods=['GET'])
    def helloworld():
        response = {
            'status': "",
            'error_msg': ""
        }

        try:
            helloworld_valid(request.get_json())
        except UnvalidRequestBody as e:
            response['status'] = "failed"
            response['error_msg'] = str(e)
            status_code = 400
        else:
            response['status'] = "succ"
            status_code = 200

        return make_response(jsonify(response), status_code)
    return app