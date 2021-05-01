# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
from src.ValidatorController import ValidatorController
from subprocess import Popen, PIPE

import sys
import os
import subprocess, signal, time, ctypes
import re 
from src.ProjectController import ProjectController

class RunnerWidget(QWidget):
    def __init__(self, project=None):
        super().__init__()
        self.setWindowTitle("Runner")
        self.setGeometry(50,50,482,432)
        self.UI()
        self.show()
        self.script_name = None

    def UI(self):
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")

        # Script display window
        self.script_display = QPlainTextEdit()
        self.script_display.setGeometry(QtCore.QRect(10,40,381,471))
        self.script_display.setReadOnly(True)

        # Load Script onto display window button/action
        self.load_script_button = QtWidgets.QPushButton(self)
        self.load_script_button.setGeometry(QtCore.QRect(370, 480, 151, 41))
        self.load_script_button.setObjectName("load_script_button")
        self.load_script_button.clicked.connect(self.display_script)

        # Script run button/script execution
        self.run_button = QtWidgets.QPushButton(self)
        self.run_button.setGeometry(QtCore.QRect(700,520,75,23))
        self.run_button.setObjectName("run_button")
        self.run_button.clicked.connect(self.execute_script)
        self.run_button.setEnabled(False)

        # Script stop button/stop script execution
        self.stop_button = QtWidgets.QPushButton(self)
        self.stop_button.setGeometry(QtCore.QRect(620,520,75,23))
        self.stop_button.setObjectName("stop_button")
        self.stop_button.clicked.connect(self.stop_script)
        self.stop_button.setEnabled(False)

        # Progress terminal
        self.progress_terminal = QtWidgets.QTextEdit()
        self.progress_terminal.setGeometry(QtCore.QRect(400, 40, 381, 471))
        self.progress_terminal.setObjectName("progress_terminal")
        self.proc = QtCore.QProcess(self)
        self.error = False
        self.stop = False
        self.proc.readyReadStandardError.connect(self.stderrReady)
        self.proc.stateChanged.connect(self.handle_state)
        self.proc.started.connect(lambda: self.run_button.setEnabled(False))
        self.proc.finished.connect(lambda: self.run_button.setEnabled(True))
        self.proc.finished.connect(self.success_message)
        
        # Timeout
        self.script_timeout = QtWidgets.QSpinBox(self)
        self.script_timeout.setGeometry(QtCore.QRect(370, 450, 151, 22))
        self.script_timeout.setMinimum(1)
        self.script_timeout.setObjectName("script_timeout")
        
        # Widget layout
        self.gridLayout.addWidget(self.progress_terminal,1,3)
        self.gridLayout.addWidget(self.script_timeout,2,3)
        self.gridLayout.addWidget(self.run_button, 0,3)
        self.gridLayout.addWidget(self.stop_button, 3,3)
        self.gridLayout.addWidget(self.load_script_button,0,0)
        self.gridLayout.addWidget(self.script_display, 1, 0)
        self.setLayout(self.gridLayout)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("RunnerTab", "Runner"))
        self.load_script_button.setText(_translate("RunnerTab", "Load Script"))
        self.run_button.setText(_translate("RunnerTab", "Run"))
        self.stop_button.setText(_translate("RunnerTab", "Stop"))

    def execute_script(self):  
        self.error = False
        self.stop = False
        script_py = self.script_name.replace('.json', '.py')
        self.stop_button.setEnabled(True)

        '''
        To communicate with PDB process, write self.script_process.stdin.write(args),
        where args is a string consisting of a PDB command, followed by a line break (\n).

        I don't expect us to use anything other than 'n' command, as that executes the current line
        but avoids going into function calls.

        Example: self.script_process.stdin.write('n\n'.encode())

        Command list: https://docs.python.org/3/library/pdb.html
        '''

        self.script_process = Popen(["python3", "-m", "pdb", script_py], stdin=PIPE, close_fds=True)
        
        '''
        Maybe turn line below into thread? Makes sense since validator needs to communicate
        with PDB. The reason that it needs to be a thread is so that it doesn't block GUI.
        Gotta test super quick, I'll work on this (Antoine). The way the validator works depends
        on this, but I've had that mapped out for a while.
        '''

        # self.validator_process = Popen(["python3", "-m", "src.Validator", str(self.script_timeout.value())], stdin=PIPE, close_fds=True, cwd=os.getcwd())

        '''
        Used this to test that writing to PDB process worked. Tested working 5:29am, 5/1/21
        for i in range(0, 5):
            self.script_process.stdin.write('n\n'.encode())
        '''

    def print_progress(self, text):
        cursor = self.progress_terminal.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)

    def stderrReady(self):
        for item in self.proc.readAllStandardError():
            self.print_progress(item.decode("utf-8"))
        self.error = True
        
    def handle_state(self, state):
        states = {QProcess.NotRunning: "Not running",
                  QProcess.Starting: "Starting",
                  QProcess.Running: "Running",
        }
        state_name = states[state]
        self.print_progress(f"\nState changed: {state_name}\n")

    def success_message(self):
        if not self.stop and not self.error:
            self.print_progress("\nSuccess\n")
        
    def stop_script(self):
        self.script_process.kill()
        self.validator_process.kill()
        self.stop = True
        self.stop_button.setEnabled(False)
        self.run_button.setEnabled(True)

    def display_script(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.script_name, _ = QFileDialog.getOpenFileName(self,"Open Script", "","All Files (*);;Python Files (*.json)", options=options)
            with open(self.script_name, 'r') as f:
                self.script_display.setPlainText(f.read())
            self.run_button.setEnabled(True)
            self.progress_terminal.clear()
        except:
            self.load_error_message()
    
    def load_error_message(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Error")
        messageBox.setText("Selected file is invalid.")
        messageBox.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = RunnerWidget()
    ui.show()
    sys.exit(app.exec_())
   