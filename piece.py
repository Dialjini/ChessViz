piece = [{'color': 'white', 'name': 'k', 'canrock': '1', 'cord': ''},
         {'color': 'white', 'name': 'q', 'cord': ''}]


def getPiece(cord):
    for i in piece:
        if (i['cord'] == cord):
            return i['name']
