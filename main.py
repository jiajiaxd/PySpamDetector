def spamdetector(s: str):
    strlist = list(s)
    strset = set(s)
    strlen = len(s)
    # 全部均为重复字符：
    if len(strset) == 1:
        return True

    # 整个字符中某一字符节大量重复
    for i in range(2, int(strlen / 2 + 1)):
        if strlen % i != 0:
            continue
        else:
            j = list()
            for k in range(0, int(strlen / i)):
                j.append(s[k * i: (k + 1) * i])
            if len(set(j)) == 1:
                return True

    # 某个字符占了整个字符串的90%
    strnum = dict()
    for i in strset:
        strnum[i] = 0
    for i in strlist:
        strnum[i] += 1
    for i in strnum.keys():
        if strnum[i] / strlen >= 0.90:
            return True
    return False


if __name__ == '__main__':
    print(spamdetector(input("输入一个字符串以进行判断：")))
