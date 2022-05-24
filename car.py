'''
Author: Zheng
Date: 2022-05-20 14:48:30
LastEditors: Zheng
LastEditTime: 2022-05-20 15:02:52
Description: default description
'''
class Car():
    def __init__(self, number, name, type, price, appearance, power, comfort_level):
        self.number = number
        self.name = name
        self.type = type
        self.price = price
        self.appearance = appearance
        self.power = power
        self.comfort_level = comfort_level

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.number, self.name, self.type, self.price, self.appearance, self.power, self.comfort_level)


class RawCar():
    def __init__(self, number, name, type, price, appearance, displacement, horsepower, torque, length, width, height, wheelbase, img_url):
        self.number = number
        self.name = name
        self.type = type
        self.price = price
        self.appearance = appearance
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque
        self.length = length
        self.width = width
        self.height = height
        self.wheelbase = wheelbase
        self.img_url = img_url

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {} {} {}'.format(self.number, self.name, self.type, self.price, self.appearance, self.displacement, self.horsepower, self.torque, self.length, self.width, self.height, self.wheelbase, self.img_url)


def findRawCar(Car):
    with open('./data/rawData.csv', 'r') as f:
        for line in f.readlines():
            line = line.strip().split(',')
            if int(line[0]) == Car.number:
                res = RawCar(int(line[0]), line[1], line[2], float(line[3]), float(line[4]), float(line[5]), float(line[6]), float(line[7]), float(line[8]), float(line[9]), float(line[10]), float(line[11]), line[12])
                return res