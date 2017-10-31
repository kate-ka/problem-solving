"""Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""


def namelist(names):
    x = []
    if len(names) == 2:
        return '{} & {}'.format(names[0]['name'], names[1]['name'])

    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 0:
        return ''
    else:
        for item in names:
            x.append(item['name'])
        first_part = x[:-2]
        second_part = x[-2:]
        final = (', ').join(first_part) + ', ' + (' & ').join(second_part)
        return final
