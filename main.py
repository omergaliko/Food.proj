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






#print(f' item name: {item_name}\n brand name: {brand_name}\n calories: {calories}')


#print(response.text)
#hits_test = [1 for response in range(1-10):,]
'''
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", type=str, help="Word to get sentiment for", required=True)
    args = parser.parse_args()
    word = args.word
    print(word)
parser = argparse.ArgumentParser()
'''
#food_search = input("which food category whould u like to search: ")
#hits = response[1]["fields"]['item_name']
#hits_test