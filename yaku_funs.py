# 不要求胡牌型式的役種----------------------------------------------------------------------

# 檢查是否符合國士無雙十三面
def kokushimusoujuusanmenmachi(hc_index_set,hc_list,ronhai):
    yaochu = {0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33}
    if yaochu == hc_index_set and hc_list.index(2) == ronhai:
        return True
    else:
        return False

# 檢查是否符合國士無雙
def kokushimusou(hc_index_set):
    yaochu = {0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33}
    if yaochu == hc_index_set:
        return True
    else:
        return False

# 檢查是否符合純正九蓮寶燈
def chuurenkyuumenmachi(hc_list, ronhai):
    hc_list = hc_list.copy()
    hc_list[ronhai] -= 1
    chuuren = [3,1,1,1,1,1,1,1,3]
    for i in [0,9,18]:
        if hc_list[i:i+9] == chuuren:
            return True
    return False

# 檢查是否符合九蓮寶燈
def chuurenpoutoo(hc_list):
    hc_list = hc_list.copy()
    chuuren = [3,1,1,1,1,1,1,1,3]
    for i in [0,9,18]:
        if all(x-y >= 0 for x, y in zip(hc_list[i:i+9], chuuren)):
            return True
    return False

# 檢查是否符合大四喜
def daisuushii(hc_list):
    if sum(hc_list[27:31]) == 12:
        return True
    else:
        return False
    
# 檢查是否符合小四喜
def shousuushii(hc_list):
    if sum(hc_list[27:31]) == 11:
        return True
    else:
        return False
    
# 檢查是否符合大三元
def daisangen(hc_list):
    if sum(hc_list[31:]) == 9:
        return True
    else:
        return False

# 檢查是否符合綠一色
def ryuuiisoo(hc_index_set):
    if hc_index_set.issubset({19,20,21,23,25,32}):
        return True
    else:
        return False
    
# 檢查是否符合字一色
def tsuuiisoo(hc_index_set):
    if hc_index_set.issubset({27,28,29,30,31,32,33}):
        return True
    else:
        return False
    
# 檢查是否符合清老頭
def chinrootoo(hc_index_set):
    if hc_index_set.issubset({0,8,9,17,18,26}):
        return True
    else:
        return False

# 檢查是否符合混老頭
def honroutoo(hc_index_set):
    if hc_index_set.issubset({0,8,9,17,18,26,27,28,29,30,31,32,33}):
        return True
    else:
        return False
    
# 檢查是否符合清一色
def chinitsu(hc_index_set):
    manzu = {0,1,2,3,4,5,6,7,8}
    pinzu = {9,10,11,12,13,14,15,16,17}
    souzu = {18,19,20,21,22,23,24,25,26}
    if hc_index_set.issubset(manzu) or hc_index_set.issubset(pinzu) or hc_index_set.issubset(souzu):
        return True
    else:
        return False
    
# 檢查是否符合混一色
def honitsu(hc_index_set):
    manzu = {0,1,2,3,4,5,6,7,8}
    pinzu = {9,10,11,12,13,14,15,16,17}
    souzu = {18,19,20,21,22,23,24,25,26}
    jihai = {27,28,29,30,31,32,33}
    # 不能只有字牌
    if hc_index_set.issubset(manzu|jihai) or hc_index_set.issubset(pinzu|jihai) or hc_index_set.issubset(souzu|jihai):
        return True
    else:
        return False
    
# 檢查是否符合斷么九
def tanyao(hc_index_set):
    if hc_index_set.issubset({1,2,3,4,5,6,7,10,11,12,13,14,15,16,19,20,21,22,23,24,25}):
        return True
    else:
        return False

# 檢查是否符合七對子
def chitoi(hc_list):
    if hc_list.count(2) == 7:
        return True
    else:
        return False

# 檢查是否符合小三元
def daisangen(hc_list):
    if sum(hc_list[31:]) == 8:
        return True
    else:
        return False


# 一般型役種-------------------------------------------------------------------------------

# 檢查是否符合四暗刻單騎
def suuankoutanki(m_list,nakipai_list,ronhai):
    ankou = [x[2] for x in m_list[0]].count(1) - [x[0][2] for x in nakipai_list if (x[1] == 2 or x[1] == 3)].count(1) # 胡牌是刻子的情況也會被算進去
    if ankou == 4 and ronhai == m_list[1]:
        return True
    else:
        return False

# 檢查是否符合四暗刻
def suuankou(m_list, nakipai_list, tsumo):
    ankou = [x[2] for x in m_list[0]].count(1) - [x[0][2] for x in nakipai_list if (x[1] == 2 or x[1] == 3)].count(1) # 胡牌是刻子的情況也會被算進去
    if tsumo and ankou == 4:
        return True
    else:
        return False

# 檢查是否符合四槓子
def suukantsu(nakipai_list):
    if [x[1] for x in nakipai_list].count(3) + [x[1] for x in nakipai_list].count(4) == 4:
        return True
    else:
        return False

