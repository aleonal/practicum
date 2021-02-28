# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Causation Extractor.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *


from ProjectInfoWidget import ProjectInfoWidget
from CreateProject import CreateProjectWidgets

class CausationExtractorWidget(object):
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
        self.progress = QtWidgets.QProgressBar(self.layoutWidget)
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.widget_layout.addWidget(self.progress, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)#Continue
        self.pushButton2 = QtWidgets.QPushButton(self.layoutWidget)#Canncel
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.widget_layout.addWidget(self.pushButton, 2, 0, 1, 1, QtCore.Qt.AlignLeft)#Continue
        self.pushButton.clicked.connect(self.launchProjectInfoWidget)
        self.pushButton2.setSizePolicy(sizePolicy)
        self.pushButton2.setCheckable(False)
        self.pushButton2.setAutoDefault(False)
        self.pushButton2.setDefault(False)
        self.pushButton2.setFlat(False)
        self.pushButton2.setObjectName("pushButton")
        self.widget_layout.addWidget(self.pushButton2, 2, 0, 1, 1, QtCore.Qt.AlignRight)#Cancel
        self.pushButton2.clicked.connect(self.launchCreateProject)

        self.progress_text = QtWidgets.QLabel(self.layoutWidget)
        self.progress_text.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_text.setObjectName("progress_text")
        self.widget_layout.addWidget(self.progress_text, 0, 0, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Causation Extractor"))
        self.pushButton.setText(_translate("Widget", "Continue"))
        self.pushButton2.setText(_translate("Widget", "Cancel"))
        self.progress_text.setText(_translate("Widget", "Progress info"))

    def launchProjectInfoWidget(self):
        self.pushButton = ProjectInfoWidget()
        self.pushButton.show()

    def launchCreateProject(self):
        self.pushButton2 = CreateProject()
        self.pushButton2.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
