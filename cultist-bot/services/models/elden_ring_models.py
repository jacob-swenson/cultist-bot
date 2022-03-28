from fuzzywuzzy import process
from dotenv import load_dotenv
import requests
import json
import os
import shutil

load_dotenv()
ELDEN_RING_API_BASE_URL = 'https://eldenring.fanapis.com/api/'
ELDEN_RING_DATA_PATH = 'data/elden-ring'
FORCE_DOWNLOAD_ELDEN_RING = os.getenv('FORCE_DOWNLOAD_ELDEN_RING') == "True"
API_LIMIT = 100

data_sets = ['weapons', 'items', 'shields', 'ashes', 'bosses', 'npcs', 'locations', 'spirits', 'talismans', 'armors',
             'creatures', 'classes', 'incantations', 'sorceries', 'ammos']
elden_ring_data = {}



def data_downloaded():
    if FORCE_DOWNLOAD_ELDEN_RING and os.path.exists(ELDEN_RING_DATA_PATH):
        shutil.rmtree(ELDEN_RING_DATA_PATH)
    if not os.path.exists(ELDEN_RING_DATA_PATH):
        return False
    if not os.path.isdir(ELDEN_RING_DATA_PATH):
        return False
    if not os.path.exists(ELDEN_RING_DATA_PATH + '/data.json'):
        return False
    with open(ELDEN_RING_DATA_PATH + '/data.json', 'r') as in_file:
        in_data = json.load(in_file)
        for data_set in data_sets:
            if data_set not in in_data.keys():
                return False
    return True


def download_data(context, page, data):
    response = requests.get(ELDEN_RING_API_BASE_URL + context + '?limit=' + str(API_LIMIT) + '&page=' + str(page)).json()
    total = response['total']
    data.extend(response['data'])
    if len(data) < total:
        return download_data(context, page+1, data)
    return data


def get_data(data_type, name):
    best_guess = process.extractOne(name, elden_ring_data[data_type].keys())
    return elden_ring_data[data_type][best_guess[0]]


def download_all_data():
    data = {}
    for data_set in data_sets:
        data[data_set] = download_data(data_set, 0, [])
    if not os.path.exists(ELDEN_RING_DATA_PATH):
        os.mkdir(ELDEN_RING_DATA_PATH)
    if not os.path.isdir(ELDEN_RING_DATA_PATH):
        os.remove(ELDEN_RING_DATA_PATH)
        os.mkdir(ELDEN_RING_DATA_PATH)
    with open(ELDEN_RING_DATA_PATH + '/data.json', 'w') as out_file:
        json.dump(data, out_file)


def load_data():
    global elden_ring_data
    global data_sets
    elden_ring_data = {}
    with open(ELDEN_RING_DATA_PATH + '/data.json', 'r') as in_file:
        in_data = json.load(in_file)
        for data_set in data_sets:
            elden_ring_data[data_set] = {}
            for data_item in in_data[data_set]:
                elden_ring_data[data_set][data_item['name']] = data_item


if not data_downloaded():
    download_all_data()

load_data()