# 檢查是否符合三暗刻
def sanankou(m_list,nakipai_list,ronhai,tsumo): # m_list=([(0,1,0),(9,1,0),(18,1,0),(27,0,1)], 28)
    ankou = [x[2] for x in m_list[0]].count(1) - [x[0][2] for x in nakipai_list if (x[1] == 2 or x[1] == 3)].count(1) # 胡牌是刻子的情況也會被算進去
    # 如果是自摸，只要判斷手牌中暗刻數量
    if tsumo and ankou == 3:
        return True
    # 如果不是自摸，還要判斷胡的牌是不是順子或雀頭，若是則暗刻數要等於3
    elif not tsumo and (ronhai == m_list[1] or (ronhai in ([x[0] for x in m_list[0] if x[1] == 1]+[x[0]+2 for x in m_list[0] if x[1] == 1]))):
        if ankou == 3:
            return True
    # 如果不是自摸，且胡的牌是不是順子或雀頭(胡的牌是刻子)，若是則暗刻數要等於4
    elif ankou == 4:
        return True
    else:
        return False

# 檢查是否符合三槓子
def sankantsu(nakipai_list):
    if [x[1] for x in nakipai_list].count(3) + [x[1] for x in nakipai_list].count(4) == 3:
        return True
    else:
        return False

# 檢查是否符合對對和
def toitoi(m_list):
    if [x[2] for x in m_list[0]].count(1) == 4:
        return True
    else:
        return False

# 檢查是否符合純全帶么九
def junchan(m_list):
    for x in m_list[0]:
        if not x in({(0,1,0),(6,1,0),(9,1,0),(15,1,0),(18,1,0),(24,1,0)
                     ,(0,0,1),(8,0,1),(9,0,1),(17,0,1),(18,0,1),(26,0,1)}):
            return False
    if m_list[1] in [0,8,9,17,18,26]:
        return True
    else:
        return False

# 檢查是否符合混全帶么九
def chanta(m_list):
    if set(m_list[0]).issubset({(0,1,0),(6,1,0),(9,1,0),(15,1,0),(18,1,0),(24,1,0)
                                ,(0,0,1),(8,0,1),(9,0,1),(17,0,1),(18,0,1),(26,0,1)
                                ,(27,0,1),(28,0,1),(29,0,1),(30,0,1),(31,0,1),(32,0,1),(33,0,1)}):
        if m_list[1] in [0,8,9,17,18,26,27,28,29,30,31,32,33]:
            return True
    else:
        return False
    
# 檢查是否符合二盃口
def ryanpeekoo(m_list,nakipai_list):
    if len([x for x in nakipai_list if x[1] != 4]):
        return False
    for x in m_list[0]:
        if m_list[0].count(x) == 2:
            trimed_m_list = [y for y in m_list[0] if y != x]
            if trimed_m_list.count(trimed_m_list[0]) == 2:
                return True
    return False

# 檢查是否符合一盃口
def iipeekoo(m_list,nakipai_list):
    if len([x for x in nakipai_list if x[1] != 4]):
        return False
    for x in m_list[0]:
        if m_list[0].count(x) == 2:
            return True
    return False

# 檢查是否符合一氣通貫
def ittsuu(m_list):
    combination = [{(0,1,0),(3,1,0),(6,1,0)},{(9,1,0),(12,1,0),(15,1,0)},{(18,1,0),(21,1,0),(24,1,0)}]
    for x in combination:
        if x.issubset(set(m_list[0])):
            return True
    else:
        return False
    
# 檢查是否符合三色同順
def sanshokudoujun(m_list):
    combination = [{(0,1,0),(9,1,0),(18,1,0)},{(1,1,0),(10,1,0),(19,1,0)},{(2,1,0),(11,1,0),(20,1,0)}
                   ,{(3,1,0),(12,1,0),(21,1,0)},{(4,1,0),(13,1,0),(22,1,0)},{(5,1,0),(14,1,0),(23,1,0)}
                   ,{(6,1,0),(15,1,0),(24,1,0)}]
    for x in combination:
        if x.issubset(set(m_list[0])):
            return True
    else:
        return False
    
# 檢查是否符合三色同刻
def sanshokudookoo(m_list):
    combination = [{(0,0,1),(9,0,1),(18,0,1)},{(1,0,1),(10,0,1),(19,0,1)},{(2,0,1),(11,0,1),(20,0,1)}
                   ,{(3,0,1),(12,0,1),(21,0,1)},{(4,0,1),(13,0,1),(22,0,1)},{(5,0,1),(14,0,1),(23,0,1)}
                   ,{(6,0,1),(15,0,1),(24,0,1)},{(7,0,1),(16,0,1),(25,0,1)},{(8,0,1),(17,0,1),(26,0,1)}]
    for x in combination:
        if x.issubset(set(m_list[0])):
            return True
    else:
        return False



# 役牌（三元牌 • 自風牌 • 場風牌） • 平和

# 其他役種---------------------------------------------------------------------------------

# 天和 • 地和 • 雙立直 • 立直 • 一發 • 門前清自摸和 • 搶槓 • 嶺上開花 • 海底撈月 • 河底撈魚 • 寶牌（赤寶牌 • 拔北寶牌三麻）
# print(chuurenpoutoo([ 0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0, 3,1,1,1,1,1,1,1,4, 0,0,0,0,0,0,0]))