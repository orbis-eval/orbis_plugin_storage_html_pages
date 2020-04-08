from palettable.tableau import Tableau_20


def sort_queue(queue):
    int_queue = []

    for item in queue:
        try:
            int_queue.append(int(item))
        except ValueError:
            int_queue.append(item)

    int_queue = sorted(int_queue)
    new_queue = [str(item) for item in int_queue]

    return new_queue


def get_keys(item):
    keys = set()
    if item.get('gold'):
        for entity in item['gold']:
            keys.add(entity['key'])

    if item.get('computed'):
        for entity in item['computed']:
            keys.add(entity['key'])
    return keys


def get_sf_colors(keys):

    sf_colors = {}
    colour_idx = 0
    for sf in keys:
        sf_colors[sf] = Tableau_20.hex_colors[colour_idx]
        colour_idx = 0 if colour_idx == 19 else colour_idx + 1
    return sf_colors
