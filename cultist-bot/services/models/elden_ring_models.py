from fuzzywuzzy import process
from dotenv import load_dotenv
import requests
import json
import os
import time
import shutil

load_dotenv()
ELDEN_RING_API_BASE_URL = 'https://eldenring.fanapis.com/api/'
ELDEN_RING_DATA_PATH = 'data/elden-ring'
FORCE_DOWNLOAD_ELDEN_RING = os.getenv('FORCE_DOWNLOAD_ELDEN_RING')
API_LIMIT = 100

elden_ring_data = {}


def data_downloaded():
    if FORCE_DOWNLOAD_ELDEN_RING:
        shutil.rmtree(ELDEN_RING_DATA_PATH)
    if not os.path.exists(ELDEN_RING_DATA_PATH):
        return False
    if not os.path.isdir(ELDEN_RING_DATA_PATH):
        return False
    if not os.path.exists(ELDEN_RING_DATA_PATH + '/data.json'):
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
    data = {
        'weapons': download_data('weapons', 0, []),
        'items': download_data('items', 0, []),
        'shields': download_data('shields', 0, []),
        'ashes': download_data('ashes', 0, [])
    }
    if not os.path.exists(ELDEN_RING_DATA_PATH):
        os.mkdir(ELDEN_RING_DATA_PATH)
    if not os.path.isdir(ELDEN_RING_DATA_PATH):
        os.remove(ELDEN_RING_DATA_PATH)
        os.mkdir(ELDEN_RING_DATA_PATH)
    with open(ELDEN_RING_DATA_PATH + '/data.json', 'w') as out_file:
        json.dump(data, out_file)


def load_data():
    global elden_ring_data
    with open(ELDEN_RING_DATA_PATH + '/data.json', 'r') as in_file:
        in_data = json.load(in_file)
        weapons = {}
        for weapon in in_data['weapons']:
            weapons[weapon['name']] = weapon
        items = {}
        for item in in_data['items']:
            items[item['name']] = item
        shields = {}
        for shield in in_data['shields']:
            shields[shield['name']] = shield
        ashes = {}
        for ash in in_data['ashes']:
            ashes[ash['name']] = ash
        elden_ring_data = {
            'weapons': weapons,
            'items': items,
            'shields': shields,
            'ashes': ashes
        }


if not data_downloaded():
    download_all_data()

load_data()
