from abc import ABC 
import enum
import re

class BaseField(ABC):
    def __init__(self)->None:
        pass

    def validate_field(self):
        pass


class Fields(enum.Enum):
    email = 1
    phone = 2
    date = 3
    text = 4


class DateField(BaseField):
    def __init__(self):
        pass

    def validate_field(self, data):
        regular_one = '\d\d\.\d\d\.\d{4}'
        regular_two = '\d{4}.\d\d.\d\d'
        return bool(re.match(regular_one, data)) | bool(re.match(regular_two, data))


class PhoneField(BaseField):
    def __init__(self) -> None:
        pass

    def validate_field(self, data):
        regular = '(\+7)?[\s]?\(?[0-9]{3}\)?[\s]?[0-9]{3}[\s]?[0-9]{2}[\s]?[0-9]{2}$'
        return bool(re.match(regular, data))


class EmailField(BaseField):
    def __init__(self) -> None:
        pass

    def validate_field(self, data):
        regular = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(regular, data))


class TextField(BaseField):
    def __init__(self) -> None:
        pass
