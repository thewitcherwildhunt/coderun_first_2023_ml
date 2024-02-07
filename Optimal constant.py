import sys
import numpy as np


def main():
    n = int(input())
    arr = np.array([int(input()) for _ in range(n)])
    print(arr.mean())
    print(np.median(arr))


if __name__ == '__main__':
    main()
