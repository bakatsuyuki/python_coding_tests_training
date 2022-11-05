import array
import time

import numpy as np

size = 10000
list = [1] * size
ar = array.array('b', [1] * size)
ndar = np.array(list)
st = ''.join(['a'] * 10000)


def stop_watch(job, tag):
    start_at = time.time()
    for i in range(10000000):
        job()
    end_at = time.time()
    print(tag)
    print(end_at - start_at)


stop_watch(lambda: list[50], 'list')
stop_watch(lambda: ar[50], 'array')
stop_watch(lambda: ndar[50], 'ndarray')
stop_watch(lambda: st[50], 'string')
