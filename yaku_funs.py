# 不要求胡牌型式的役種----------------------------------------------------------------------

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
    if hc_index_set.issubset(manzu|jihai) or hc_index_set.issubset(pinzu|jihai) or hc_index_set.issubset(souzu|jihai):
        return True
    else:
        return False
    
# 檢查是否符合斷么九
def tanyao(hc_index_set):
    if hc_index_set.issubset({1,2,3,4,5,6,7,10,11,12,13,14,15,16,19,20,21,22,23,24,25,27,28,29,30,31,32,33}):
        return True
    else:
        return False
    
# 非一般型役種-----------------------------------------------------------------------------


# 檢查是否符合國士無雙
def kokushi(hc_list):
    yaochu = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]
    yaochu_count = 0
    for i in yaochu:
        if hc_list[i] > 0 :
            yaochu_count += 1
    if yaochu_count == 13 and hc_list.index(2) in yaochu:
        return True
    else:
        return False

# 檢查是否符合七對子
def chitoi(hc_list):
    # 因為已排除兩盃口的可能性，所以只要檢查有沒有七個對子
    if hc_list.count(2) == 7:
        return True
    else:
        return False

# 檢查是否符合九蓮寶燈
def chuurenpoutoo(hc_list):
    hc_list = hc_list.copy()
    chuuren = [3,1,1,1,1,1,1,1,3]
    for i in [0,9,18]:
        if all(x-y >= 0 for x, y in zip(hc_list[i:i+9], chuuren)):
            return True
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
# 一般型役種-------------------------------------------------------------------------------

# 大三元 • 四喜和 • 四槓子 • 四暗刻 • 純全帶么九 • 二杯口 • 一氣通貫 • 混全帶么九 • 三色同順 • 三色同刻
# 三暗刻 • 三槓子 • 小三元 • 對對和 • 混老頭 • 七對子 • 役牌（三元牌 • 自風牌 • 場風牌） • 平和 • 一杯口

# 其他役種---------------------------------------------------------------------------------

# 天和 • 地和 • 雙立直 • 立直 • 一發 • 門前清自摸和 • 搶槓 • 嶺上開花 • 海底撈月 • 河底撈魚 • 寶牌（赤寶牌 • 拔北寶牌三麻）
print(chuurenpoutoo([ 0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0, 3,1,1,1,1,1,1,1,4, 0,0,0,0,0,0,0]))
