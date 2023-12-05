"""General helper functions used in most solutions."""
import time


def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print(f"func:{f.__name__} took: {te - ts} sec")
        return result

    return timed


def grouped(iterable, n):
    return zip(*[iter(iterable)] * n)


def read_input(single_string: bool = False, test: bool = False) -> list[str] | str:
    """Read input file lines."""
    input_file = "input.txt"
    if test:
        input_file = "test_input.txt"
    with open(input_file, "r") as f:
        if single_string:
            return f.read()
        return f.readline()
