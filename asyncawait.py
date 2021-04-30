import asyncio
import time

async def nsum(l_arg):
    # await asyncio.sleep(0.1)
    return sum(l_arg)

async def sub_case(l_arg, cur_min, len_list):
    #len_list = len(list_num)
    for n in range(1, len_list):
        print("n", n, "cur_min", cur_min)
        task1 = asyncio.create_task(nsum(list_num[:n]))
        task2 = asyncio.create_task(nsum(list_num[n:]))
        await task1
        await task2
        result1 = task1.result()
        print(result1)
        result2 = task2.result()
        print(result2)
        diff = abs(result1 - result2)
        if diff == 0:
            print(0)
            print(f"finished at {time.strftime('%X')}")
            return
        if diff < cur_min:
            cur_min = diff
    return cur_min
    

# https://prog-cpp.ru/permutation/
def swap(list_num, i, j):
    s = list_num[i]
    list_num[i] = list_num[j]
    a[j] = s


def next_set(list_num, len_list):
    j = len_list -2
    while j != -1 and list_num[j] >= list_num[j + 1]:
        j -= 1
    if j == -1:
        return False  # больше перестановок нет
    k = len_list - 1
    while list_num[j] >= list_num[k]:
        k -= 1
    swap(list_num, j, k)
    l = j = 1
    r = n - 1  # сортируем оставшуюся часть последовательности
    while l < r:
        swap(list_num, l, r)
        l += 1
        r -= 1
    return True


async def main():
    print(f"started at {time.strftime('%X')}")
    # list_num = [50000, 80000, 13000, 27000, 14000, 78123, 12987, 98010, 15900, 1001, 56800, 80001, 13800, 27012, 14000, 78123, 12987, 98010, 15900, 1001]
    list_num = [5, 8, 13, 27, 14]
    len_list = len(list_num)
    cur_min = 2000000
    while next_set(list_num, len_list):
        task_sub_case = asyncio.create_task(sub_case(list_num, cur_min, len_list))
        cur_min = task_sub_case.result()
    
    print("cur_min", cur_min)
        
    # Вернуть сумму первых n аргументов из N
    #print(await nsum(list_num[:1]))
    # Вернуть сумму последних LEN - n аргументов
    #print(await nsum(list_num[1:]))
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


