import time


def time_decor(old_function):
    def new_function(*args, **kwargs):
        start = time.time()
        result = old_function(*args, **kwargs)
        finish = time.time()
        print(f'функция {old_function.__name__} отработала за {finish-start} секунд')
        return result
    return new_function


@time_decor
def summary(a, b):
    return a + b


res = summary(4, 5)
print(res)
