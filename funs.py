import re,math


# 將字符串手牌轉為列表
def convert_hc_to_list(hc: str) -> list:
    if not hc:
        raise ValueError
    # 赤寶牌處理
    hc = hc.replace("0", "5")
    hc_list = [0] * 34
    pattern = re.compile(r"\d+[mspz]")
    result = pattern.findall(hc)
    for x in result:
        if x[-1] == "m":
            for y in x[:-1]:
                hc_list[int(y) - 1] += 1
        if x[-1] == "p":
            for y in x[:-1]:
                hc_list[int(y) - 1 + 9] += 1
        if x[-1] == "s":
            for y in x[:-1]:
                hc_list[int(y) - 1 + 18] += 1
        if x[-1] == "z":
            for y in x[:-1]:
                hc_list[int(y) - 1 + 27] += 1
    return hc_list

# 檢測特殊役種七對子向聽、待牌
def chitoitsu(hc_list):
    toiitsu = 0
    yuukouhai = []
    for x in range(34):
        if hc_list[x] == 2:
            toiitsu += 1
        elif hc_list[x] == 1:
            yuukouhai.append(x)
    syanten = 6 - toiitsu
    return (syanten, yuukouhai)

# 檢測特殊役種國士無雙向聽、待牌
def kokushi(hc_list):
    yaochu = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]
    yuukouhai = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]
    yaochu_count = 0
    toiitsu = 0
    for x in yaochu:
        if hc_list[x] >= 1:
            yaochu_count += 1
            yuukouhai.remove(x)
            if hc_list[x] >= 2:
                toiitsu = 1
    # 全部13張么九牌都有就是國士無雙十三面
    if yaochu_count == 13:
        return (0, yaochu)
    #普通的國士無雙
    syanten = 13 - toiitsu - yaochu_count
    return (syanten, yuukouhai)

# 從手牌中減去面子牌
def trimed_mentsu(hc_list, m_list):
    hc_list = hc_list.copy()
    for mentsu in m_list:
        index = mentsu[0]
        if mentsu[1] > 0:
            hc_list[index] -= 1
            hc_list[index + 1] -= 1
            hc_list[index + 2] -= 1
        elif mentsu[2] > 0:
            hc_list[index] -= 3
    return hc_list

# 從手牌中加上面子牌
def add_mentsu(hc_list, m_list):
    hc_list = hc_list.copy()
    for mentsu in m_list:
        index = mentsu[0]
        if mentsu[1] > 0:
            hc_list[index] += 1
            hc_list[index + 1] += 1
            hc_list[index + 2] += 1
        elif mentsu[2] > 0:
            hc_list[index] += 3
    return hc_list

# 從手牌中減去塔子牌
def trimed_taatsu(hc_list, d_list):
    hc_list = hc_list.copy()
    for taatsu in d_list:
        index = taatsu[0]
        if taatsu[1] > 0:
            hc_list[index] -= 2
        elif taatsu[2] > 0:
            hc_list[index] -= 1
            hc_list[index + 1] -= 1
        elif taatsu[3] > 0:
            hc_list[index] -= 1
            hc_list[index + 2] -= 1
    return hc_list

# 向聽計算公式
def calc_syanten(m, d, jantou):
    # c 超載數/ q 雀頭數
    if m + d <= 5:
        c = 0 
    else:
        c = m + d - 5

    if m + d <= 4:
        q = 1
    else:
        if jantou:
            q = 1
        else:
            q = 0

    syanten = 9 - 2 * m - d + c - q
    return syanten

# 孤立牌獲取
def get_koritsuhai(hc_list):
    koritsuhai_list = []
    for x in range(34):
        if hc_list[x] == 1:
            koritsuhai_list.append(x) # koritsuhai_list = [3,8,22,...]
    return koritsuhai_list

# 獲取孤立牌附近能组成塔子的牌
def get_koritsuhai_around(koritsuhai_list: list):
    koritsuhai_around = [] # 獲取孤立牌附近能组成塔子的牌(有效牌)
    for koritsuhai in koritsuhai_list:
        if koritsuhai < 27:
            for x in [koritsuhai - 2, koritsuhai - 1, koritsuhai + 1, koritsuhai + 2]:
                if x >= 0 and math.floor(x / 9) == math.floor(koritsuhai / 9):
                    koritsuhai_around.append(x) # koritsuhai_around = [3,4,6,7,...]
    return koritsuhai_around

