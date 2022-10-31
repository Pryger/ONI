from config import *
import math

def get_distance(first, second):
    w = abs(alph[first]['x'] - alph[second]['x'])
    h = abs(alph[first]['y'] - alph[second]['y'])
    return round(math.sqrt(w*w + h*h), 4)


s = input()
print(get_distance(s[0], s[1]))