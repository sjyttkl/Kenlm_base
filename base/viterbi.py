# -*- coding: utf-8 -*-

"""
==================================================
   File Name：     viterbi.py
   email:         songdongdong@weidian.com
   Author :       songdongdong
   date：          2020/7/25 18:28
   Description :   统计学习方法里案例
==================================================
"""
import numpy as np
def viterbi(train_prob,emission_prob,start_pro,obs_seq):
    """
    维特比
    :param train_pro:  转移矩阵
    :param emission_prob:  发射矩阵
    :param start_pro:   初始概率
    :param obs_pro:
    :return:
    """
    train_prob = np.array(train_prob) # #转换为矩阵进行运算
    emission_prob = np.array(emission_prob)
    start_pro = np.array(start_pro)

    row = np.array(train_prob).shape[0]
    col = len(obs_seq)
    # 最后返回一个Row*Col的矩阵结果
    result = np.zeros((row,col))
    print(result.shape) #(3, 3)
    result_index = []
    first = result[:,0]  = start_pro*np.transpose(emission_prob[:,obs_seq[0]]) # 初始概率* 转移矩阵
    result_index.append(list(first).index(max(list(first))))
    for time in range(1,col): # 一个一个时间步的运行
        list_max = []
        for state in range(row): #状态转移循环
            list_x = list(np.array(result[:,time-1]) * np.transpose(train_prob[:,state]))#前一个状态概率 *  转移矩阵
            # #获取最大概率
            list_p = []
            for i in list_x:
                list_p.append(i*10000)
            #记录最大路径前一个状态
            list_max.append(max(list_p)/10000)
        result_index.append(list_p.index(max(list_p)))
        result[:,time] = np.array(list_max) * np.transpose(emission_prob[:,obs_seq[time]]) # 这个状态* 发射概率
    return result,result_index


if __name__=='__main__':
    #隐藏状态
    invisible=['Sunny','Cloud','Rainy']
    print("隐藏状态： ",np.array(invisible))

    #初始状态
    pi=[0.2,0.4,0.4]
    print("初始状态： ",np.array(pi))
    #转移矩阵
    # trainsion_probility=[[0.5,0.375,0.125],[0.25,0.125,0.625],[0.25,0.375,0.375]]
    trainsion_probility=[[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]]

    print("转移矩阵： ",np.array(trainsion_probility))
    #发射矩阵
    emission_probility=[[0.5,0.5],[0.4,0.6],[0.7,0.3]]
    print("发射矩阵： ",np.array(emission_probility))

    #最后显示状态
    obs_seq=[0,1,0] #这个就是待观测待序列 红白红
    print("最后显示状态  " ,obs_seq)
    #最后返回一个Row*Col的矩阵结果
    result,result_index =viterbi(trainsion_probility,emission_probility,pi,obs_seq)
    print("最终结果。。。")
    print(result)
    print(result_index)