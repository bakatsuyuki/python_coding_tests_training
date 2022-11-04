import math
import sys
import modint
import numpy
import numpy as np
from fractions import Fraction


def problem_a():
    n = int(input())
    h_list = list(map(int, input().split(' ')))
    max_h = 0
    max_i = -1
    for i in range(n):
        if h_list[i] > max_h:
            max_h = h_list[i]
            max_i = i
    print(max_i + 1)


def problem_b():
    a, b, c, d, e, f = list(map(int, input().split(' ')))
    target = a * b * c - d * e * f
    print(target % 998244353)


def problem_c():
    s = []
    for i in range(9):
        s.append(list(input()))

    porn_positions = list()
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                porn_positions.append([i, j])

    square_count = 0
    for i in range(len(porn_positions)):
        a_position = porn_positions.pop()
        for b_position in porn_positions:
            x_dif = b_position[0] - a_position[0]
            y_dif = b_position[1] - a_position[1]
            x_adjust = y_dif
            y_adjust = abs(x_dif)
            c_position = [a_position[0] + x_adjust, a_position[1] + y_adjust]
            d_position = [b_position[0] + x_adjust, b_position[1] + y_adjust]
            if c_position in porn_positions and d_position in porn_positions:
                square_count += 1


dps_map = {}


def problem_d():
    n = int(input())
    print(dps(n))


def dps(n: int):
    if n in dps_map:
        return dps_map[n]
    if n == 0:
        return 1
    dps_map[n] = dps(math.floor((n / 2))) + dps(math.floor((n / 3)))
    return dps_map[n]


def problem_e():
    n, m, k = list(map(int, input().split(' ')))
    before_count_at_positions = {}
    for i in range(k):
        current_count_on_positions = {}
        if i == 0:
            for number in range(m):
                before_count_at_positions[number + 1] = 1
            continue
        for j in range(n):
            target_position = j + 1
            current_count_on_positions[target_position] = 0
            if target_position == n and n in before_count_at_positions:
                current_count_on_positions[n] = before_count_at_positions[n]
            for before_position in before_count_at_positions:
                if before_position == n:
                    continue
                count = before_count_at_positions[before_position]
                # print(f'{before_position}=>{target_position}')
                if can_reach_with_advance(before_position, target_position, m):
                    current_count_on_positions[target_position] += count
                if can_reach_with_back(before_position, target_position, m, n):
                    current_count_on_positions[target_position] += count
                    # print('バック')
                # print()
        before_count_at_positions = current_count_on_positions
    print(sum(before_count_at_positions.values()))
    z = p_mod(before_count_at_positions[n], sum(before_count_at_positions.values()))
    print(z)


def p_mod(numerator, denominator):
    mod = 998244353
    x_per_y = Fraction(numerator, denominator)
    return x_per_y.numerator * pow(x_per_y.denominator, mod - 2, mod) % mod


def can_reach_with_advance(before_position, target_position, m):
    return before_position < target_position <= m + before_position


def can_reach_with_back(before_position, target_position, m, n):
    return n - m < target_position < n and 2 * n - before_position - target_position <= m


def problem_e_sample():
    n, m, k = map(int, input().split())
    mod = 998244353
    # Mのmod上での逆数
    m_inv = pow(m, mod - 2, mod)

    # dpテーブルをnumpy.ndarrayとして持つ
    # dp[i] = (マスiからK回以内にゴールできる確率)
    dp = np.zeros(shape=n + 1, dtype='i4')
    dp[-1] = 1
    # K回遷移を行う
    for _ in range(k):
        print('ここ')
        dp[:-1] = np.convolve(
            a=np.append(arr=dp[1:], values=dp[-2:-(m + 1):-1]),
            v=np.full(shape=m, fill_value=1),
            mode='valid'
        ) % mod
    print(dp[0])


def problem_f():
    n, m = map(int, input().split())
    a = np.array(map(int, input().split()))
    a_sum = sum(a)
    for i in range(m):
        for j in range(a):
            for k in range(n - j):
                if i == a_sum - sum(a[j:j + k]):
                    return


def problem_37():
    n, m = map(int, input().split())
    maze = numpy.empty([n, m], dtype=object)
    for i in range(n):
        maze[i] = list(input())

    sx_array, sy_array = np.where(maze == 'S')
    gx_array, gy_array = np.where(maze == 'G')
    sx, sy, gx, gy = sx_array[0], sy_array[0], gx_array[0], gy_array[0]

    maze[sx][sy] = 0
    loop_queue = [[sx, sy]]
    already_goal = False
    while loop_queue and not already_goal:
        x, y = loop_queue.pop(0)
        count = int(maze[x][y]) + 1

        for position in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            ix, iy = position
            if ix < 0 or ix >= n or iy < 0 or iy >= m:
                continue
            if maze[ix][iy] == '.':
                maze[ix][iy] = count
                loop_queue.append([ix, iy])
            if maze[ix][iy] == 'G':
                print(count)
                already_goal = True


def problem_typical90_001():
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


if __name__ == '__main__':
    problem_typical90_001()
