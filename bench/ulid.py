import timeit
from time import time

from ulid_transform import ulid_at_time, ulid_now

count = 5000000
result = timeit.Timer(ulid_now).timeit(count)
print(f"ulid_now x {count} took {result} seconds")
result = timeit.Timer("ulid_at_time(1)", globals={"ulid_at_time": ulid_at_time}).timeit(
    count
)
print(f"ulid_at_time without time x {count} took {result} seconds")
result = timeit.Timer(
    "ulid_at_time(time())", globals={"time": time, "ulid_at_time": ulid_at_time}
).timeit(count)
print(f"ulid_at_time w/time x {count} took {result} seconds")
