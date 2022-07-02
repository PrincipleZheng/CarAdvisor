'''
Author: Zheng
Date: 2022-05-20 01:57:25
LastEditors: Zheng
LastEditTime: 2022-05-20 02:44:52
Description: default description
'''
import sys

from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication
from PyQt5.Qt import QT_VERSION_STR
from PyQt5.QtCore import QVersionNumber, Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from functools import partial
from PyQt5.uic.properties import QtWidgets
from car import *
from makeDecision import makeDecision
import userQuestions

# def convert(ui):
#     input = ui.plainTextEdit.toPlainText()
#     result = float(input) * 6.7
#     print(result)
#     ui.plainTextEdit_2.setPlainText(str(result))
list = []
recommend_level = []
reasons = []
currentIndex = 0
# 全局变量
def select(ui):
    cars = []
    min_price = 0
    max_price = 0
    if ui.checkBox_10_20.isChecked():
        min_price = 10
        max_price = 20
    elif ui.checkBox_20_30.isChecked():
        min_price = 20
        max_price = 30
    elif ui.checkBox_30_50.isChecked():
        min_price = 30
        max_price = 50
    elif ui.checkBox_50.isChecked():
        min_price = 50
        max_price = 1000000
    # print(min_price, max_price)
    cartypes = []
    if ui.checkBox_big.isChecked():
        cartypes.append('大型车')
    if ui.checkBox_mid.isChecked():
        cartypes.append('中型车')
    if ui.checkBox_small.isChecked():
        cartypes.append('小型车')
    if ui.checkBox_suv.isChecked():
        cartypes.append('SUV')
    if ui.checkBox_mpv.isChecked():
        cartypes.append('MPV')
    if ui.checkBox_sports.isChecked():
        cartypes.append('跑车')

    # 各项指标 默认为1 即“完全不在乎”
    worthy_degree = 1
    if ui.checkBox_worthy_1.isChecked():
        worthy_degree = 1
    elif ui.checkBox_worthy_2.isChecked():
        worthy_degree = 2
    elif ui.checkBox_worthy_3.isChecked():
        worthy_degree = 3
    elif ui.checkBox_worthy_4.isChecked():
        worthy_degree = 4

    performance_degree = 1
    if ui.checkBox_performance_1.isChecked():
        performance_degree = 1
    elif ui.checkBox_performance_2.isChecked():
        performance_degree = 2
    elif ui.checkBox_performance_3.isChecked():
        performance_degree = 3
    elif ui.checkBox_performance_4.isChecked():
        performance_degree = 4

    comfortable_degree = 1
    if ui.checkBox_comfortable_1.isChecked():
        comfortable_degree = 1
    elif ui.checkBox_comfortable_2.isChecked():
        comfortable_degree = 2
    elif ui.checkBox_comfortable_3.isChecked():
        comfortable_degree = 3
    elif ui.checkBox_comfortable_4.isChecked():
        comfortable_degree = 4

    appearance_degree = 1
    if ui.checkBox_appearance_1.isChecked():
        appearance_degree = 1
    elif ui.checkBox_appearance_2.isChecked():
        appearance_degree = 2
    elif ui.checkBox_appearance_3.isChecked():
        appearance_degree = 3
    elif ui.checkBox_appearance_4.isChecked():
        appearance_degree = 4
    global reasons
    cars.clear()
    reasons.clear()

    cars, reasons = makeDecision(min_price, max_price, cartypes, worthy_degree, performance_degree, comfortable_degree,appearance_degree)
    # print all reasons
    # for car in cars:
    #     print(car.name)
    # for reason in reasons:
    #     print(reason)

    list.clear()
    for car in cars:
        # print(car)
        # print(findRawCar(car))
        list.append(findRawCar(car))
    # for RawCar in list:
    #     print(RawCar)
    ui.label_3.setText('为您找到 '+str(len(list))+' 辆车')

    recommend_level.clear()
    total_nums = len(list)
    level_distince = 100 / (total_nums+1)
    for i in range(total_nums):
        if (i+1) * level_distince >= 100:
            recommend_level.append(100)
        else:
            recommend_level.append((i+1) * level_distince)
    recommend_level.reverse()

    # for car in cars:
    #     print(car.name)
    # todo: 新建界面展示车辆信息
    if list.__len__() == 0:
        ui.label_3.setText('没有找到车辆')
        ui.label_img.setPixmap(QPixmap('pics/defaultCar.png'))
    else:
        ui.titleLable.setText(list[0].name)

        ui.value1.setText(str(list[0].number))
        ui.value2.setText(list[0].type)
        ui.value3.setText(str(list[0].price))
        ui.value4.setText(str(list[0].appearance))
        ui.value5.setText(str(list[0].displacement))
        ui.value6.setText(str(list[0].horsepower))
        ui.value7.setText(str(list[0].torque))
        ui.value8.setText(str(list[0].length))
        ui.value9.setText(str(list[0].width))
        ui.value10.setText(str(list[0].height))
        ui.value11.setText(str(list[0].wheelbase))
        ui.recommendLabel.setText(reasons[0])

        # 设置推荐度 按列表排序 第一为100% 末尾为0%
        ui.progressBar.setProperty("value", recommend_level[0])

        # ui.imglinkLable.setText('详细链接：'+list[0].img_url)

        local_pic_path = 'pics/'+str(list[0].number)+'.png'
        ui.label_img.setPixmap(QPixmap(local_pic_path))
        # ui.label_img.setPixmap(QPixmap('pics/kmr.png'))