# 根據塔子和當前向聽數 返回能夠減少向聽數的牌(有效牌)
def get_yuukouhai_from_taatsu(d_list, syanten, mentsu_count, taatsu_count, jantou, trimed_twice_hc_list, koritsuhai):
    # taatsu = [(2, 1, 0, 0), (18, 0, 0, 1)]
    yuukouhai = []
    # 向聽數為0
    if syanten == 0:
        if not d_list:
            yuukouhai += koritsuhai
        elif len(d_list) == 2:
            if d_list[0][1] > 0 and d_list[1][1] > 0:
                yuukouhai.append(d_list[0][0])
                yuukouhai.append(d_list[1][0])
            else:
                for taatsu in d_list:
                    index = taatsu[0]
                    # [11]
                    if taatsu[2] > 0:
                        if index in [0, 9, 18]:
                            yuukouhai.append(index + 2)
                        elif index in [7, 16, 25]:
                            yuukouhai.append(index - 1)
                        else:
                            yuukouhai.append(index - 1)
                            yuukouhai.append(index + 2)
                    # [101]
                    if taatsu[3] > 0:
                        yuukouhai.append(index + 1)
        return yuukouhai
    # 1向聽及以上
    for taatsu in d_list:
        index = taatsu[0]
        # [2]
        if taatsu[1] > 0:
            yuukouhai.append(index)
        # [11]
        if taatsu[2] > 0:
            if index in [0, 9, 18]:
                yuukouhai.append(index + 2)
            elif index in [7, 16, 25]:
                yuukouhai.append(index - 1)
            else:
                yuukouhai.append(index - 1)
                yuukouhai.append(index + 2)
        # [101]
        if taatsu[3] > 0:
            yuukouhai.append(index + 1)
    # 向聽數為1
    if syanten == 1:
        if taatsu_count == 1:
            if jantou:
                koritsuhai_around = get_koritsuhai_around(koritsuhai)
                yuukouhai += koritsuhai_around
                yuukouhai += koritsuhai
            else:
                yuukouhai += koritsuhai
        if taatsu_count == 2:
            for taatsu in d_list:
                index = taatsu[0]
                if taatsu[1] > 0:
                    yuukouhai.append(index)
                elif taatsu[2] > 0:
                    yuukouhai.append(index)
                    yuukouhai.append(index + 1)
                elif taatsu[3] > 0:
                    yuukouhai.append(index)
                    yuukouhai.append(index + 2)
    # 向聽數為2以上
    if syanten >= 2:
        if mentsu_count + taatsu_count < 5:
            # 4塔子0雀頭, 不需要新的塔子(顺子型)
            if mentsu_count + taatsu_count == 4 and not jantou:
                less_than_5 = get_md_less_than_5(trimed_twice_hc_list,0)
                yuukouhai += less_than_5
            # 需要新的塔子
            else: 
                less_than_5 = get_md_less_than_5(trimed_twice_hc_list,1)
                yuukouhai += less_than_5
        else: # mentsu_count + taatsu_count >= 5
            # 超載時 塔子自身可以化為雀頭 孤立牌也可以
            if not jantou:
                for taatsu in d_list:
                    index = taatsu[0]
                    if taatsu[1] > 0:
                        yuukouhai += [index]
                    elif taatsu[2] > 0:
                        yuukouhai += [index]
                        yuukouhai += [index+1]
                    elif taatsu[3] > 0:
                        yuukouhai += [index]    
                        yuukouhai += [index+2]
                yuukouhai += koritsuhai

    yuukouhai = list(set(yuukouhai))
    yuukouhai.sort()
    return yuukouhai


# m+d < 5時 減少向聽數的進張
def get_md_less_than_5(hc_list, new_taatsu = 1):
    koritsuhai_list = []
    for x in range(34):
        if hc_list[x] == 1:
            koritsuhai_list.append(x)
            if x < 27 and new_taatsu:
                for y in [x - 2, x - 1, x + 1, x + 2]:
                    if y >= 0 and math.floor(y / 9) == math.floor(x / 9):
                        koritsuhai_list.append(y)
    return koritsuhai_list

# 計算枚數
def calc_yuukouhai_sum(hc_list, yuukouhai):
    yuukouhai_count = 0
    for x in yuukouhai:
        yuukouhai_count += 4 - hc_list[x]
    return yuukouhai_count

# 根據索引返回牌名
def convert_index_to_cardname(num: int):
    cardname = None
    if num < 9:
        cardname = str(num + 1) + "万"
    elif 9 <= num < 18:
        cardname = str(num - 9 + 1) + "条"
    elif 18 <= num < 27:
        cardname = str(num - 18 + 1) + "筒"
    else:
        cardname = ["东", "南", "西", "北", "白", "发", "中"][num - 27]
    return cardname