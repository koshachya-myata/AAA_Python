"""Utils for logging."""
from typing import Callable, Union
import random


def log(template: Union[str, None] = None) -> Callable:
    """
    Decorate a function to log its execution time (simulated using randint).

    Parameters:
        template (Union[str, None]): a format string to customize log message.
                                     If None, a default message is used.
                                     String should contain a placeholder: {}.

    Returns:
        Callable: Decorated function.

    Example:
        @log("Execution time: {} seconds.")
        def my_function():
            # function logic
    """
    def deocrator(fn: Callable):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            delta_time = random.randint(1, 5)
            if template is None:
                print(f'{fn.__name__} — {delta_time}s!')
            else:
                print(template.format(delta_time))
            return result
        return wrapper
    return deocrator
