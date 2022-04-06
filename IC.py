import copy
import random


def runIC(G, S):
    # 为了不污染S,所以采用深拷贝拷贝S
    # 一个用于存放当前所有已经激活的节点，一个用于存放每一轮新激活的节点
    active_nodes = copy.deepcopy(S)
    active_new = copy.deepcopy(S)
    # temp用于临时存放新激活的节点，在每一轮结束后会将值给active_new
    temp = []
    # 当没有节点被激活时循环就停止了
    while len(active_new):
        # 每一次循环只需要遍历新激活的节点的邻居就可以了
        for node in active_new:
            # 对新激活的节点出邻居进行遍历
            for u in G[node]:
                # 节点被激活时就加入temp和active_nodes
                if random.random() < G[node][u]['propagate_probability']:
                    temp.append(u)
                    active_nodes.append(u)
        # 每一轮结束后将新激活的节点结果交个active_new并清空temp
        active_new = copy.deepcopy(temp)
        temp.clear()
    # 最终返回值为所有激活的节点列表
    return active_nodes


def set_propagate_probability(G):
    for edge in G.edges:
        # G[edge[0]][edge[1]]['propagate_probability'] = random.random()
        G[edge[0]][edge[1]]['propagate_probability'] = 0.1


def avaIC(G, S, v, iter_num):
    # 为了不污染种子集S，所以采用深拷贝拷贝当前种子集
    Seeds = copy.deepcopy(S)
    # 设置一个变量用于存放蒙特卡洛模拟激活的节点总数之和
    average = 0.0
    # 如果当前选择的节点是已经被选择为种子节点那么影响力直接返回0
    if v in S:
        return average
    # 否则的话就将当前节点加入种子集进行计算影响力
    Seeds.append(v)
    # 这里是蒙特卡洛模拟每一次循环
    for _ in range(iter_num):
        # 每次都跑一次IC模型并将结果加到average里
        average += len(runIC(G, Seeds))
    # 最后返回平均影响力
    return average / iter_num
