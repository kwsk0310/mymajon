import math

# 獲取所有可能的面子組合
def get_mentsu(hc_list):
    hc_list = hc_list.copy()
    depth = math.floor(sum(hc_list)/3) #判斷應有幾個面子(台麻5個，日麻4個)，並做為dsf的深度
    mentsu_possible_list = [] # [(2,1,0),(7,0,1),...] 345w,888w,...

    # 順子
    for i in range(27-2):
        if hc_list[i] and hc_list[i+1] and hc_list[i+2] and math.floor(i/9) == math.floor((i+2)/9):
            mentsu_possible_list.append((i,1,0))
    # 刻子
    for i in range(34):
        if hc_list[i] >= 3:
            mentsu_possible_list.append((i,0,1))

    m_list = [] # [(2,1,0),(7,0,1),...]
    mentsu_list = [] # [[(2,1,0),(7,0,1),...],[(7,0,1),(13,1,0),...]...]
    hc_stack = []
    hc_stack.append(hc_list)

    # 遞迴取得所有可能組合
    def dfs(m_list, d):
        # len(m_list)等於depth時為終點
        if len(m_list) >= depth:
            m_list_copy = m_list.copy()
            m_list_copy.sort()
            if m_list_copy not in mentsu_list:
                mentsu_list.append(m_list_copy)

        else: #len(m_list) < depth
            continue_count = 0
            for mentsu in mentsu_possible_list: # mentsu => (2,1,0) 345w
                # hc_satck長度不能超過d+1
                for x in range(len(hc_stack) - d - 1):
                    hc_stack.pop()
                hc_list = hc_stack[d].copy()
                # m_list長度不能超過d
                for x in range(len(m_list)-d):
                    m_list.pop()

                index = mentsu[0]
                # 順子
                if mentsu[1] > 0:
                    if hc_list[index] >= 1 and hc_list[index+1] >= 1 and hc_list[index+2] >= 1:
                        hc_list[index] -= 1
                        hc_list[index+1] -= 1
                        hc_list[index+2] -= 1
                        m_list.append(mentsu)
                    else:
                        continue_count += 1
                        # 連續len(mentsu_possible_list)次continue為終點
                        if continue_count >= len(mentsu_possible_list):
                            m_list_copy = m_list.copy()
                            m_list_copy.sort()
                            if m_list_copy not in mentsu_list:
                                mentsu_list.append(m_list_copy)
                        continue
                # 刻子
                elif mentsu[2] > 0:
                    if hc_list[index] >= 3:
                        hc_list[index] -= 3
                        m_list.append(mentsu)
                    else:
                        continue_count += 1
                        # 連續len(mentsu_possible_list)次continue為終點
                        if continue_count >= len(mentsu_possible_list):
                            m_list_copy = m_list.copy()
                            m_list_copy.sort()
                            if m_list_copy not in mentsu_list:
                                mentsu_list.append(m_list_copy)
                        continue
                hc_stack.append(hc_list)
                dfs(m_list, d+1)
    # 執行dsf
    dfs(m_list, 0)

    # 面子回退 應對 1345型拆解 -> 13 45 or 1 345
    mentsu_count_max = 0
    for m_list in mentsu_list:
        mentsu_count = len(m_list)
        if mentsu_count > mentsu_count_max:
            mentsu_count_max = mentsu_count
    # m_list的長度目前組合中最大時，進行回退
    for m_list in mentsu_list:
        if len(m_list) == mentsu_count_max:
            for x in range(len(m_list)):
                new_m_list = m_list[0:x] + m_list[x+1:] 
                new_m_list.sort()
                if new_m_list not in mentsu_list:
                    mentsu_list.append(new_m_list)

    return mentsu_list

# 獲取所有可能的塔子組合
def get_taatsu(hc_list):
    hc_list = hc_list.copy()
    depth = math.floor(sum(hc_list)/2) #判斷應有幾個塔子(台麻8個，日麻6個)，並做為dsf的深度
    taatsu_possible_list = [] # [(2,1,0,0),(7,0,1,0),(13,0,0,1)...] 33w,89w,57p...

    # [2]
    for i in range(34):
        if hc_list[i] >= 2:
            taatsu_possible_list.append((i,1,0,0))

    # [11]
    for i in range(27-1):
        if hc_list[i] and hc_list[i+1] and math.floor(i/9) == math.floor((i+1)/9):
            taatsu_possible_list.append((i,0,1,0))
    
    # [101]
    for i in range(27-2):
        if hc_list[i] and hc_list[i+2] and math.floor(i/9) == math.floor((i+2)/9):
            taatsu_possible_list.append((i,0,0,1))

    d_list = [] # [(2,1,0,0),(7,0,1,0),...]
    taatsu_list = [] # [[(2,1,0,0),(7,0,1,0),...],[(7,0,1,0),(13,1,0,0),...]...]
    hc_stack = []
    hc_stack.append(hc_list)

    # 遞迴取得所有可能組合
    def dfs(d_list, d):
        # len(d_list)等於depth時為終點
        if len(d_list) >= depth:
            d_list_copy = d_list.copy()
            d_list_copy.sort()
            if d_list_copy not in taatsu_list:
                taatsu_list.append(d_list_copy)

        else: #len(d_list) < depth
            continue_count = 0
            for taatsu in taatsu_possible_list: # taatsu => (2,1,0,0) 33w
                # hc_satck長度不能超過d+1
                for x in range(len(hc_stack) - d - 1):
                    hc_stack.pop()
                hc_list = hc_stack[d].copy()
                # d_list長度不能超過d
                for x in range(len(d_list)-d):
                    d_list.pop()

                index = taatsu[0]
                # [2]
                if taatsu[1] > 0:
                    if hc_list[index] >= 2:
                        hc_list[index] -= 2
                        d_list.append(taatsu)
                    else:
                        continue_count += 1
                        # 連續len(taatsu_possible_list)次continue為終點
                        if continue_count >= len(taatsu_possible_list):
                            d_list_copy = d_list.copy()
                            d_list_copy.sort()
                            if d_list_copy not in taatsu_list:
                                taatsu_list.append(d_list_copy)
                        continue
                # [11]
                elif taatsu[2] > 0:
                    if hc_list[index] >= 1 and hc_list[index+1] >= 1:
                        hc_list[index] -= 1
                        hc_list[index+1] -= 1
                        d_list.append(taatsu)
                    else:
                        continue_count += 1
                        # 連續len(taatsu_possible_list)次continue為終點
                        if continue_count >= len(taatsu_possible_list):
                            d_list_copy = d_list.copy()
                            d_list_copy.sort()
                            if d_list_copy not in taatsu_list:
                                taatsu_list.append(d_list_copy)
                        continue
                # [101]
                elif taatsu[3] > 0:
                    if hc_list[index] >= 1 and hc_list[index+2] >= 1:
                        hc_list[index] -= 1
                        hc_list[index+2] -= 1
                        d_list.append(taatsu)
                    else:
                        continue_count += 1
                        # 連續len(taatsu_possible_list)次continue為終點
                        if continue_count >= len(taatsu_possible_list):
                            d_list_copy = d_list.copy()
                            d_list_copy.sort()
                            if d_list_copy not in taatsu_list:
                                taatsu_list.append(d_list_copy)
                        continue
                
                hc_stack.append(hc_list)
                dfs(d_list, d+1)
    # 執行dsf
    dfs(d_list, 0)

    return taatsu_list

# a = get_mentsu([4,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# print(a)
# print(len(a))