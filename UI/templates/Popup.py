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
        self.layoutWidget = QtWidgets.QWidget(Widget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.widget_layout = QtWidgets.QGridLayout(self.layoutWidget)
        self.widget_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setSpacing(0)
        self.widget_layout.setObjectName("widget_layout")
        self.continue_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_button.sizePolicy().hasHeightForWidth())
        self.continue_button.setSizePolicy(sizePolicy)
        self.continue_button.setObjectName("continue_button")
        self.widget_layout.addWidget(self.continue_button, 1, 0, 1, 1)
        self.popup_text = QtWidgets.QLabel(self.layoutWidget)
        self.popup_text.setAlignment(QtCore.Qt.AlignCenter)
        self.popup_text.setObjectName("popup_text")
        self.widget_layout.addWidget(self.popup_text, 0, 0, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.continue_button.setText(_translate("Widget", "Continue"))
        self.popup_text.setText(_translate("Widget", "Popup Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
