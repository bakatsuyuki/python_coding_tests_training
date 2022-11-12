n = int(input())
s = [input() for _ in range(n)]

char_set = set()
first_char = ['H', 'D', 'C', 'S']
second_char = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

is_no = False
for s_child in s:
    if s_child[0] not in first_char or s_child[1] not in second_char or s_child in char_set:
        is_no = True
        break
    char_set.add(s_child)

if is_no:
    print('No')
else:
    print('Yes')
