from dfs import *
from yaku_funs import *
from funs import convert_hc_to_list,trimed_mentsu

def yaku(hc_list, ronhai):
    hc_list = hc_list.copy()
    hc_list[ronhai] += 1
    mentsu_list = get_mentsu(hc_list)
    mentsu_list = [x for x in mentsu_list if len(x) == 4]

    # 胡牌可能面子及雀頭組合
    ron_mentsu_list = []
    for m_list in mentsu_list:
        trimed_hc_list = trimed_mentsu(hc_list, m_list)
        if trimed_hc_list.count(2) == 1:
            ron_mentsu_list.append((m_list,trimed_hc_list.index(2))) # ([(0,1,0),(9,1,0),(18,1,0),(27,0,1)], 28)

    # 不要求胡牌型式的役種
    hc_index_set = {i for i,value in enumerate(hc_list) if value > 0}
    if ryuuiisoo(hc_index_set):
        print("綠一色")
    if tsuuiisoo(hc_index_set):
        print("字一色")
    if chinrootoo(hc_index_set):
        print("清老頭")
    if honroutoo(hc_index_set):
        print("混老頭")
    if chinitsu(hc_index_set):
        print("清一色")
    if honitsu(hc_index_set):
        print("混一色")
    if tanyao(hc_index_set):
        print("斷么九")

    # len(ron_mentsu_list) == 0，代表非一般型役種
    if len(ron_mentsu_list) == 0:
        if kokushi(hc_list):
            if hc_list.index(2) == ronhai:
                print("国士無雙十三面")
            else:
                print("国士無雙")
        if chuurenpoutoo(hc_list):
            if chuurenkyuumenmachi(hc_list, ronhai):
                print("純正九蓮宝燈")
            else:
                print("九蓮宝燈")
        if chitoi(hc_list):
            print("七對子")
    
    # 一般型役種
    for ron_m_list in ron_mentsu_list:
        pass
    

yaku(convert_hc_to_list("123m123p123s1112z"),28)