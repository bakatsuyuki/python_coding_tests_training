import sys

n = int(input())
cp = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

sum_cache = {}


def lr_to_key(l, r):
    return l * 1000000 + r


def key_to_lr(key):
    return key // 1000000, key % 1000000


def cached_max_lr(l, r):
    max_lr = None
    max_range = -1
    for cached_l, cached_r in map(key_to_lr, sum_cache.keys()):
        if cached_l >= l and cached_r <= r and max_range < cached_r - cached_l:
            max_range = cached_r - cached_l
            max_lr = cached_l, cached_r
    return max_lr


def combine_results(l_result, r_result):
    return [l_result[0] + r_result[0], l_result[1] + r_result[1]]


def memo_sum(l, r):
    key = lr_to_key(l, r)
    if l > r or l < 0 or r < 0:
        return [0, 0]
    if key in sum_cache:
        return sum_cache[key]
    cached_lr = cached_max_lr(l, r)
    mid = (l + r) // 2
    if cached_lr:
        cached_l, cached_r = cached_lr
        cached_result = memo_sum(cached_l, cached_r)
        result = combine_results(cached_result,combine_results(memo_sum(l, cached_l - 1), memo_sum(cached_r + 1, r)))
    elif l == r:
        c, p = cp[l]
        if c == 1:
            result = [p, 0]
        else:
            result = [0, p]
    elif mid == l or mid == r:
        result = combine_results(memo_sum(l, l), memo_sum(r, r))
    else:
        result = combine_results(memo_sum(l, mid), memo_sum(mid + 1, r))
    sum_cache[key] = result
    return result


answers = [memo_sum(l - 1, r - 1) for l, r in lr]

sys.stdout.writelines('\n'.join(map(lambda points: f'{points[0]} {points[1]}', answers)))
