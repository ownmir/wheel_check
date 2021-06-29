from sys import stdin
from array import array


def rec(n, s1, s2):
    global res, N, Pile

    if n == N or res == 0:
        # print(True)
        cur_res = abs(s1 - s2)
        if cur_res < res:
            res = cur_res
        return

    rec(n + 1, s1 + Pile[n], s2)
    rec(n + 1, s1, s2 + Pile[n])

res = 2000000
N = int(input())
Pile = array('I', (int(x) for x in input().split()))
rec(0, 0, 0)
print(res)
