'''
给定整数n,求离根号n最近的整数。
'''
import numpy as np

def bin_search_sqrt(num):
    left, right = 0, num
    while right - left > 1:
        mid = (left + right) // 2
        if mid ** 2 > num:
            right = mid
        else:
            left = mid
    return right if right ** 2 - num < num - left ** 2 else left


if __name__ == '__main__':

    n = 17
    print(bin_search_sqrt(n), np.sqrt(n))