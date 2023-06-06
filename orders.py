from datetime import *

from regex import regex, match


# Проверка имени пользователя (соответствие формату)
def check_name(name):
    if not regex.match("^[a-zA-Z0-9_]+$", name):
        return False
    else:
        return True


# Проверка телефона пользователя (американский формат без плюса, с дефисами)
def check_phone(phone):
    if not regex.match("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", phone):
        return False
    else:
        return True


# Проверка дедлайна (не раньше чем сегодня)
def check_date(deadline):
    if datetime.strptime(deadline, "%Y-%m-%d").date() < datetime.now().date():
        return False
    else:
        return True
