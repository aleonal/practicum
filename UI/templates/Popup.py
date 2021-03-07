# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(320, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QtCore.QSize(320, 240))
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.popup_text = QtWidgets.QLabel(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popup_text.sizePolicy().hasHeightForWidth())
        self.popup_text.setSizePolicy(sizePolicy)
        self.popup_text.setAlignment(QtCore.Qt.AlignCenter)
        self.popup_text.setWordWrap(True)
        self.popup_text.setObjectName("popup_text")
        self.verticalLayout.addWidget(self.popup_text, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.continue_button = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_button.sizePolicy().hasHeightForWidth())
        self.continue_button.setSizePolicy(sizePolicy)
        self.continue_button.setObjectName("continue_button")
        self.verticalLayout.addWidget(self.continue_button, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.popup_text.setText(_translate("Widget", "Popup Info"))
        self.continue_button.setText(_translate("Widget", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