def clear(ui):
    if ui.checkBox_10_20.isChecked():
        ui.checkBox_10_20.setChecked(False)
    if ui.checkBox_20_30.isChecked():
        ui.checkBox_20_30.setChecked(False)
    if ui.checkBox_30_50.isChecked():
        ui.checkBox_30_50.setChecked(False)
    if ui.checkBox_50.isChecked():
        ui.checkBox_50.setChecked(False)
    if ui.checkBox_big.isChecked():
        ui.checkBox_big.setChecked(False)
    if ui.checkBox_mid.isChecked():
        ui.checkBox_mid.setChecked(False)
    if ui.checkBox_small.isChecked():
        ui.checkBox_small.setChecked(False)
    if ui.checkBox_suv.isChecked():
        ui.checkBox_suv.setChecked(False)
    if ui.checkBox_mpv.isChecked():
        ui.checkBox_mpv.setChecked(False)
    if ui.checkBox_sports.isChecked():
        ui.checkBox_sports.setChecked(False)
    if ui.checkBox_worthy_1.isChecked():
        ui.checkBox_worthy_1.setChecked(False)
    if ui.checkBox_worthy_2.isChecked():
        ui.checkBox_worthy_2.setChecked(False)
    if ui.checkBox_worthy_3.isChecked():
        ui.checkBox_worthy_3.setChecked(False)
    if ui.checkBox_worthy_4.isChecked():
        ui.checkBox_worthy_4.setChecked(False)
    if ui.checkBox_performance_1.isChecked():
        ui.checkBox_performance_1.setChecked(False)
    if ui.checkBox_performance_2.isChecked():
        ui.checkBox_performance_2.setChecked(False)
    if ui.checkBox_performance_3.isChecked():
        ui.checkBox_performance_3.setChecked(False)
    if ui.checkBox_performance_4.isChecked():
        ui.checkBox_performance_4.setChecked(False)
    if ui.checkBox_comfortable_1.isChecked():
        ui.checkBox_comfortable_1.setChecked(False)
    if ui.checkBox_comfortable_2.isChecked():
        ui.checkBox_comfortable_2.setChecked(False)
    if ui.checkBox_comfortable_3.isChecked():
        ui.checkBox_comfortable_3.setChecked(False)
    if ui.checkBox_comfortable_4.isChecked():
        ui.checkBox_comfortable_4.setChecked(False)
    if ui.checkBox_appearance_1.isChecked():
        ui.checkBox_appearance_1.setChecked(False)
    if ui.checkBox_appearance_2.isChecked():
        ui.checkBox_appearance_2.setChecked(False)
    if ui.checkBox_appearance_3.isChecked():
        ui.checkBox_appearance_3.setChecked(False)
    if ui.checkBox_appearance_4.isChecked():
        ui.checkBox_appearance_4.setChecked(False)


