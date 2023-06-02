from timeit import timeit

import flatten  # noqa

SIZE = 1000
TO_MS = 1000
NUM = 10
FUNCTIONS = [
    "flatten_comprehension",
    "flatten_concatenation",
    "flatten_extend",
    "flatten_reduce_lambda",
    "flatten_sum",
    "flatten_itertools_chain",
    "flatten_reduce_add",
    "flatten_reduce_concat",
    "flatten_reduce_iconcat",
]

matrix = [list(range(SIZE))] * SIZE

results = {
    func: timeit(f"flatten.{func}(matrix)", globals=globals(), number=NUM)
    for func in FUNCTIONS
}

print(f"Time to flatten a {SIZE}x{SIZE} matrix (in milliseconds):\n")

for func, time in sorted(results.items(), key=lambda result: result[1]):
    print(f"{func + '()':.<30}{time * TO_MS / NUM:.>10.6f} ms")
