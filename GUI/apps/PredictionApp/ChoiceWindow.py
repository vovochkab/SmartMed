# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinishWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ChoiceWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 40, 321, 71))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 120, 311, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonLinear = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonLinear.setObjectName("radioButtonLinear")
        self.verticalLayout.addWidget(self.radioButtonLinear)
        self.radioButtonLogit = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonLogit.setObjectName("radioButtonLogit")
        self.verticalLayout.addWidget(self.radioButtonLogit)
        self.radioButtonRoc = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonRoc.setObjectName("radioButtonRoc")
        self.verticalLayout.addWidget(self.radioButtonRoc)
        self.radioButtonPol = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonPol.setObjectName("radioButtonPol")
        self.verticalLayout.addWidget(self.radioButtonPol)
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNext.setGeometry(QtCore.QRect(490, 400, 113, 32))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(320, 400, 113, 32))
        self.pushButtonBack.setObjectName("pushButtonBack")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Для начала основого этапа выберите</span></p><p><span style=\" font-size:18pt;\"> одну из регрессионных моделей:</span></p></body></html>"))
        self.radioButtonLinear.setText(_translate("MainWindow", "Множественная(линейная) регрессия"))
        self.radioButtonLogit.setText(_translate("MainWindow", "Логистическая регрессия"))
        self.radioButtonRoc.setText(_translate("MainWindow", "ROC-анализ"))
        self.radioButtonPol.setText(_translate("MainWindow", "Полиномиальная регрессия"))
        self.pushButtonNext.setText(_translate("MainWindow", "Вперед"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
