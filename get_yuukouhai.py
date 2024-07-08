from dfs import *
from funs import *


# 計算13張牌的向聽数 syanten
def calc_syanten_13(hc_list):
    # 判斷是否為13張牌
    if sum(hc_list) != 13:
        raise ValueError("請傳入13張牌")
    mentsu_list = get_mentsu(hc_list)
    # 若沒有面子，則生成空列表
    if not mentsu_list:
        mentsu_list = [[]]
    # 最大8向聽
    syanten_list =[[]for i in range(8)]
    min_syanten = 999

    # 七對子向聽數
    syanten,yuukouhai = chitoitsu(hc_list)
    syanten_list[syanten] += yuukouhai
    min_syanten = min(min_syanten, syanten)

    # 國士無雙向聽數
    syanten,yuukouhai = kokushi(hc_list)
    syanten_list[syanten] += yuukouhai
    min_syanten = min(min_syanten, syanten)

    # 一般型最小向聽數
    for m_list in mentsu_list:
        mentsu_count = len(m_list)
        trimed_hc = trimed_mentsu(hc_list.copy(), m_list) # 去除面子
        taatsu_list = get_taatsu(trimed_hc)
        for d_list in taatsu_list:
            # 是否有雀頭 jantou
            jantou = 0
            for taatsu in d_list:
                if taatsu[1] > 0:
                    jantou = 1
                    break
            taatsu_count = len(d_list)
            syanten = calc_syanten(mentsu_count, taatsu_count, jantou) # 去除塔子

            if syanten <= min_syanten:
                trimed_twice_hc = trimed_taatsu(trimed_hc, d_list)
                # 孤立牌 koritsuhai
                koritsuhai = get_koritsuhai(trimed_twice_hc)
                # 有效牌 yuukouhai
                yuukouhai = get_yuukouhai_from_taatsu(d_list, syanten, mentsu_count, taatsu_count, jantou, trimed_twice_hc, koritsuhai)
                syanten_list[syanten] += yuukouhai

    for x in range(len(syanten_list)):
        if syanten_list[x]:
            return (x,list(set(syanten_list[x])))


# 一般型牌理分析
def calc_syanten_14(hc_list):
    if sum(hc_list) != 14:
        raise ValueError("請傳入14張牌")
    sianten_list = []
    for x in range(len(hc_list)):
        if hc_list[x] > 0:
            # 依序切出一張牌，並檢查向聽數
            hc_list[x] -= 1
            sianten = calc_syanten_13(hc_list)
            if sianten:
                sianten_list.append([x, sianten])
            # 恢復手牌
            hc_list[x] += 1
    # 最小向聽數
    min_sianten = min([x[1][0] for x in sianten_list])
    if min_sianten == 0:
        print("聽牌\n")
    else:
        print("{}向聽\n".format(min_sianten))
    card_advice_list = []
    for x_sianten in sianten_list:
        sianten = x_sianten[1]
        if sianten[0] == min_sianten:
            sianten[1].sort()
            yuukouhai_count = calc_yuukouhai_sum(hc_list, sianten[1])
            card_advice_list.append([x_sianten[0], sianten[1], yuukouhai_count])
    card_advice_list.sort(key=lambda x: x[2], reverse=True)
    for x in card_advice_list:
        print("打{}  摸:{}  {}枚\n".format(convert_index_to_cardname(x[0]), [convert_index_to_cardname(x) for x in x[1]], x[2]))
    if not sianten:
        print("出現錯誤")

calc_syanten_14(convert_hc_to_list("1199m1199p1199s11z"))