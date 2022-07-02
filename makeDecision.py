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


class Reason():
    def __init__(self, car, reason, grade):
        self.car = car
        self.reason = reason
        self.grade = grade


def makeDecision(min_price, max_price, cartypes, worthy_degree, performance_degree, comfortable_degree,
                 appearance_degree):
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
        res = SelectCar1(arr, worthy_degree, performance_degree, comfortable_degree, appearance_degree)
        return res


def SelectCar(arr, worthy_degree, performance_degree, comfortable_degree, appearance_degree):
    with open('./data/gradeData.csv') as f:
        carArr = []
        for line in f:
            if int(line.split(',')[0]) in arr:
                line = line.split(',')
                carArr.append(Car(int(line[0]), line[1], line[2], round(float(line[3]), 2), round(float(line[4]), 2),
                                  round(float(line[5]), 2), round(float(line[6]), 2)))
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


def SelectCar1(arr, worthy_degree, performance_degree, comfortable_degree, appearance_degree):
    global reasonsText
    with open('./data/gradeData.csv') as f:
        carArr = []
        for line in f:
            if int(line.split(',')[0]) in arr:
                line = line.split(',')
                carArr.append(Car(int(line[0]), line[1], line[2], round(float(line[3]), 2), round(float(line[4]), 2),
                                  round(float(line[5]), 2), round(float(line[6]), 2)))
    f.close()
    # todo：核心筛选算法 可采取某种数学模型
    carArr.sort(key=lambda x: x.price, reverse=True)
    # 根据用户选择计算总评分
    # print(worthy_degree, performance_degree, comfortable_degree, appearance_degree)

    rankCars = []

    average_worthy = 0
    average_performance = 0
    average_comfortable = 0
    average_appearance = 0

    for car in carArr:
        average_worthy += car.price
        average_performance += car.power
        average_comfortable += car.comfort_level
        average_appearance += car.appearance

    average_worthy = average_worthy / len(carArr)
    average_performance = average_performance / len(carArr)
    average_comfortable = average_comfortable / len(carArr)
    average_appearance = average_appearance / len(carArr)
    reasons = []
    for car in carArr:
        cf1 = cfRule_worthy(car, worthy_degree, average_worthy)
        cf2 = cfRule_performance(car, performance_degree, average_performance)
        cf3 = cfRule_comfortable(car, comfortable_degree, average_comfortable)
        cf4 = cfRule_appearance(car, appearance_degree, average_appearance)
        # find which cf is the highest
        cf_max = max(cf1, cf2, cf3, cf4)
        reasonsText = ""
        if cf_max == cf1:
            reasonsText += "价格"
        if cf_max == cf2:
            reasonsText += " 动力"
        elif cf_max == cf3:
            reasonsText += " 舒适性"
        elif cf_max == cf4:
            reasonsText += " 外观"

        cf = cf1
        cf = cf + cf2 * (1 - cf)
        cf = cf + cf3 * (1 - cf)
        cf = cf + cf4 * (1 - cf)

        rankCars.append(Rank(car, cf))
        reasonText = car.name[0:3] + "...在综合您对"+reasonsText+"的偏好下，"+"获得评分为" + str(cf)[0:6]
        reasons.append(Reason(car, reasonText, cf))

    rankCars.sort(key=lambda x: x.grade, reverse=True)
    reasons.sort(key=lambda x: x.grade, reverse=True)
    res = []
    reasonsArr = []
    for i in range(0, len(rankCars)):
        res.append(rankCars[i].car)
        reasonsArr.append(reasons[i].reason)
    return res, reasonsArr


def cfRule_worthy(car, worthy_degree, average_worthy):
    # 非常在乎价格
    if worthy_degree == 4:
        if car.price <= average_worthy * 0.8:
            return 0.7
        elif car.price > average_worthy * 0.8 and car.price < average_worthy:
            return 0.5
        elif car.price >= average_worthy and car.price < average_worthy * 1.2:
            return 0.3
        else:
            return 0.2
    # 在乎价格
    elif worthy_degree == 3:
        if car.price <= average_worthy * 0.8:
            return 0.7
        elif car.price > average_worthy * 0.8 and car.price < average_worthy:
            return 0.7
        elif car.price >= average_worthy and car.price < average_worthy * 1.2:
            return 0.5
        else:
            return 0.2
    # 不太在乎价格
    elif worthy_degree == 2:
        if car.price <= average_worthy * 0.8:
            return 0.7
        elif car.price > average_worthy * 0.8 and car.price < average_worthy:
            return 0.7
        elif car.price >= average_worthy and car.price < average_worthy * 1.2:
            return 0.7
        else:
            return 0.5
    # 不在乎价格
    elif worthy_degree == 1:
        if car.price <= average_worthy * 0.8:
            return 0.7
        elif car.price > average_worthy * 0.8 and car.price < average_worthy:
            return 0.7
        elif car.price >= average_worthy and car.price < average_worthy * 1.2:
            return 0.7
        else:
            return 0.7


