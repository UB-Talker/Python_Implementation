from json import loads, dumps


def save(profile, profile_name):
    f = open('UI/Profiles/'+profile_name, 'w')
    f.write(dumps(profile))
    f.close()
    load(profile_name)
    pass


def load(profile_name):
    try:
        f = open('UI/Profiles/'+profile_name, 'r')
        profile = loads(f.read())
        f.close()
    except FileNotFoundError:
        profile = default_profile
    return profile


default_profile = {'Sample': 'Speak', 'Quit': 'Quit'}
