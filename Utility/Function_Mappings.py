function_map = {'Speak': None, 'Quit': None, 'Folder': None}


def set_mapping(key, f):
    function_map[key] = f
    pass


def get_mapping(key):
    return function_map[key]
