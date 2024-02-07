import sys
import numpy as np


def main():
    n = int(input())
    arr = np.array([list(map(int, input().split())) for _ in range(n)])
    arr_shift = np.roll(arr, 2)
    arr_shift[0] = np.array([0, 0])
    print(arr)
    print(arr_shift)


if __name__ == '__main__':
    main()
