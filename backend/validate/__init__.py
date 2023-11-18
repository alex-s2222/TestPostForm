import re


def get_type_data(value: str) -> str:
    if validate_date(value):
        return 'date'
    elif validate_phone(value):
        return 'phone'
    elif validate_email(value):
        return 'email'
    else:
        return 'text'


def validate_date(data: str) -> bool:
    regular_one = '\d\d\.\d\d\.\d{4}'
    regular_two = '\d{4}.\d\d.\d\d'
    return bool(re.match(regular_one, data)) | bool(re.match(regular_two, data))


def validate_phone(data: str) -> bool:
    regular = '(\+?7)?[\s]?\(?[0-9]{3}\)?[\s]?[0-9]{3}[\s]?[0-9]{2}[\s]?[0-9]{2}$'
    return bool(re.match(regular, data))


def validate_email(data: str) -> bool:
    regular = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regular, data))

