h, w = map(int, input().split())
q_count = int(input())
q = [list(map(int, input().split())) for _ in range(q_count)]

board = [[False] * (h + 1) for _ in range(w + 1)]


def query_1(arguments):
    r, c = arguments
    board[r][c] = True


def query_2(arguments):
    ra, ca, rb, cb = arguments
    if board[ra][ca] and board[rb][cb]:
        print('Yes')
    else:
        print('No')


for query in q:
    if query[0] == 1:
        query_1(query[1:])
    if query[0] == 2:
        query_2(query[1:])
