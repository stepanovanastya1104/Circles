# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'circles.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Circles(object):
    def setupUi(self, Circles):
        Circles.setObjectName("Circles")
        Circles.resize(608, 497)
        Circles.setMinimumSize(QtCore.QSize(608, 497))
        Circles.setMaximumSize(QtCore.QSize(608, 497))
        self.show_btn = QtWidgets.QPushButton(Circles)
        self.show_btn.setGeometry(QtCore.QRect(220, 380, 161, 61))
        self.show_btn.setObjectName("show_btn")

        self.retranslateUi(Circles)
        QtCore.QMetaObject.connectSlotsByName(Circles)

    def retranslateUi(self, Circles):
        _translate = QtCore.QCoreApplication.translate
        Circles.setWindowTitle(_translate("Circles", "circles"))
        self.show_btn.setText(_translate("Circles", "Показать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Circles = QtWidgets.QWidget()
    ui = Ui_Circles()
    ui.setupUi(Circles)
    Circles.show()
    sys.exit(app.exec_())
