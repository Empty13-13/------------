import random
import numpy as np
import math


# Функции помощники
def __generateLineImg():
    a = np.array([0, 0, 0])
    b = np.array([255, 255, 255])

    line = np.array([0, 0, 0])
    if random.randrange(0, 2):
        line = np.array([255, 255, 255])

    for i in range(15):
        if random.randrange(0, 2):
            line = np.row_stack((b, line))
        else:
            line = np.row_stack((a, line))

    return line


def __generate16x16():
    arr = []
    for i in range(16):
        arr.append(__generateLineImg())
    return np.array(arr).astype(np.uint8)


def __copy4img(arr):
    arr90 = np.rot90(arr)
    arr = np.row_stack((arr, arr90))
    arr = np.column_stack((arr, np.rot90(np.rot90(arr))))
    return arr


def generateKey():
    arr = __generate16x16()
    return __copy4img(arr)


# Функции помощники для встраивания ЦВЗ
def __W(n, m, W, K, L):
    # print(W[math.floor(n/L), math.floor(m/L)],
    #      K[math.floor(n/L), math.floor(m/L)])
    return W[math.floor(n/L), math.floor(m/L)] ^ K[math.floor(n/L), math.floor(m/L)]


# Функция встраивания ЦВЗ
def generateWithDWM(main, dwm, key, q):
    L = len(dwm)
    N = len(dwm)
    # mainResult = np.round(main/q).astype(np.uint8)
    print('yes', main[0][0][0])
    print('no',  main[399][399][0])
    for n, item in enumerate(main):
        for m, item in enumerate(item):
            if __W(n, m, dwm, key, L)[i] > 127:
                # main[n][m][i] = math.floor( main[n][m][i]/q) + (q/2) + (main[n][m][i] % (q/2))
                print(int(main[n][m][i])/q)
                pass
            else:
                pass
                # main[n][m][i] = math.floor(int(main[n][m][i]) / q) + (main[n][m][i] % (q/2))
            # print('')
    print('Встраивание завершено')
    # print(__W(0, 0, dwm, key, L))
