n, k = map(int, input().split())
s = input()


def create_map(sub_s):
    s_index_map = {}
    for i in range(len(sub_s)):
        split_s = sub_s[i]
        if split_s not in s_index_map:
            s_index_map[split_s] = []
        s_index_map[split_s].append(i)
    return s_index_map


remain_char_count = n

sub_s = s
remain_n = n
remain_k = k

result = ''

for _ in range(k):
    s_index_map = create_map(sub_s)
    remain_n = len(sub_s)
    for i in range(97, 123):
        alphabet = str(chr(i))
        if alphabet in s_index_map and remain_n - remain_k - (min(s_index_map[alphabet])) >= 0:
            result = f'{result}{alphabet}'
            remain_k -= 1
            index = min(s_index_map[alphabet])
            sub_s = sub_s[index + 1:]
            break

print(result)
