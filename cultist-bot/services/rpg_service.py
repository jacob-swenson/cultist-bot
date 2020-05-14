from services import base_service, user_service
import json
import random
import re


def name_generator(uid: str):
    user = user_service.get_user(uid)
    user.set_node('get_gender')
    return random.choice(base_service.messages['_request_gender'])


def get_gender(text: str, uid: str):
    user = user_service.get_user(uid)
    gender = None
    pronoun = None
    if re.search(text, r'\b(male)|(boy)\b'):
        gender = 'male'
        pronoun = base_service.respond_to('_male_pronoun')
    elif re.search(text, r'\b(female)|(girl)\b'):
        gender = 'female'
        pronoun = base_service.respond_to('_female_pronoun')
    if gender is None:
        response = base_service.respond_to('_request_gender_failed')
    else:
        user.set_node('get_setting')
        user.set_data('gender', gender)
        response = base_service.respond_to('_request_setting_pre') + pronoun + \
            base_service.respond_to('_request_setting_post') + '\n'
        for setting in name_data:
            response += setting + '\n'
    return response


def get_setting(text: str, uid: str):
    user = user_service.get_user(uid)
    gender = user.get_data('gender')
    setting = None
    for setting_from_data in name_data:
        if text.find(setting_from_data) != -1:
            setting = setting_from_data
    if setting is None:
        response = random.choice(base_service.messages['_request_setting_failed']) + '\n'
        for setting_from_data in name_data:
            response += setting_from_data + '\n'
    else:
        response = random.choice(base_service.messages['_get_name_success'])
        response += random.choice(name_data[setting][gender])
        user.set_node(None)
    return response


with open('data/rpg/names.json') as name_file:
    name_data = json.load(name_file)
