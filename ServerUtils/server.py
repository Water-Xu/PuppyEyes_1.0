from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 在应用中使用CORS
status = False


@app.after_request
def func_res(resp):
    res = make_response(resp)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return res


@app.route('/get_data', methods=['GET'])
def get_data():
    data = {'status': status}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
