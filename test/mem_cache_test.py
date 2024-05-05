import unittest

from datetime import datetime
from cache import *
from test.helper import generate_samples

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)-10s [%(levelname)s] %(message)s")


class MemoryCacheTest(unittest.TestCase):

    def setUp(self):
        strs, samples = generate_samples()
        timing = {"init" : datetime.now()}
        mcache: AdtCache = MemoryCache()
        mcache.push_values("random_keys", strs)
        timing["push"] = datetime.now()
        for i, s in enumerate(samples):
            inter = mcache.intersect("random_keys", s)
            timing[f"intersect_{i}"] = datetime.now()

        self.timing = timing

    def test_memcache(self):
        epochs = 10
        epoch_list = []
        for i in range(epochs):
            timings = self.timing
            values = list(timings.values())
            deltas = [values[i + 1] - values[i] for i in range(len(values) - 1)]
            epoch_list.append(list(map(lambda x: x.total_seconds() * 1000, deltas)))

        for i in range(len(epoch_list[0])):
            print(f"{i}: {sum([e[i] for e in epoch_list]) / epochs}")

    def test_simple_operation(self):
        mcache: AdtCache = MemoryCache()
        mcache.push_values("key", ["value", "value2"])
        print(mcache.get("key"))

        inter = mcache.intersect("key", ["value2"])
        self.assertEqual(["value2"], inter)
        print("inter : ", inter)

        self.assertEqual(mcache.intersect("key2", []), [])