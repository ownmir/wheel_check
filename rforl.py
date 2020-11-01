def create_tag(tag, addbegin="", addend=""):
    """
    Возвращает начальный таг addbegin<tag>addend
    """
    return "{}<{}>{}".format(addbegin, tag, addend)
def create_end_tag(tag, addbegin="", addend=""):
    """
    Возвращает конечный таг addbegin</tag>addend
    """
    return "{}</{}>{}".format(addbegin, tag, addend)
def read_for_learn(s_row):
    # t = tuple()
    by_words = s_row.split()
    
    t = tuple(map(lambda x: x + ".", by_words))
    # full = map(lambda x: x + ",", by_words)
    l = len(t)
    for tm in t:
        # l += 1
        if len(tm) > 3:
            print(tm)
    with open("C:\\Users\\ownmi\\Documents\\PRECIS\\Eth\\sentence.html", "w", encoding="utf-8") as f:
        f.write(create_tag("html", addend="\n"))
        f.write(create_tag("head", addbegin="\t", addend="\n"))
        f.write(create_tag("title", addbegin="\t\t", addend="Split sentence"))
        f.write(create_end_tag("title", addbegin="\t\t", addend="\n"))
        f.write(create_end_tag("head", addbegin="\t", addend="\n"))
        f.write(create_tag("body", addbegin="\t", addend="\n"))
        # l = len(t)
        if l < 6:
            for i in range(1, l+1):
                word = t[i-1]
                if len(word) > 4:
                    f.write(create_tag("H{}".format(i), addbegin="\t\t", addend="\n"))
                    f.write("\t\t\t{}\n".format(word))
                    f.write(create_end_tag("H{}".format(i), addbegin="\t\t", addend="\n"))
        else:
            for i in range(1, 6):
                word = t[i-1]
                if len(word) > 4:
                    f.write(create_tag("H{}".format(i), addbegin="\t\t", addend="\n"))
                    f.write("\t\t\t{}\n".format(t[i-1]))
                    f.write(create_end_tag("H{}".format(i), addbegin="\t\t", addend="\n"))
            for i in range(6, l+1):
                word = t[i-1]
                if len(word) > 4:
                    f.write(create_tag("P", addbegin="\t\t", addend="\n"))
                    f.write("\t\t\t{}\n".format(t[i-1]))
                    f.write(create_end_tag("P", addbegin="\t\t", addend="\n"))
        f.write(create_tag("H5", addbegin="\t\t", addend="\n"))
        for tm in by_words:
            f.write("\t\t\t{},".format(tm))
        f.write(create_end_tag("H5", addbegin="\t\t", addend="\n"))    
        f.write(create_end_tag("body", addbegin="\t", addend="\n"))
        f.write(create_end_tag("html", addend="\n"))
        
if __name__ == '__main__':
    import sys
    read_for_learn(sys.argv[1])
