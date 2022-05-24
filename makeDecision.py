'''
Author: Zheng
Date: 2022-05-20 15:23:26
LastEditors: Zheng
LastEditTime: 2022-05-20 15:31:42
Description: default description
'''
from car import Car

class Rank():
    def __init__(self, car, grade):
        self.car = car
        self.grade = grade

def makeDecision(min_price, max_price, cartypes, worthy_degree, performance_degree, comfortable_degree, appearance_degree):
    # 首先按价格、车型筛选列表
    arr = []
    type = ''
    with open("./data/gradeData.csv") as f:
        for line in f:
            price = float(line.split(",")[3])
            if price <= max_price and price >= min_price:
                if line.split(",")[2] in cartypes:
                    arr.append(int(line.split(",")[0]))
        f.close()
        # print("您可以选择的车型有：")
        # for i in arr:
        #     print(i)
        res = SelectCar(arr, worthy_degree, performance_degree, comfortable_degree, appearance_degree)
        return res

def SelectCar(arr, worthy_degree, performance_degree, comfortable_degree, appearance_degree):
    with open('./data/gradeData.csv') as f:
        carArr = []
        for line in f:
            if int(line.split(',')[0]) in arr:
                line = line.split(',')
                carArr.append(Car(int(line[0]), line[1], line[2], round(float(line[3]), 2), round(float(line[4]),2), round(float(line[5]),2), round(float(line[6]),2)))
    f.close()
    # todo：核心筛选算法 可采取某种数学模型
    carArr.sort(key=lambda x: x.price, reverse=True)
    # 根据用户选择计算总评分
    # print(worthy_degree, performance_degree, comfortable_degree, appearance_degree)
    total_value_degree = performance_degree + comfortable_degree + appearance_degree
    performance_degree = performance_degree / total_value_degree
    comfortable_degree = comfortable_degree / total_value_degree
    appearance_degree = appearance_degree / total_value_degree
    rankCars = []
    for car in carArr:
        rank = performance_degree * car.power + comfortable_degree * car.comfort_level + appearance_degree * car.appearance
        rankCars.append(Rank(car, rank))

    rankCars.sort(key=lambda x: x.grade, reverse=True)
    res = []
    reasonsArr = []
    for i in range(0, len(rankCars)):
        res.append(rankCars[i].car)
    return res, reasonsArr