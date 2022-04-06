from IC import *


def run_greedy(G, seed_num, iter_num):
    # 首先创建数组用来存放种子节点
    S = []
    # 需要多少种子节点就进行多少次循环
    for _ in range(seed_num):
        # 每次循环需要设置一个临时数组用来存放节点的影响力
        print(f'寻找第 {_+1} 个种子')
        temp = [0.0 for i in range(30)]
        # 对于每个节点计算当前节点加入种子集后的平均影响力
        for node in G:
            temp[int(node)] = avaIC(G, S, node, iter_num)
        # 最后选出具有最大影响力的节点及其索引
        value = max(temp)
        indexOfValue = temp.index(value)
        # 加入种子集
        S.append(str(indexOfValue))
        # temp.clear()
        print('本轮种子', indexOfValue, ', 影响力', value,  ', 种子集', S)
    return S
