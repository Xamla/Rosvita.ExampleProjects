from typing import Tuple
from lib.python.example_lib import get_instance, get_shared_instance


def main() -> Tuple[str, int]:
    persistent_object = get_shared_instance()

    result = ('get_lib_instance return object with'
                ' memory adress {} and create date time {}'
                ''.format(id(persistent_object),
                          persistent_object.date_time))

    persistent_object.increase_count()

    return result, persistent_object.count