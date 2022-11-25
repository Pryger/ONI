from alph import *
import math


def check_password(num, alph, correct_password):
    len_alph = len(alph)
    size = list()
    while num > 0:
        size.append(num % len_alph)
        num = num // len_alph

    string = ''.join(list(map(lambda x: alph[x], size)))
    return string if string == correct_password else False


def create_distance_list(char, alph):
    distance = list()
    for a in alph:
        distance.append({'char': a, 'distance': get_distance(char, a)})

    distance_sorted = sorted(distance, key=lambda x: x['distance'])
    alph_sorted = list(map(lambda x: x['char'], distance_sorted))
    return list(reversed(alph_sorted))


def get_distance(first, second):
    first, second = first.lower(), second.lower()
    w = abs(alph[first]['x'] - alph[second]['x'])
    h = abs(alph[first]['y'] - alph[second]['y'])
    return round(math.sqrt(w*w + h*h), 4)