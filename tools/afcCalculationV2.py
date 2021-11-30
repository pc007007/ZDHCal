#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import json


# constant variables:
# J:超高峰小时系数
# K:检票机通过率
# AH:近期高峰列车对数/小时
# J = [1.25,1.35,1.4,1.38,1.3,1.15,1.18,1.25,1.12,1.1,1.1,1.35,1.38,1.25,1.18,1.15,
#      1.22,1.28,1.18,1.18,1.15,1.2,1.2,1.18,1.2,1.28,1.35,1.15,1.32,1.3,1.35,1.4,1.3]
# K = 20
# AH = 24

# # **Read the data input**

# In[20]:
class AFC_project:

    def __init__(self, file_path="./标准输入.xlsx", tab_names=["近期早高峰客流", "近期晚高峰客流"],
                 parameter_list=[20, 24, 6, 8, 5, 4, 20, 20]):
        self.df_jqzg = pd.read_excel(file_path, tab_names[0], header=[0, 1], index_col=0)
        self.df_jqwg = pd.read_excel(file_path, tab_names[1], header=[0, 1], index_col=0)
        self.K = parameter_list[0]
        self.AH = parameter_list[1]
        # 6
        self.min_jz_afc = parameter_list[2]
        # 8
        self.min_cz_afc = parameter_list[3]

        self.cpclnl = parameter_list[4]

        self.min_spj = parameter_list[5]

        self.jq_syl = 0.01 * parameter_list[6]
        self.jq_syl = 0.01 * parameter_list[7]

    # df_yqzg = pd.read_excel("./标准输入.xlsx","远期早高峰客流",header=[0,1],index_col=0)
    # df_yqwg = pd.read_excel("./标准输入.xlsx","远期晚高峰客流",header=[0,1],index_col=0)

    def run(self):
        # # # **Input data processing and manipulation**
        df_jqzg = self.df_jqzg.iloc[:, 0:8].dropna()
        df_jqwg = self.df_jqwg.iloc[:, 0:9].dropna()
        df_jq = pd.concat([df_jqzg, df_jqwg], axis=1)
        df_jq.columns = ['早高峰\n下行上客量',
                         '早高峰\n下行换乘量',
                         '早高峰\n下行下客量',
                         '早高峰\n下行换乘量',
                         '早高峰\n上行上客量',
                         '早高峰\n上行换乘量',
                         '早高峰\n上行下客量',
                         '早高峰\n上行换乘量',
                         '晚高峰\n下行上客量',
                         '晚高峰\n下行换乘量',
                         '晚高峰\n下行下客量',
                         '晚高峰\n下行换乘量',
                         '晚高峰\n上行上客量',
                         '晚高峰\n上行换乘量',
                         '晚高峰\n上行下客量',
                         '晚高峰\n上行换乘量',
                         '超高峰小时系数']

        # 总进站客流（近期）zjjq
        # 总出站客流（近期）zcjq
        # 总进站客流（远期）zjyq
        # 总出站客流（远期）zcyq

        input1 = df_jq
        J = df_jq.iloc[:, -1]
        J.to_list()

        jqzgfzj = df_jq.iloc[:, 0] + df_jq.iloc[:, 4]
        jqzgfcj = df_jq.iloc[:, 2] + df_jq.iloc[:, 6]
        jqwgfzj = df_jq.iloc[:, 8] + df_jq.iloc[:, 12]
        jqwgfcj = df_jq.iloc[:, 10] + df_jq.iloc[:, 14]
        # output:
        df_jp_numpy = pd.concat([jqzgfzj, jqwgfzj, jqzgfcj, jqwgfcj], axis=1).to_numpy()

        # constant variables:
        # J:超高峰小时系数
        # K:检票机通过率
        # AH:近期高峰列车对数/小时
        # J = [1.25,1.35,1.4,1.38,1.3,1.15,1.18,1.25,1.12,1.1,1.1,1.35,1.38,1.25,1.18,1.15,
        #      1.22,1.28,1.18,1.18,1.15,1.2,1.2,1.18,1.2,1.28,1.35,1.15,1.32,1.3,1.35,1.4,1.3]
        # K = 20
        # AH = 24

        B = df_jp_numpy[:, 0]
        C = df_jp_numpy[:, 1]
        D = df_jp_numpy[:, 2]
        E = df_jp_numpy[:, 3]

        F = []
        for i, j in zip(B, C):
            F.append(max(i, j))
        F = np.array(F)

        G = []
        for i, j in zip(D, E):
            G.append(max(i, j))
        G = np.array(G)

        # data processing

        # Variables:
        # A: 车站
        # B: 早高峰进站小时人数
        # C: 晚高高峰进站小时人数
        # D: 早高峰出站小时人数
        # E: 晚高峰出站小时人
        # F: MAX(C进)
        # G: MAX(C出)

        # A = data_part1[:,2]
        # B = data_part1_num[:,0] + data_part1_num[:,2]
        # C = data_part2_num[:,0] + data_part2_num[:,2]
        # D = data_part1_num[:,1] + data_part1_num[:,3]
        # E = data_part2_num[:,1] + data_part2_num[:,3]

        F = []
        for i, j in zip(B, C):
            F.append(max(i, j))
        F = np.array(F)

        G = []
        for i, j in zip(D, E):
            G.append(max(i, j))
        G = np.array(G)

        # H:进站朝晚比例
        # I:出站朝晚比例

        H = B / C
        I = D / E

        # L: 进站检票机计算数量(早高峰)
        # M: 出站检票机计算数量(早高峰)
        # N: 进站检票机计算数量(晚高峰)
        # O: 出站检票机计算数量(晚高峰)
        # P: 进站检票机计算数量(MAX)
        # Q: 出站检票机计算数量(MAX)
        # R: 进站检票机早晚差
        # S: 出站检票机早晚差
        # T: 进站检票机最小数量
        # U: 出站检票机最小数量
        # V: 双向检票机最小数量
        # W: 合计

        L = np.ceil(B * J / self.K / 60)
        M = np.ceil(D * J / self.K / 60)
        N = np.ceil(C * J / self.K / 60)
        O = np.ceil(E * J / self.K / 60)
        P = np.ceil(F * J / self.K / 60)
        Q = np.ceil(G * J / self.K / 60)
        R = L - N
        S = M - O
        V = []
        for i in range(len(R)):
            if (R[i] * S[i]) < 0:
                V.append(min(abs(R[i]), abs(S[i])))
            else:
                V.append(0)

        T = []
        for i in range(len(R)):
            if (R[i] * S[i]) < 0:
                if abs(R[i]) < abs(S[i]):
                    T.append(min(L[i], N[i]))
                else:
                    T.append(max(L[i], N[i]) - V[i])
            else:
                T.append(max(L[i], N[i]))
        T = np.array(T)

        U = []
        for i in range(len(R)):
            if (R[i] * S[i]) < 0:
                if abs(R[i]) < abs(S[i]):
                    U.append(max(M[i], O[i]) - V[i])
                else:
                    U.append(min(M[i], O[i]))
            else:
                U.append(max(M[i], O[i]))
        U = np.array(U)
        W = T + U + V

        # AE:检票机出站通过时间（min)
        # A:F乘客疏散后空闲时间(s)（此值越小越拥堵）
        # AG:列车间隔时间(min)
        # AH:近期高峰列车对数/小时
        # AI:高峰小时平均一列车的出站人数(含超高峰系数)

        AG = [60 / self.AH] * len(B)
        AI = G * J / self.AH

        # X:检票机出站通过时间（min)
        # Y:乘客疏散后空闲时间(s)（此值越小越拥堵）
        X = AI / Q / self.K
        Y = (AG - X) * 60

        # T: 进站检票机最小数量
        # U: 出站检票机最小数量
        # V: 双向检票机最小数量
        # W: 合计

        # AC为宽通道双向检票机，这个以后可做成一个函数
        AC = [2] * len(L)
        self.min_jz_afc = self.min_jz_afc - 1
        self.min_cz_afc = self.min_cz_afc - 1
        print(self.min_jz_afc)
        print(self.min_cz_afc)
        Z = [self.min_jz_afc] * len(L)
        for i in range(len(L)):
            while P[i] > Z[i] + 1:
                Z[i] = Z[i] + 1

        AA = [self.min_cz_afc] * len(L)
        for i in range(len(L)):
            while Q[i] >= AA[i]:
                AA[i] = AA[i] + 1

        print("after change")

        AB = [0] * len(L)

        AD = [0.5 * i + j for i, j in zip(AC, AA)]

        AE = AI / AD / self.K

        AF = (AG - AE) * 60

        # In[73]:

        # T: 进站检票机最小数量
        # U: 出站检票机最小数量
        # V: 双向检票机最小数量
        # W: 合计
        output = pd.DataFrame(np.round(np.array([T, U, V, W, X, Y, AI]).transpose(), decimals=2),
                              columns=['进站检票机最小数量', '出站检票机最小数量', '双向检票机最小数量', '合计',
                                       '检票机出站通过时间(min)', '乘客疏散后空闲时间(s)(此值越小越拥堵)',
                                       '高峰小时平均一列车的出站人数(含超高峰系数)'])
        df_jp_numpy[:, 2]
        output1 = pd.concat([df_jq.iloc[:, [0, 2, 4, 6, 8, 10, 12, 14, 16]], jqzgfzj, jqwgfzj, jqzgfcj, jqwgfcj,
                             pd.DataFrame(F, index=df_jq.index), pd.DataFrame(G, index=df_jq.index),
                             pd.DataFrame(np.round(I, decimals=2), index=df_jq.index)], axis=1)

        output1.columns = ['早高峰\n下行上客量', '早高峰\n下行下客量', '早高峰\n上行上客量',
                           '早高峰\n上行下客量', '晚高峰\n下行上客量', '晚高峰\n下行下客量',
                           '晚高峰\n上行上客量', '晚高峰\n上行下客量', '超高峰\n小时系数', '早高峰进站', '晚高峰进站', '早高峰出站', '晚高峰出站',
                           'MAX(C进)', 'MAX(C出)', '出站朝晚比例']

        L = L.astype(int)
        M = M.astype(int)
        N = N.astype(int)
        O = O.astype(int)
        P = P.astype(int)
        Q = Q.astype(int)

        # 按照最大高峰小时人流(含超高峰系数)计算所需检票机数量
        output2 = pd.concat([pd.DataFrame(L, index=df_jq.index),
                             pd.DataFrame(M, index=df_jq.index),
                             pd.DataFrame(N, index=df_jq.index),
                             pd.DataFrame(O, index=df_jq.index),
                             pd.DataFrame(P, index=df_jq.index),
                             pd.DataFrame(Q, index=df_jq.index),
                             pd.DataFrame(np.round(X, decimals=2),
                                          index=df_jq.index), pd.DataFrame(np.round(Y, decimals=2), index=df_jq.index)
                             ], axis=1)

        output2.columns = ["进站检票机\n(早高峰)",
                           "出站检票机\n(早高峰)",
                           "进站检票机\n(晚高峰)",
                           "出站检票机\n(晚高峰)",
                           "进站检票机\n(MAX)",
                           "出站检票机\n(MAX)",
                           "检票机出站\n通过时间(min)",
                           "乘客疏散后空闲时间(s)\n(此值越小越拥堵)"]
        C2 = C
        D2 = F
        E2 = J

        F2 = [i * j * self.jq_syl / 60 / self.cpclnl for i, j in zip(D2, E2)]

        G2 = np.ceil(F2)

        for i in range(len(G2)):
            if G2[i] < self.min_spj:
                G2[i] = self.min_spj

        G2 = G2.astype(int)
        AD = [int(i) for i in AD]

        output3 = pd.concat([
            pd.DataFrame(Z, index=df_jq.index),
            pd.DataFrame(AA, index=df_jq.index), pd.DataFrame(AB, index=df_jq.index),
            pd.DataFrame(AC, index=df_jq.index), pd.DataFrame(AD, index=df_jq.index),
            pd.DataFrame(np.around(AE, decimals=2), index=df_jq.index),
            pd.DataFrame(np.around(AF, decimals=2), index=df_jq.index),
            pd.DataFrame(G2, index=df_jq.index),
            pd.DataFrame(AG, index=df_jq.index),
            # pd.DataFrame(np.around(X,decimals=2),index=df_jq.index),
            pd.DataFrame(np.around(AI, decimals=2), index=df_jq.index),
            pd.DataFrame(Q, index=df_jq.index),
            pd.DataFrame([self.K] * len(Z), index=df_jq.index)],
            axis=1)

        output3.columns = ["进站检票机", "出站检票机", "双向检票机", "双向检票机\n(宽)","出站检票机\n(总可用量)",
                           "检票机出站\n通过时间(min)",
                           "乘客疏散后空闲时间(s)\n(此值越小越拥堵)",
                           "自动售票机",
                           "列车间隔\n时间(min)",
                           "高峰小时平均\n一列车的出站人数\n(含超高峰系数)",
                           "出站检票机\n计算数量(MAX)",
						   "检票机通过率\n(人/分钟)"]

        output4 = pd.concat([pd.DataFrame(R, index=df_jq.index),
                             pd.DataFrame(S, index=df_jq.index),
                             pd.DataFrame(T, index=df_jq.index),
                             pd.DataFrame(U, index=df_jq.index),
                             pd.DataFrame(V, index=df_jq.index),
                             pd.DataFrame(W, index=df_jq.index)], axis=1)

        output4.columns = ['进站检票机\n早晚差',
                           '出站检票机\n早晚差',
                           '进站检票机\n最小数量',
                           '出站检票机\n最小数量',
                           '双向检票机\n最小数量',
                           '合计']

        final_output = [input1, output1, output2, output3, output4]

        return final_output


