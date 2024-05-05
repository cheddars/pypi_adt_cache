import unittest
from datetime import datetime
from cache import *
from test.helper import generate_samples

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)-10s [%(levelname)s] %(message)s")


class RedistCacheTest(unittest.TestCase):

    def setUp(self):
        cache = RedisCache(host="localhost", port=6379, db=6)
        strs, samples = generate_samples()
        timing = {"init" : datetime.now()}
        mcache: AdtCache = cache
        mcache.push_values("random_keys", strs)
        timing["push"] = datetime.now()
        for i, s in enumerate(samples):
            inter = mcache.intersect("random_keys", s)
            timing[f"intersect_{i}"] = datetime.now()
        self.timing = timing

    def test_rediscache(self):
        epochs = 10
        epoch_list = []
        for i in range(epochs):
            timings = self.timing
            values = list(timings.values())
            deltas = [values[i + 1] - values[i] for i in range(len(values) - 1)]
            print(deltas)
            epoch_list.append(map(lambda x: {"round": i, "secs": x.total_seconds() * 1000}, deltas))

        print(epoch_list)
    #    for i in range(len(epoch_list[0].values())):
    #        print(f"{i}: {sum([e.values()[i] for e in epoch_list]) / epochs}")

    def test_key(self):
        cache = RedisCache(host="localhost", port=6379, db=6)
        cache.set("key", "value")
        print(cache.get("key"))