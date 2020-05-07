from services import cthulhuwars, base_service


def get_handler(command: str):
    if command not in commands:
        return unknown
    return commands[command]['handler']


def dispatch(command: str, args):
    return get_handler(command)(command, args)


def draft(command, players):
    print('User wants to run a Cthulhu Wars draft')
    return cthulhuwars.draft(players)


def base_command(command, args):
    print('Handling base command')
    return base_service.respond_to(command)


def unknown(command, args):
    print(f'Unknown input: {command} with args: {args}')
    return base_service.respond_to('unknown')


def get_help(command, args):
    print('Showing help test')
    resp = 'I am a bot built by m3ddl3r as a side project in his free time.\n'
    resp += 'Commands cultist knows:\n```\n'
    for cmd in commands:
        resp += f"{cmd}:\t{commands[cmd]['help']}\n"
    resp += '```\n I am also slowly learning how to understand natural language. DM me and tell me to do some of these ' \
            'commands in plain English and see what I can do!'
    return resp


def populate_base_commands():
    for command in base_service.messages:
        if command == 'unknown':
            continue
        commands[command] = {
            'help': 'Run me to see what I do',
            'handler': base_command
        }


commands = {
    'draft': {
        'help': 'Runs a draft for Cthulhu Wars',
        'handler': draft
    },
    'help': {
        'help': 'Displays this message',
        'handler': get_help
    }
}


populate_base_commands()