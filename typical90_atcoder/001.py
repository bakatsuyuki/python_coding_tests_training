n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
pieces = []
for i in range(n):
    if i == 0:
        pieces.append(a[i])
    else:
        pieces.append(a[i] - a[i - 1])
pieces.append(l - a[n - 1])

for _ in range(n - k):
    min_piece_index = pieces.index(min(pieces))


    def combine_pieces(target_index):
        pieces[min_piece_index] += pieces[target_index]
        del pieces[target_index]


    if min_piece_index == 0:
        combine_pieces(min_piece_index + 1)
    elif min_piece_index == len(pieces) - 1:
        combine_pieces(min_piece_index - 1)
    elif pieces[min_piece_index - 1] > pieces[min_piece_index + 1]:
        combine_pieces(min_piece_index + 1)
    else:
        combine_pieces(min_piece_index - 1)
print(min(pieces))
