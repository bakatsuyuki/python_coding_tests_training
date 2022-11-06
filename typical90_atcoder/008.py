n = int(input())
s = input()

mod = 10 ** 9 + 7

before_indexes = None
count = 1
all_index_maps = []

target_chars = 'atcoder'

s = ''.join([x for i, x in enumerate(s) if x in target_chars])
result_memo = {}
first_indexes = {}
last_indexes = {}
for char in target_chars:
    first_indexes[char] = s.index(char)
    last_indexes[char] = len(s) - 1 - list(reversed(target_chars)).index(char)


def count_alphabet_after_index(target_char_index, index):
    key = f'{target_char_index}-{index}'
    if target_char_index >= len(target_chars):
        return 1
    target_char = target_chars[target_char_index]
    if last_indexes[target_char] < index:
        return 0
    if key in result_memo:
        return result_memo[key]
    found_indexes = [i for i, x in enumerate(s[index:]) if x == target_char]
    result = 0
    for found_index in found_indexes:
        new_index = max([first_indexes[target_char], found_index + index + 1])
        result += count_alphabet_after_index(target_char_index + 1, new_index)
    result %= mod
    result_memo[key] = result
    return result


print(count_alphabet_after_index(0, 0))
