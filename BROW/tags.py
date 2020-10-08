def is_tag(sour):
    len_sour = len(sour)
    if len_sour < 3:
        # ваш tag не может быть менее 3-х символов
        return False
    first = sour[0]
    # print("first", first)
    if first != "<":
        # 
        return False
    last = sour[-1]
    if last != ">":
        return False
    # print("last", last)
    
    return True

if __name__ == "__main__":
    sour = "<b>"
    print(is_tag(sour))

