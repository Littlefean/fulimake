import random


def get_random_score(max_score):
    """根据一个算法生成一个随机分数"""
    # 定义参数
    mu, sigma = max_score * 0.65, 15  # 设定平均数和标准差
    # 20% 的概率会出现 后缀分.5
    add_score = 0.5 if random.random() < 0.2 else 0
    return min(max_score, int(random.normalvariate(mu, sigma)) + add_score)
