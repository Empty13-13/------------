import random
import numpy as np


def generateLineImg():
    a = np.array([0, 0, 0])
    b = np.array([255, 255, 255])

    line = np.array([0, 0, 0])
    if random.randrange(0, 2):
        line = np.array([255, 255, 255])

    for i in range(16):
        if random.randrange(0, 2):
            line = np.row_stack((b, line))
        else:
            line = np.row_stack((a, line))

    return line


def generate16x16():
    arr = []
    for i in range(16):
        arr.append(generateLineImg())
    return np.array(arr).astype(np.uint8)


def generateWithDWM(main, dwm, key):
    pass
