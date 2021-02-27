# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base QWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QtCore.QSize(640, 480))
        self.verticalLayoutWidget = QtWidgets.QWidget(Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 621, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.launcher_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.launcher_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.launcher_layout.setContentsMargins(0, 0, 0, 0)
        self.launcher_layout.setObjectName("launcher_layout")
        self.project_info = QtWidgets.QVBoxLayout()
        self.project_info.setObjectName("project_info")
        self.launcher_layout.addLayout(self.project_info)
        self.component_layout = QtWidgets.QGridLayout()
        self.component_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.component_layout.setContentsMargins(-1, -1, -1, 0)
        self.component_layout.setSpacing(0)
        self.component_layout.setObjectName("component_layout")
        self.runner_launcher = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runner_launcher.sizePolicy().hasHeightForWidth())
        self.runner_launcher.setSizePolicy(sizePolicy)
        self.runner_launcher.setObjectName("runner_launcher")
        self.component_layout.addWidget(self.runner_launcher, 0, 2, 1, 1)
        self.builder_launcher = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.builder_launcher.sizePolicy().hasHeightForWidth())
        self.builder_launcher.setSizePolicy(sizePolicy)
        self.builder_launcher.setObjectName("builder_launcher")
        self.component_layout.addWidget(self.builder_launcher, 0, 1, 1, 1)
        self.packager_launcher = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packager_launcher.sizePolicy().hasHeightForWidth())
        self.packager_launcher.setSizePolicy(sizePolicy)
        self.packager_launcher.setObjectName("packager_launcher")
        self.component_layout.addWidget(self.packager_launcher, 0, 0, 1, 1)
        self.launcher_layout.addLayout(self.component_layout)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.launcher_layout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.runner_launcher.setText(_translate("Widget", "Open\n"
"Runner"))
        self.builder_launcher.setText(_translate("Widget", "Open\n"
"Builder"))
        self.packager_launcher.setText(_translate("Widget", "Open\n"
"Packager"))
        self.pushButton.setText(_translate("Widget", "Launch\n"
"Project"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
