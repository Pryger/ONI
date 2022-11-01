from alph import *
import math

def get_distance(first, second):
    w = abs(alph[first]['x'] - alph[second]['x'])
    h = abs(alph[first]['y'] - alph[second]['y'])
    return round(math.sqrt(w*w + h*h), 4)

def next_step(arr):
    for i, item in enumerate(arr):
        if arr[i] + 1 == 129 and i != 0:
            arr[i] = 32
            arr[i - 1] += 1
    arr[-1] += 1
    return arr

def ch2int_arr(arr):
    return list(map(lambda x: ord(x), arr))

def int2ch_arr(arr):
    return ''.join(list(map(lambda x: chr(x), arr)))