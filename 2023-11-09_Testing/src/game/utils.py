from functools import wraps


def when(condition_method_name):
    def decorator(mth):
        @wraps(mth)
        def wrapper(character, *args, **kwargs):
            condition = getattr(character, condition_method_name)
            if condition():
                return mth(character, *args, **kwargs)
        return wrapper
    return decorator
