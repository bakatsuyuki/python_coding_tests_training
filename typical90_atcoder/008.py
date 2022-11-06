n = int(input())
s = input()

mod = 10 ** 9 + 7

before_indexes = None
count = 1
all_index_maps = []

target_chars = list('atcoder')

result_memo = {}


# [i for i, x in enumerate(s) if x == target_char]

def count_alphabet_after_index(target_char_index, index):
    key = f'{target_char_index}-{index}'
    if key in result_memo:
        return result_memo[key]
    if target_char_index >= len(target_chars):
        return 1

    target_char = target_chars[target_char_index]

    found_indexes = [i for i, x in enumerate(s[index:]) if x == target_char]
    result = 0
    for found_index in found_indexes:
        result += count_alphabet_after_index(target_char_index + 1, found_index + index + 1)
    result %= mod
    result_memo[key] = result
    return result


print(count_alphabet_after_index(0, 0))
