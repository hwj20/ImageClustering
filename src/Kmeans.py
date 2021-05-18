import numpy as np
import matplotlib.pyplot as plt

'''标志位统计递归运行次数'''
flag = 0

'''欧式距离'''


def ecludDist(x, y):
    # print(x-y)
    # print(np.square(x-y))
    # print(sum(np.square(x-y)))
    return np.sqrt(sum(np.square(x - y)))


'''曼哈顿距离'''


def manhattanDist(x, y):
    return np.sum(np.abs(x - y))


'''夹角余弦'''


def cos(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))


'''计算簇的均值点'''


def clusterMean(dataset):
    if len(dataset) == 0:
        return []
    return np.sum(np.array(dataset), axis=0) / len(dataset)


'''生成随机均值点'''


def randCenter(dataset, k):
    temp = []
    while len(temp) < k:
        index = np.random.randint(0, len(dataset) - 1)
        if index not in temp:
            temp.append(index)
    # temp = [0,1,2]
    return np.array([dataset[i] for i in temp])


'''以数据集的前k个点为均值点'''


def orderCenter(dataset, k):
    return np.array([dataset[i] for i in range(k)])


'''聚类'''


def kMeans(dataset, dist, center, k):
    global flag
    # all_kinds用于存放中间计算结果
    all_kinds = []
    index_list = []
    for _ in range(k):
        temp = []
        all_kinds.append(temp)
    # 计算每个点到各均值点的距离
    for i in dataset:
        temp = []
        for j in center:
            temp.append(dist(i, j))
        all_kinds[temp.index(min(temp))].append(i)  # temp.index(min(temp)) is the min value's index in center
        index_list.append(temp.index((min(temp))))
    # 打印中间结果
    for i in range(k):
        if not all_kinds[i]:
            # to make two same center come to one, in some case
            for j in range(len(center)):
                if center[j] == center[i]:
                    all_kinds[i] = all_kinds[j]
        print('第' + str(i) + '组:', all_kinds[i], end='\n')
    flag += 1
    print('************************迭代' + str(flag) + '次***************************')
    # 更新均值点
    center_ = np.array([clusterMean(i) for i in all_kinds])
    if (center_ == center).all():
        print('结束')
        return index_list, center_
    else:
        # 递归调用kMeans函数
        center = center_
        return kMeans(dataset, dist, center, k)


def mul_kMeans(dataset, dist, k, times):
    index_list, center_all = kMeans(dataset, dist, randCenter(dataset, k), k)
    for i in range(times-1):
        index_list, center = kMeans(dataset, dist, randCenter(dataset, k), k)
        center_all = center_all + center
    center_all = center_all / times

    all_kinds = []
    for _ in range(k):
        temp = []
        all_kinds.append(temp)
    index_list = []
    for i in dataset:
        temp = []
        for j in center_all:
            temp.append(dist(i,j))
        all_kinds[temp.index(min(temp))].append(i)  # temp.index(min(temp)) is the min value's index in center
        index_list.append(temp.index((min(temp))))

    return index_list, center_all

