h, w = map(int, input().split())
q_count = int(input())
q = [list(map(int, input().split())) for _ in range(q_count)]

red_points_map = {}


def point_to_key(r, c):
    return f'{r} {c}'


def key_to_point(key):
    return map(int, key.split())


def query_1(arguments):
    r, c = arguments
    keys = [point_to_key(r + 1, c), point_to_key(r, c + 1), point_to_key(r - 1, c), point_to_key(r, c - 1)]

    new_list = [arguments]
    red_points_map[point_to_key(r, c)] = new_list
    for key in keys:
        if key in red_points_map:
            new_list.extend(red_points_map[key])
            for point in red_points_map[key]:
                red_points_map[point_to_key(point[0], point[1])] = new_list


def query_2(arguments):
    ra, ca, rb, cb = arguments
    key_a = point_to_key(ra, ca)
    key_b = point_to_key(rb, cb)
    if key_a in red_points_map and key_b in red_points_map and red_points_map[key_a] == red_points_map[key_b]:
        print('Yes')
    else:
        print('No')


for query in q:
    if query[0] == 1:
        query_1(query[1:])
    if query[0] == 2:
        query_2(query[1:])