def viewprevious(ui, index):
    num = list.__len__()
    if num == 0:
        return
    global currentIndex
    if currentIndex > 0:
        currentIndex -= 1
    elif currentIndex == 0:
        currentIndex = num - 1
    ui.titleLable.setText(list[currentIndex].name)
    ui.value1.setText(str(list[currentIndex].number))
    ui.value2.setText(list[currentIndex].type)
    ui.value3.setText(str(list[currentIndex].price))
    ui.value4.setText(str(list[currentIndex].appearance))
    ui.value5.setText(str(list[currentIndex].displacement))
    ui.value6.setText(str(list[currentIndex].horsepower))
    ui.value7.setText(str(list[currentIndex].torque))
    ui.value8.setText(str(list[currentIndex].length))
    ui.value9.setText(str(list[currentIndex].width))
    ui.value10.setText(str(list[currentIndex].height))
    ui.value11.setText(str(list[currentIndex].wheelbase))
    # ui.imglinkLable.setText('详细链接：'+list[currentIndex].img_url)
    local_pic_path = 'pics/' + str(list[currentIndex].number) + '.png'
    ui.label_img.setPixmap(QPixmap(local_pic_path))
    ui.progressBar.setProperty("value", recommend_level[currentIndex])
    ui.recommendLabel.setText(reasons[currentIndex])


def viewnext(ui):
    num = list.__len__()
    if num == 0:
        return
    global currentIndex
    if currentIndex < num - 1:
        currentIndex += 1
    elif currentIndex == num - 1:
        currentIndex = 0
    ui.titleLable.setText(list[currentIndex].name)
    ui.value1.setText(str(list[currentIndex].number))
    ui.value2.setText(list[currentIndex].type)
    ui.value3.setText(str(list[currentIndex].price))
    ui.value4.setText(str(list[currentIndex].appearance))
    ui.value5.setText(str(list[currentIndex].displacement))
    ui.value6.setText(str(list[currentIndex].horsepower))
    ui.value7.setText(str(list[currentIndex].torque))
    ui.value8.setText(str(list[currentIndex].length))
    ui.value9.setText(str(list[currentIndex].width))
    ui.value10.setText(str(list[currentIndex].height))
    ui.value11.setText(str(list[currentIndex].wheelbase))
    # ui.imglinkLable.setText('详细链接：'+list[currentIndex].img_url)
    local_pic_path = 'pics/' + str(list[currentIndex].number) + '.png'
    ui.label_img.setPixmap(QPixmap(local_pic_path))
    ui.progressBar.setProperty("value", recommend_level[currentIndex])
    ui.recommendLabel.setText(reasons[currentIndex])



if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = userQuestions.Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Recommendation = QMainWindow()
    # ui_recommendation = recommendWindow.Ui_MainWindow()
    # ui_recommendation.setupUi(Recommendation)

    MainWindow.show()

    ui.pushButton.clicked.connect(partial(select, ui))
    ui.pushButton_2.clicked.connect(partial(clear, ui))
    ui.pushButton_3.clicked.connect(partial(viewnext, ui))
    ui.pushButton_5.clicked.connect(partial(viewprevious, ui))
    # ui.pushButton.clicked.connect(partial(convert, ui))
    sys.exit(app.exec_())

    # v_compare = QVersionNumber(5,6,0)
    # v_current = QVersionNumber.fromString(QT_VERSION_STR) #获取当前Qt版本
    #
    # if QVersionNumber.compare(v_current,v_compare) >= 0:
    #     QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    #     app = QApplication(sys.argv)
    # else:
    #     app = QApplication(sys.argv)
    #     font = QFont("宋体")
    #     pointsize = font.pointSize()
    #     font.setPixelSize(pointsize*90/72)
    #     app.setFont(font)
    #
    # MainWindow = QMainWindow()
    # ui = userQuestions.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # ui.pushButton.clicked.connect(partial(select, ui))
    # # ui.pushButton.clicked.connect(partial(convert, ui))
    # sys.exit(app.exec_())
