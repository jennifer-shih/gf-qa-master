from src.helper.log import Logger


def retry(times, exceptions):
    """
    Retry Decorator
    Retries the wrapped function/method `times` times if the exceptions listed
    in ``exceptions`` are thrown
    :param times: The number of times to repeat the wrapped function/method
    :type times: Int
    :param Exceptions: Lists of exceptions that trigger a retry attempt
    :type Exceptions: Tuple of Exceptions
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    Logger.getLogger().warning(
                        f"Exception thrown when attempting to run {func}, attempt {attempt} of {times}"
                    )
                    attempt += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator
