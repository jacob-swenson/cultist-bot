from services.models import elden_ring_models


def weapon(name):
    print("Getting weapon: " + name)
    data = elden_ring_models.get_data('weapons', name)
    response = data["image"] + "\n\n\n"
    response += "Name: " + data["name"] + "\n"
    response += "Category: " + data["category"] + "\n"
    response += "Weight: " + str(data["weigth"]) + "\n\n"
    response += "Description\n```" + data["description"] + "```\n"
    response += "Attack\n```"
    for attack_stat in data["attack"]:
        response += attack_stat["name"] + ":\t" + str(attack_stat["amount"]) + "\n"
    response += "```\n"
    response += "Defence\n```"
    for defence_stat in data["defence"]:
        response += defence_stat["name"] + ":\t" + str(defence_stat["amount"]) + "\n"
    response += "```\n"
    response += "Scales With\n```"
    for scale_stat in data["scalesWith"]:
        response += scale_stat["name"] + ":\t" + scale_stat["scaling"] + "\n"
    response += "```\n"
    response += "Required Attributes\n```"
    for required_stat in data["requiredAttributes"]:
        response += required_stat["name"] + ":\t" + str(required_stat["amount"]) + "\n"
    response += "```\n"
    return response


def item(name):
    print("Getting Item " + name)
    data = elden_ring_models.get_data('items', name)
    response = data["image"] + "\n\n\n"
    response += "Name: " + data["name"] + "\n"
    response += "Type: " + data["type"] + "\n"
    response += "Description\n```" + data["description"] + "```\n"
    response += "Effect\n```" + data["effect"] + "```\n"
    return response


def shield(name):
    print("Getting Shield " + name)
    data = elden_ring_models.get_data('shields', name)
    response = data["image"] + "\n\n\n"
    response += "Name: " + data["name"] + "\n"
    response += "Category: " + data["category"] + "\n"
    response += "Weight: " + str(data["weigth"]) + "\n\n"
    response += "Description\n```" + data["description"] + "```\n"
    response += "Attack\n```"
    for attack_stat in data["attack"]:
        response += attack_stat["name"] + ":\t" + str(attack_stat["amount"]) + "\n"
    response += "```\n"
    response += "Defence\n```"
    for defence_stat in data["defence"]:
        response += defence_stat["name"] + ":\t" + str(defence_stat["amount"]) + "\n"
    response += "```\n"
    response += "Scales With\n```"
    for scale_stat in data["scalesWith"]:
        response += scale_stat["name"] + ":\t" + scale_stat["scaling"] + "\n"
    response += "```\n"
    response += "Required Attributes\n```"
    for required_stat in data["requiredAttributes"]:
        response += required_stat["name"] + ":\t" + str(required_stat["amount"]) + "\n"
    response += "```\n"
    return response


def ashes(name):
    print("Getting Ashes " + name)
    data = elden_ring_models.get_data('ashes', name)
    response = data["image"] + "\n\n\n"
    response += "Name: " + data["name"] + "\n"
    response += "Affinity: " + data["affinity"] + "\n"
    response += "Skill: " + data["skill"] + "\n"
    response += "Description:\n```" + data["description"] + "```\n"
    return response

