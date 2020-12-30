from logs import logger
import json
import send
import argparse


def load_config():
    with open('./configuration.json') as json_file:
        configs = json.load(json_file)
        key = configs['configurations']['key']
        host = configs['configurations']['host']
        return key, host

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--food", type=str, help="Word to get sentiment for", required=True)
    args = parser.parse_args()
    food = args.food
    print(food)
    logger.info("The selected food is: " + str(args))

    key, host = load_config()
    send.send(key, host, food)


main()