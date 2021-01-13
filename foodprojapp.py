from flask import Flask
from flask import request
import json
import send

app = Flask(__name__)

def load_config():
    with open('./configuration.json') as json_file:
        configs = json.load(json_file)
        key = configs['configurations']['key']
        host = configs['configurations']['host']
        return key, host

@app.route('/', methods=['POST'])


def main():
    data = request.get_json() or {}
    food = data['food']
    key = load_config()[0]
    host = load_config()[1]
    response = send.send(key, host, food)
    #json_resp = json.dumps(response)
    # json_response = json.loads(json_resp)
    print(type(response))

    # this can be used to custom construct json response
    # data = {}
    # data['key'] = 'value'
    # json_data = json.dumps(data)

    return response['hits'][0]['fields']