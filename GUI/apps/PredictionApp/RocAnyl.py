# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RocAnyl.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 40, 141, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 341, 21))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 130, 321, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxTrashhold = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxTrashhold.setObjectName("checkBoxTrashhold")
        self.verticalLayout.addWidget(self.checkBoxTrashhold)
        self.checkBoxRecall = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxRecall.setObjectName("checkBoxRecall")
        self.verticalLayout.addWidget(self.checkBoxRecall)
        self.checkBoxPrecision = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxPrecision.setObjectName("checkBoxPrecision")
        self.verticalLayout.addWidget(self.checkBoxPrecision)
        self.checkBoxAccur = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxAccur.setObjectName("checkBoxAccur")
        self.verticalLayout.addWidget(self.checkBoxAccur)
        self.checkBoxF = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxF.setObjectName("checkBoxF")
        self.verticalLayout.addWidget(self.checkBoxF)
        self.checkBoxConf = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxConf.setObjectName("checkBoxConf")
        self.verticalLayout.addWidget(self.checkBoxConf)
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(350, 400, 113, 32))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.pushButtonDone = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDone.setGeometry(QtCore.QRect(510, 400, 113, 32))
        self.pushButtonDone.setObjectName("pushButtonDone")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Выбор метрик:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Выберите показатели, которые хотите посчитать:</span></p></body></html>"))
        self.checkBoxTrashhold.setText(_translate("MainWindow", "Оптимальный порог сечения"))
        self.checkBoxRecall.setText(_translate("MainWindow", "Полнота"))
        self.checkBoxPrecision.setText(_translate("MainWindow", "Точность"))
        self.checkBoxAccur.setText(_translate("MainWindow", "Доля верных ответов"))
        self.checkBoxF.setText(_translate("MainWindow", "F-мера"))
        self.checkBoxConf.setText(_translate("MainWindow", "Построить доверительный интервал"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
        self.pushButtonDone.setText(_translate("MainWindow", "Завершить"))
