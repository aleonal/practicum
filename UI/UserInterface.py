# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.BuilderWidget import BuilderWidget
from UI.RunnerWidget import RunnerWidget
from UI.PackagerWidget import PackagerWidget
from UI.CreateProject import CreateProjectWidget
from UI.ProjectInfoWidget import ProjectInfoWidget
from src.ProjectController import ProjectController
import os
import sys

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        #app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        #ui = Ui_MainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        #sys.exit(app.exec_())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 720)
        MainWindow.setDockNestingEnabled(True)
        self.layout = QtWidgets.QVBoxLayout()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(self.layout)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1101, 811))
        self.tabWidget.setObjectName("tabWidget")

        #Creating Project Info tab
        self.project_info_tab = ProjectInfoWidget()
        self.project_info_tab.setAccessibleName("ProjectInfoWidget")
        self.project_info_tab.setObjectName("project_info_tab")
        self.tabWidget.addTab(self.project_info_tab, "")

        #Creating Builder tab
        self.builder_tab = BuilderWidget()
        self.builder_tab.setAccessibleName("BuilderWidget")
        self.builder_tab.setObjectName("builder_tab")
        self.tabWidget.addTab(self.builder_tab, "")
        #self.tabWidget.setTabEnabled(1,False) #Disable Builder Tab

        #Creating Runner tab
        self.runner_tab = RunnerWidget()
        self.runner_tab.setAccessibleName("RunnerWidget")
        self.runner_tab.setObjectName("runner_tab")
        self.tabWidget.addTab(self.runner_tab, "")
        #self.tabWidget.setTabEnabled(2,False) #Disable Runner Tab

        #Add all our tabs into our main windows layout
        self.layout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        #Setup menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        #Setup statusbar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Setup actions
        self.actionNew_Project = QtWidgets.QAction(MainWindow, triggered=self.new_project)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionOpen_Project = QtWidgets.QAction(MainWindow, triggered=self.open_directory)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionImport_Raw_Data = QtWidgets.QAction(MainWindow)
        self.actionImport_Raw_Data.setObjectName("actionImport_Raw_Data")
        self.actionExport_Project = QtWidgets.QAction(MainWindow)
        self.actionExport_Project.setObjectName("actionExport_Project")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionSave_Project_As = QtWidgets.QAction(MainWindow, triggered=self.save_file)


        self.actionSave_Project_As.setObjectName("actionSave_Project_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionFind_Replace = QtWidgets.QAction(MainWindow)
        self.actionFind_Replace.setObjectName("actionFind_Replace")
        self.actionCausation_Extractor = QtWidgets.QAction(MainWindow)
        self.actionCausation_Extractor.setObjectName("actionCausation_Extractor")
        self.actionOpen_Builder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Builder.setObjectName("actionOpen_Builder")
        self.actionOpen_Runner = QtWidgets.QAction(MainWindow)
        self.actionOpen_Runner.setObjectName("actionOpen_Runner")
        self.actionOpen_Packager = QtWidgets.QAction(MainWindow)
        self.actionOpen_Packager.setObjectName("actionOpen_Packager")

        #Add actions to menu buttons
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionImport_Raw_Data)
        self.menuFile.addAction(self.actionExport_Project)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionSave_Project_As)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionFind_Replace)
        self.menuView.addAction(self.actionCausation_Extractor)
        self.menuView.addAction(self.actionOpen_Builder)
        self.menuView.addAction(self.actionOpen_Runner)
        self.menuView.addAction(self.actionOpen_Packager)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def new_project(self):
        self.project_window = CreateProjectWidget(previous_window=self)
        self.project_window.show()


    def open_directory(self):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QFileDialog(), "Select Directory", directory=os.path.realpath(os.getcwd())))
        ProjectController.load_project(directory)

        if(ProjectController.is_project_loaded):
            QMessageBox.information(self.centralwidget, "Success", "Project has been loaded successfully.")
            self.update_tabs()
        else:
            QMessageBox.critical(self.centralwidget, "Project Failure", "Project could not be loaded. Check that directory contains appropriate files")

    def save_file(self):
        file = str(QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QFileDialog(), "Save File", directory=os.path.realpath(os.getcwd())))
        #save file
        #We will get the file name, now we have to write to it

    # Updates Builder tab when project is loaded
    def update_tabs(self):
        if(ProjectController.is_project_loaded):
            self.project_info_tab.update_project_display()
            #Remove builder tab and insert it again - updates information
            self.tabWidget.removeTab(1)
            self.tabWidget.insertTab(1, BuilderWidget(), "Builder")
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agent Build System"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.project_info_tab), _translate("MainWindow", "Project Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.builder_tab), _translate("MainWindow", "Builder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.runner_tab), _translate("MainWindow", "Runner"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionImport_Raw_Data.setText(_translate("MainWindow", "Import Raw Data"))
        self.actionExport_Project.setText(_translate("MainWindow", "Export Project"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project"))
        self.actionSave_Project_As.setText(_translate("MainWindow", "Save Project As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionFind_Replace.setText(_translate("MainWindow", "Find/Replace"))
        self.actionCausation_Extractor.setText(_translate("MainWindow", "Causation Extractor"))
        self.actionOpen_Builder.setText(_translate("MainWindow", "Open Builder"))
        self.actionOpen_Runner.setText(_translate("MainWindow", "Open Runner"))
        self.actionOpen_Packager.setText(_translate("MainWindow", "Open Packager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
