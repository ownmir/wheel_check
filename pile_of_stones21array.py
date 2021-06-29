from sys import stdin
from array import array


def rec(n, s1, s2):
    global res, N, Pile
    #global res, common_sum
    # s2 = common_sum - s1
    # print('n', n, 's1', s1, 's2', s2, 'res', res)

    if n == N or res == 0:
        # print(True)
        cur_res = abs(s1 - s2)
        if cur_res < res:
            res = cur_res
        return
    # rec(n + 1, prom_s1, prom_s2, N, mas)
    rec(n + 1, s1 + Pile[n], s2)
    rec(n + 1, s1, s2 + Pile[n])

res = 2000000
N = int(next(stdin))
# N = 20
N = 5
# print('N', N, type(N))
# Pile = array('I', (int(x) for x in stdin.read().split()))
# Pile = [90000,80000,80000,70000,60000,50000,60000,10000,25000,35000,90000,12000,50000,56700,23000,745258,40000,13000,15610,86000]
# Pile = array('I', (90000,80000,80000,70000,60000,50000,60000,10000,25000,35000,90000,12000,50000,56700,23000,745258,40000,13000,15610,86000))
# Pile = [1, 4, 2, 3]
Pile = [5, 8, 13, 27, 14]
# Pile = array('I', (5, 8, 13, 27, 14,))
# print('Pile', Pile)

# Pile_s = stdin.read().split()
# Pile = []
# for it in Pile_s:
#     int_it = int(it)
#     Pile.append(int_it)
# common_sum = sum(Pile)
# common_sum = sum([90000,80000,80000,70000,60000,50000,60000,10000,25000,35000,90000,12000,50000,56700,23000,745258,40000,13000,15610,86000])
# rec(0, 0, 0)

print(res)
