# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 80, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged.connect(self.left_motor)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(127)
        self.horizontalSlider_2 = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(230, 80, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(127)
        self.horizontalSlider_2.valueChanged.connect(self.right_motor)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setReadOnly(True)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(60, 110, 121, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 110, 121, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 40, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 21, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 60, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 60, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(370, 60, 55, 16))
        self.label_6.setObjectName("label_6")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "3PI Motor Twiddler"))
        self.label.setText(_translate("Dialog", "Left Motor"))
        self.label_2.setText(_translate("Dialog", "Right Motor"))
        self.label_3.setText(_translate("Dialog", "0"))
        self.label_4.setText(_translate("Dialog", "127"))
        self.label_5.setText(_translate("Dialog", "0"))
        self.label_6.setText(_translate("Dialog", "127"))
    def left_motor(self):
        print("left motor value is:")
        print(self.horizontalSlider.value())
        motorStrenght=self.horizontalSlider.value()
        self.textEdit.setText(str(hex(motorStrenght))+"    "+str(motorStrenght)) #pretty print the values
    def right_motor(self):
        print("right motor value is:")
        print(self.horizontalSlider_2.value())
        motorStrenght=self.horizontalSlider_2.value()
        self.textEdit_2.setText(str(hex(motorStrenght))+"    "+str(motorStrenght))