def get_entire_file(file_name='./天津1号线.json'):
    with open(file_name, "r") as load_f:
        load_dict = json.load(load_f)
    return (load_dict)


def get_parameter(file_name='./天津1号线.json'):
    with open(file_name, "r") as load_f:
        load_dict = json.load(load_f)
    return (load_dict.get('gate'))


def get_dataFrame(objectName, file_name='./天津1号线.json'):
    with open(file_name, "r") as load_f:
        load_dict = json.load(load_f)

    # 根据情况反馈函数，如果找不到返回一个特定值
    try:
        load_dict.get(objectName)
        df = pd.read_json(load_dict.get(objectName), orient='columns')
    except:
        # 如找不到对应Key，返还1
        return None

    return (df)


def save_dataFrame(df, objectName, file_name='./天津1号线.json'):
    data = df.to_json(orient="columns", force_ascii=False)

    with open(file_name, "r") as load_f:
        load_dict = json.load(load_f)

    load_dict.update({objectName: data})

    with open(file_name, "w") as f:
        json.dump(load_dict, f)

    return 0


def output_excel(path, output, manual_output=None):
    writer = pd.ExcelWriter(path, engin='openpyxl')
    output[0].to_excel(writer, sheet_name='输入资料')
    output[1].to_excel(writer, sheet_name='输出1')
    output[2].to_excel(writer, sheet_name='输出2')
    output[4].to_excel(writer, sheet_name='输出3')
    output[3].to_excel(writer, sheet_name='计算数量')
    manual_output.to_excel(writer, sheet_name='最终确定数量')
    writer.save()


def loadParam(filePath):
    with open(filePath, 'r') as f:
        data = json.load(f)
    f.close()
    para = [
        data['gate']['passRate'],
        data['gate']['peakTrainPairs'],
        data['gate']['minNum'],
        data['gate']['maxNum'],
        data['vendingMachine']['tktProcessingCap'],
        data['vendingMachine']['minNum'],
        data['vendingMachine']['rateOfRecentUse'],
        data['vendingMachine']['rateOfFutureUse'],
    ]
    ridershipAddress = data['ridershipAddress']
    return para, ridershipAddress
