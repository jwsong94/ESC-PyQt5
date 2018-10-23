# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'esc_v1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)
        self.MView = QtWidgets.QGraphicsView(Frame)
        self.MView.setGeometry(QtCore.QRect(10, 10, 281, 281))
        self.MView.setObjectName("MView")
        self.BLabel = QtWidgets.QLabel(Frame)
        self.BLabel.setGeometry(QtCore.QRect(310, 40, 71, 16))
        self.BLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BLabel.setObjectName("BLabel")
        self.SLabel = QtWidgets.QLabel(Frame)
        self.SLabel.setGeometry(QtCore.QRect(320, 160, 59, 16))
        self.SLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SLabel.setObjectName("SLabel")
        self.BButton = QtWidgets.QPushButton(Frame)
        self.BButton.setGeometry(QtCore.QRect(300, 10, 91, 31))
        self.BButton.setObjectName("BButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.BLabel.setText(_translate("Frame", "Conn Stat"))
        self.SLabel.setText(_translate("Frame", "Sensors"))
        self.BButton.setText(_translate("Frame", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

