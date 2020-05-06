import random


def run_draft(choices: list, players: list):
    result = {player: [] for player in players}
    loops = len(choices) // len(result)
    print('Looping ' + str(loops) + ' times')
    # draft choices
    for x in range(0, loops):
        print('Loop ' + str(x))
        for player in result:
            print('Handling player ' + player)
            print(choices)
            repeat = True
            attempts = 0
            timeout = 10
            while repeat:
                selected = random.choice(choices)
                if selected in result[player]:
                    repeat = True
                    if attempts is timeout:
                        result[player].append('N/A')
                        repeat = False
                else:
                    print('Chose ' + selected + ' for player ' + player)
                    result[player].append(selected)
                    choices.remove(selected)
                    repeat = False
    return result


def beautify_draft(results):
    response = '```\n'
    for player in results:
        response += player + '\n'
        n = 1
        for option in results[player]:
            response += '\t' + str(n) + '. ' + option + '\n'
            n += 1
        response += '\n'
    response += '```'
    return response
