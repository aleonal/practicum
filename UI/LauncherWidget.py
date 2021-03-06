from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *

from CreateProject import CreateProjectWidget
from ProjectInfoWidget import ProjectInfoWidget
from src.ProjectController import ProjectController
from PopupWidget import PopupWidget

class LauncherWidget(QWidget):
    def __init__(self, previous_window=None):
        super().__init__()
        self.previous_window = previous_window
        self.UI()
        self.show()

    def UI(self):
        self.setObjectName("launcher_widget")

        # Window sizing
        self.resize(320, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(320, 240))

        # ABS Logo
        self.label = QtWidgets.QLabel(self)
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ABS.png"))#ABS logo
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Button to create new project
        self.new_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_button.sizePolicy().hasHeightForWidth())
        self.new_button.setSizePolicy(sizePolicy)
        self.new_button.setDefault(False)
        self.new_button.setObjectName("new_button")
        self.new_button.clicked.connect(self.newProject)

        # Button to open existing project
        self.open_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setObjectName("open_button")
        self.open_button.clicked.connect(self.openProject)

        # Layout that structures buttons
        self.button_layout = QtWidgets.QGridLayout()
        self.button_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.button_layout.setContentsMargins(-1, -1, -1, 0)
        self.button_layout.setSpacing(0)
        self.button_layout.setObjectName("button_layout")
        self.button_layout.addWidget(self.new_button, 0, 1, 1, 1)
        self.button_layout.addWidget(self.open_button, 0, 0, 1, 1)

        # Widget layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.button_layout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Widget", "Launcher"))
        self.new_button.setText(_translate("Widget", "New Project"))
        self.open_button.setText(_translate("Widget", "Open Project"))
        self.setWindowIcon(QtGui.QIcon("A.png"))# A icon

    def openProject(self):
        project_file = QFileDialog.getOpenFileName(self, 'Open file')

        try:
            if project_file[0]:
                ProjectController.load_project(project_file[0])
                self.project_info = ProjectInfoWidget(previous_window = self)
                self.project_info.show()
                self.hide()
            else:
                raise FileNotFoundError("No file selected")
        except FileNotFoundError as err:
            self.popup = PopupWidget(previous_window = self)
            self.popup.retranslateUi(popup_title = "File Error", popup_text = "File error: {0}".format(err))
            self.popup.show()
        except TypeError as err:
            self.popup = PopupWidget(previous_window = self)
            self.popup.retranslateUi(popup_title = "File Error", popup_text = "File error: {0}".format(err))
            self.popup.show()
            
    def newProject(self):
        self.creator = CreateProjectWidget(previous_window = self)
        self.creator.show()
        self.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

        #setup style sheet
    style = """
        QPushButton{
            color: #ffffff;
            background: #8f8f8f;
            border: 3px #000000 solid;
            padding: 5px 10px;
            border-radius: 2px;
            font-weight: plain;
            font-size: 9pt;
            outline: none;ss
        }
        QPushButton:hover{
            border: 3px #000000 solid;
            background: #80aaff;
        }
    """
    app.setStyleSheet(style)
    # # # # #end style
    ui = LauncherWidget()
    ui.show()
    sys.exit(app.exec_())