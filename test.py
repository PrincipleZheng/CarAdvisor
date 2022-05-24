# -*- coding:utf-8 -*-
import sys
from UI import styleBook
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon
from stqt import mainWindows

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = mainWindows()
    mainWindow.setWindowTitle('Single Table Query Tools')
    mainWindow.setWindowIcon(QIcon('./LOGO.ico'))
    main_qss = styleBook.get_main_style()
    mainWindow.setStyleSheet(main_qss)
    mainWindow.show()
    sys.exit(app.exec_())