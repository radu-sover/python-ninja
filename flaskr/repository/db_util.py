import functools


def execute_with_transaction(function, database):
    @functools.wraps(function)
    def wrap(*args, **kwargs):
        with database.begin() as connection:
            result = function(*args, connection=connection, **kwargs)
        return result
    return wrap
