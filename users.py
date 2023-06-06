from datetime import *

from regex import regex


def name(nickname):
    if not regex.match("^[a-zA-Z0-9_]+$", nickname):
        return False
    else:
        return True


def date(deadline):
    if datetime.strptime(deadline, "%Y-%m-%d").date() <= datetime.now().date():
        return True
    else:
        return False
