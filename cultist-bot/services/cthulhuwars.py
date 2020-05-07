from services.drafter import run_draft, beautify_draft

factions = ['Opener of the Way', 'Crawling Chaos', 'Yellow Sign', 'Great Cthulhu', 'Sleepers', 'The Ancients',
            'Black Goat', 'Windwalkers', 'Tcho-Tcho']


def draft(players):
    result = run_draft(get_factions(), players)
    response = beautify_draft(result)
    return response


def get_factions():
    return factions.copy()
