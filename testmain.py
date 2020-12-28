import send
import json
import argparse

def load_config():
    with open('configurations') as json_file:
        configs = json.load(json_file)
        key = configs['configurations']['key']
        host = configs['configurations']['host']
        return key, host

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--food', action='store', dest='fields', help='all_fields', required=True)
    args = parser.parse_args()
    food = args.food
    print(food)


    key = load_config()[0]
    host = load_config()[1]

    response = send.send(key, host, word)
    print(response)