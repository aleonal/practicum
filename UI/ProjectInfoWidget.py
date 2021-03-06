from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *

from src.ProjectController import ProjectController


class ProjectInfoWidget(QWidget):
    def __init__(self, previous_window=None):
        super().__init__()
        self.project_data = ProjectController.get_project_info()
        self.previous_window = previous_window
        self.UI()
        self.show()

    def UI(self):
        self.setObjectName("project_info_widget")
        
        # Window sizing
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(440, 280))

        # Project details label
        self.project_label = QtWidgets.QLabel(self)
        self.project_label.setObjectName("project_label")


        # ABS Logo
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_label.setAutoFillBackground(False)
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("UI/ABS.png"))#ABS logo
        self.logo_label.setScaledContents(True)
        self.logo_label.setFixedSize(60,60)
        self.logo_label.setObjectName("label")

        # Project information list
        self.project_info = QtWidgets.QListWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_info.sizePolicy().hasHeightForWidth())
        self.project_info.setSizePolicy(sizePolicy)
        self.project_info.setMinimumSize(QtCore.QSize(0, 0))
        self.project_info.setObjectName("project_info")

        # populate project info list
        self.populate_project_info()

        # Layout for buttons
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.horizontalLayout.addWidget(self.close_button, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.setStretch(0, 1)

        # Widget layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.project_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.logo_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.project_info)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

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

    def populate_project_info(self):
        # project name, idx 0
        item = QtWidgets.QListWidgetItem()
        self.project_info.addItem(item)

        # project dir, idx 1
        item = QtWidgets.QListWidgetItem()
        self.project_info.addItem(item)

        # eceld root, idx 2
        item = QtWidgets.QListWidgetItem()
        self.project_info.addItem(item)

        # time frame, idx 3
        item = QtWidgets.QListWidgetItem()
        self.project_info.addItem(item)

        # white space, idx 4
        item = QtWidgets.QListWidgetItem()
        self.project_info.addItem(item)

        # salient artifact label, idx 5
        item = QtWidgets.QListWidgetItem()
        self.project_info.addItem(item)

        # salient artifacts
        for i in range(len(self.project_data['salient_artifacts'])):
            item = QtWidgets.QListWidgetItem()
            self.project_info.addItem(item)
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.setWindowTitle(_translate("Widget", "Project Information"))
        self.project_label.setText(_translate("Widget", "PROJECT DETAILS"))

        self.update_project_display()
        self.setWindowIcon(QtGui.QIcon("A.png"))# A icon
        

    def update_project_display(self):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.project_info.isSortingEnabled()
        self.project_data = ProjectController.get_project_info()
        self.project_info.setSortingEnabled(False)
        self.project_info.clear()

        self.project_info.addItem(QListWidgetItem("Project Name: {0}".format(self.project_data['project_name'])))
        self.project_info.addItem(QListWidgetItem("Project Directory: {0}".format(self.project_data['project_directory'])))
        self.project_info.addItem(QListWidgetItem("ECELd Data Directory: {0}".format(self.project_data['eceld_root'])))
        self.project_info.addItem(QListWidgetItem("Project Timeframe: {0}".format(self.project_data['time_frame'])))

        item = QListWidgetItem()
        item.setFlags(Qt.NoItemFlags)
        item.setText(_translate("Widget", " "))
        self.project_info.addItem(item)

        self.project_info.addItem(QListWidgetItem("Salient Artifacts"))
        
        for artifact in ProjectController.get_salient_artifacts_json():
            self.project_info.addItem(QListWidgetItem(str(artifact)))


        self.project_info.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ProjectInfoWidget()
    ui.show()
    sys.exit(app.exec_())