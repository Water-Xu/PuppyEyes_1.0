from flask import Flask, request, jsonify
from flask_cors import cross_origin
import json

import detect

app = Flask(__name__)


@app.route('/get_config')
@cross_origin(origins="*")
def get_config():
    with open('../ffmpegConfig.json', 'r') as f:
        config = json.load(f)
    return jsonify(config)


@app.route('/update_config', methods=['POST'])
@cross_origin(origins="*")
def update_config():
    new_config = request.get_json()
    with open('../ffmpegConfig.json', 'w') as f:
        json.dump(new_config, f)
    return 'Config updated successfully!'


if __name__ == '__main__':
    app.run()
