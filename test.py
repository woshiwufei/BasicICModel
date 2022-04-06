import time
import networkx as nx
import matplotlib.pyplot as plt
from greedy import *


def graph_creator(path):
    with open(path) as f:
        n, m = f.readline().split()
        for line in f:
            n, m = line.split()
            G.add_edge(n, m)
        print("Graph created***")


if __name__ == "__main__":
    start = time.time()
    G = nx.DiGraph()

    # 首先需要对数据集进行处理
    graph_creator('./data/graph30.txt')

    # 设置边上的传播概率
    set_propagate_probability(G)

    # 然后用贪心算法找到种子节点,参数需要图，种子数量，蒙特卡洛的次数，返回值为种子集
    S = run_greedy(G, 10, 100)

    print(time.time() - start)
    print(S)
