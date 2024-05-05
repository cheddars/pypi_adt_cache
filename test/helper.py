import random

import string


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