def cfRule_performance(car, performance_degree, average_performance):
    # 非常在乎性能
    if performance_degree == 4:
        if car.power >= average_performance * 1.2:
            return 0.7
        elif car.power > average_performance and car.power < average_performance * 1.2:
            return 0.6
        elif car.power <= average_performance and car.power > average_performance * 0.8:
            return 0.4
        else:
            return 0.2
    # 在乎性能
    elif performance_degree == 3:
        if car.power >= average_performance * 1.2:
            return 0.7
        elif car.power > average_performance and car.power < average_performance * 1.2:
            return 0.7
        elif car.power <= average_performance and car.power > average_performance * 0.8:
            return 0.5
        else:
            return 0.3

    # 不太在乎性能
    elif performance_degree == 2:
        if car.power >= average_performance * 1.2:
            return 0.7
        elif car.power > average_performance and car.power < average_performance * 1.2:
            return 0.7
        elif car.power <= average_performance and car.power > average_performance * 0.8:
            return 0.6
        else:
            return 0.4

    # 不在乎性能
    elif performance_degree == 1:
        return 0.7


def cfRule_comfortable(car, comfortable_degree, average_comfortable):
    # 非常在乎舒适度
    if comfortable_degree == 4:
        if car.comfort_level >= average_comfortable * 1.2:
            return 0.7
        elif car.comfort_level > average_comfortable and car.comfort_level < average_comfortable * 1.2:
            return 0.5
        elif car.comfort_level <= average_comfortable and car.comfort_level > average_comfortable * 0.8:
            return 0.3
        else:
            return 0.2
    # 在乎舒适度
    elif comfortable_degree == 3:
        if car.comfort_level >= average_comfortable * 1.2:
            return 0.7
        elif car.comfort_level > average_comfortable and car.comfort_level < average_comfortable * 1.2:
            return 0.6
        elif car.comfort_level <= average_comfortable and car.comfort_level > average_comfortable * 0.8:
            return 0.4
        else:
            return 0.3

    # 不太在乎舒适度
    elif comfortable_degree == 2:
        if car.comfort_level >= average_comfortable * 1.2:
            return 0.7
        elif car.comfort_level > average_comfortable and car.comfort_level < average_comfortable * 1.2:
            return 0.7
        elif car.comfort_level <= average_comfortable and car.comfort_level > average_comfortable * 0.8:
            return 0.5
        else:
            return 0.4

    # 不在乎舒适度
    elif comfortable_degree == 1:
        if car.comfort_level >= average_comfortable * 1.2:
            return 0.7
        elif car.comfort_level > average_comfortable and car.comfort_level < average_comfortable * 1.2:
            return 0.7
        elif car.comfort_level <= average_comfortable and car.comfort_level > average_comfortable * 0.8:
            return 0.7
        else:
            return 0.6


def cfRule_appearance(car, appearance_degree, average_appearance):
    # 非常在乎外观
    if appearance_degree == 4:
        if car.appearance >= average_appearance * 1.2:
            return 0.7
        elif car.appearance > average_appearance and car.appearance < average_appearance * 1.2:
            return 0.5
        elif car.appearance <= average_appearance and car.appearance > average_appearance * 0.8:
            return 0.4
        else:
            return 0.3
    # 在乎外观
    elif appearance_degree == 3:
        if car.appearance >= average_appearance * 1.2:
            return 0.7
        elif car.appearance > average_appearance and car.appearance < average_appearance * 1.2:
            return 0.7
        elif car.appearance <= average_appearance and car.appearance > average_appearance * 0.8:
            return 0.5
        else:
            return 0.4

    # 不太在乎外观
    elif appearance_degree == 2:
        if car.appearance >= average_appearance * 1.2:
            return 0.7
        elif car.appearance > average_appearance and car.appearance < average_appearance * 1.2:
            return 0.7
        elif car.appearance <= average_appearance and car.appearance > average_appearance * 0.8:
            return 0.7
        else:
            return 0.5

    # 不在乎外观
    elif appearance_degree == 1:
        if car.appearance >= average_appearance * 1.2:
            return 0.7
        elif car.appearance > average_appearance and car.appearance < average_appearance * 1.2:
            return 0.7
        elif car.appearance <= average_appearance and car.appearance > average_appearance * 0.8:
            return 0.7
        else:
            return 0.7
