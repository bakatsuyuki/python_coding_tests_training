import array
import time

import numpy as np

size = 10000
list = [1] * size
ar = array.array('b', [1] * size)
ndar = np.array(list)
st = ''.join(['a'] * 1000000)


def stop_watch(job, tag):
    start_at = time.time()
    for i in range(10000000):
        job()
    end_at = time.time()
    print(tag)
    print(end_at - start_at)


stop_watch(lambda: list[:30], 'list')
stop_watch(lambda: ar[:30], 'array')
stop_watch(lambda: ndar[:30], 'ndarray')
stop_watch(lambda: st[:30], 'string')
