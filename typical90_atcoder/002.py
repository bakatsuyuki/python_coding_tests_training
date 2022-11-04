n = int(input())
if n % 2 == 1:
    exit()

brackets_count_max = int(n / 2)


def dps(sentence):
    if len(sentence) == n:
        print(sentence)
        return

    left_count = sentence.count('(')
    right_count = sentence.count(')')
    if left_count < brackets_count_max:
        dps(f'{sentence}(')
    if left_count > right_count:
        dps(f'{sentence})')


dps('(')
