from typing import Tuple
from lib.python.example_lib import get_instance, get_shared_instance


def main() -> Tuple[str, str]:
    non_persistent_object = get_instance()

    result_1 = ('get_instance returns object with'
                ' memory address {} and creation date time {}'
                ''.format(id(non_persistent_object),
                          non_persistent_object.date_time))

    persistent_object = get_shared_instance()

    result_2 = ('get_lib_instance returns object with'
                ' memory address {} and creation date time {}'
                ''.format(id(persistent_object),
                          persistent_object.date_time))

    persistent_object.increase_count()

    return result_1, result_2

