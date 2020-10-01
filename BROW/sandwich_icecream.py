def is_it(sour):
    len_sour = len(sour)
    if len_sour < 3:
        # ваш сэндвич не может быть менее 3-х символов
        return False
    first = sour[0]
    # print("first", first)
    last = sour[-1]
    # print("last", last)
    if first != last:
        # вы не можете иметь только мороженное (без сэндвича)
        return False
    set_sour = set(sour)
    # print("set_sour", set_sour)
    len_set = len(set_sour)
    if len_set > 2 or len_set == 1:
        # вы не можете иметь начинку из разных символов
        return False
    # second = list(set_sour)[1] - не работает, так как множество А,С или С,А
    for ch in sour:
        if ch != first:
            second = ch
            break
    # print("Second char", second)
    left_count = sour.count(first, 0, sour.index(second))
    
    right_count = sour.count(first, sour.index(second))
    # print("left_count", left_count, "right_count", right_count, "sour.index(second)", sour.index(second))
    if left_count != right_count:
        # вы не можете иметь неравные окончания в сэндвиче
        return False
    return True

if __name__ == "__main__":
    sour = "AABBABBAA"
    print(is_it(sour))

