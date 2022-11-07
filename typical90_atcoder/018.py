import numpy as np


def calc_angle(a, b, c):
    vec_a = b - a
    vec_c = b - c

    cos = np.inner(vec_a, vec_c) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_c))
    rad = np.arccos(cos)
    return np.rad2deg(rad)
