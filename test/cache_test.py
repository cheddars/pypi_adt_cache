import string
import random
from datetime import datetime
from cache import *


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_samples():
    strs = [get_random_string(20) for i in range(10000)]
    sample_01_100 = [random.choice(strs) for i in range(100)]
    sample_02_90 = [random.choice(strs) for i in range(90)]
    sample_03_80 = [random.choice(strs) for i in range(80)]
    sample_04_70 = [random.choice(strs) for i in range(70)]
    sample_05_60 = [random.choice(strs) for i in range(60)]
    sample_06_50 = [random.choice(strs) for i in range(50)]

    strxs = [get_random_string(21) for i in range(1000)]
    samplex_01_10 = [random.choice(strxs) for i in range(10)]
    samplex_02_20 = [random.choice(strxs) for i in range(20)]
    samplex_03_30 = [random.choice(strxs) for i in range(30)]
    samplex_04_40 = [random.choice(strxs) for i in range(40)]
    samplex_05_50 = [random.choice(strxs) for i in range(50)]
    samplex_06_60 = [random.choice(strxs) for i in range(60)]


    samples = [sample_01_100 + samplex_01_10,
               sample_02_90 + samplex_02_20,
               sample_03_80 + samplex_03_30,
               sample_04_70 + samplex_04_40,
               sample_05_60 + samplex_05_50,
               sample_06_50 + samplex_06_60]
    for s in samples:
        random.shuffle(s)
    return strs, samples


def test_cache(cache: AdtCache):
    strs, samples = generate_samples()
    timing = {"init" : datetime.now()}
    mcache: AdtCache = cache
    mcache.push_values("random_keys", strs)
    timing["push"] = datetime.now()
    for i, s in enumerate(samples):
        inter = mcache.intersect("random_keys", s)
        timing[f"intersect_{i}"] = datetime.now()

    return timing

def test_memcache():
    epochs = 10
    epoch_list = []
    for i in range(epochs):
        timings = test_cache(MemoryCache())
        values = list(timings.values())
        deltas = [values[i + 1] - values[i] for i in range(len(values) - 1)]
        epoch_list.append(list(map(lambda x: x.total_seconds() * 1000, deltas)))
    #test_cache(RedisCache(host="localhost", port=6379, db=0))

    for i in range(len(epoch_list[0])):
        print(f"{i}: {sum([e[i] for e in epoch_list]) / epochs}")

def test_rediscache():
    epochs = 10
    epoch_list = []
    for i in range(epochs):
        timings = test_cache(RedisCache(host="localhost", port=6380, db=1))
        values = list(timings.values())
        deltas = [values[i + 1] - values[i] for i in range(len(values) - 1)]
        print(deltas)
        epoch_list.append(map(lambda x: {"round": i, "secs": x.total_seconds() * 1000}, deltas))

    print(epoch_list)
#    for i in range(len(epoch_list[0].values())):
#        print(f"{i}: {sum([e.values()[i] for e in epoch_list]) / epochs}")

if __name__ == "__main__":
   test_rediscache()