from dfs import *
from yaku_funs import *
from funs import convert_hc_to_list,trimed_mentsu,add_mentsu

# nakipai = [[(0,1,0), 1-4, 1-4], ...] (吃 碰 槓 暗槓 , 上家 對家 下家 自家)
def yaku(hc_list, ronhai, nakipai_list=[],tsumo=False):
    hc_list = hc_list.copy()
    hc_list[ronhai] += 1
    mentsu_list = get_mentsu(hc_list)

    naki_list = [x[0] for x in nakipai_list] # 精簡鳴牌列表
    hc_list = add_mentsu(hc_list,naki_list)
    mentsu_list = [x + naki_list for x in mentsu_list if len(x)+len(naki_list) == 4]
    

    # 胡牌可能面子及雀頭組合
    ron_mentsu_list = []
    for m_list in mentsu_list:
        trimed_hc_list = trimed_mentsu(hc_list, m_list)
        if 2 in trimed_hc_list:
            jantou = trimed_hc_list.index(2)
            ron_mentsu_list.append((m_list,jantou)) # [([(0,1,0),(9,1,0),(18,1,0),(27,0,1)], 28), ...]

    # 不要求胡牌型式的役種
    hc_index_set = {i for i,value in enumerate(hc_list) if value > 0}
    if kokushimusoujuusanmenmachi(hc_index_set,hc_list,ronhai):
        print("国士無雙十三面")
    elif kokushimusou(hc_index_set):
        print("国士無雙")
    if chuurenkyuumenmachi(hc_list, ronhai):
        print("純正九蓮宝燈")
    elif chuurenpoutoo(hc_list):
        print("九蓮宝燈")
    if daisuushii(hc_list):
        print("大四喜")
    elif shousuushii(hc_list):
        print("小四喜")
    if daisangen(hc_list):
        print("大三元")
    if ryuuiisoo(hc_index_set):
        print("綠一色")
    if tsuuiisoo(hc_index_set):
        print("字一色")
    if chinrootoo(hc_index_set):
        print("清老頭")
    

    elif honroutoo(hc_index_set):
        print("混老頭")
    if chinitsu(hc_index_set):
        print("清一色")
    elif honitsu(hc_index_set):
        print("混一色")
    if tanyao(hc_index_set):
        print("斷么九")
    if chitoi(hc_list):
        print("七對子")
    
    # 一般型役種
    for m_list in ron_mentsu_list:
        if suuankoutanki(m_list,naki_list,ronhai):
            print("四暗刻單騎")
        elif suuankou(m_list, naki_list, tsumo):
            print("四暗刻")
        if suukantsu(nakipai_list):
            print("四槓子")
        if sanankou(m_list,nakipai_list,ronhai,tsumo):
            print("三暗刻")
        if sankantsu(nakipai_list):
            print("三槓子")
        if toitoi(m_list):
            print("對對和")
        if junchan(m_list):
            print("純全帯幺九")
        elif chanta(m_list):
            print("混全帯幺九")
        if ryanpeekoo(m_list,nakipai_list):
            print("二盃口")
        elif iipeekoo(m_list,nakipai_list):
            print("一盃口")
        if ittsuu(m_list):
            print("一氣通貫")
        if sanshokudoujun(m_list):
            print("三色同順")
        if sanshokudookoo(m_list):  
            print("三色同刻")
    

yaku(convert_hc_to_list("111m111p111s1122z"),27,[],True)
# yaku(convert_hc_to_list("1m"),0,[[(4,0,1),4,4],[(3,0,1),4,4],[(2,0,1),4,4],[(1,0,1),4,4]],False)