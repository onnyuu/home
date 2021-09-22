# coding: utf-8

from PySide2 import QtWidgets, QtCore, QtGui
from maya import OpenMayaUI as omUI

import maya.cmds as cmds
import shiboken2


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(self.get_maya_window())
        self.setWindowTitle("Curve Object")

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # mainのVBoxレイアウト作成
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(self.mainLayout)

        self.label = QtWidgets.QLabel(u'生産したいボタンを押してください。')
        self.mainLayout.addWidget(self.label)

        self.nodeButtonLayout = QtWidgets.QGridLayout()
        self.nodeButtonWidget = QtWidgets.QWidget()
        self.nodeButtonWidget.setLayout(self.nodeButtonLayout)
        self.mainLayout.addWidget(self.nodeButtonWidget)
        self.diamondButton = QtWidgets.QPushButton()
        self.nodeButtonLayout.addWidget(self.diamondButton, 0, 0)
        self.diamondButton.setIcon(QtGui.QIcon(':/polyOctahedron.svg'))
        self.diamondButton.setIconSize(QtCore.QSize(40, 40))
        self.diamondButton.setFixedSize(50, 50)

        self.boxButton = QtWidgets.QPushButton()
        self.nodeButtonLayout.addWidget(self.boxButton, 0, 1)
        self.boxButton.setIcon(QtGui.QIcon(':/polyCube.svg'))
        self.boxButton.setIconSize(QtCore.QSize(40, 40))
        self.boxButton.setFixedSize(50, 50)

        self.sphereButton = QtWidgets.QPushButton()
        self.nodeButtonLayout.addWidget(self.sphereButton, 0, 2)
        self.sphereButton.setIcon(QtGui.QIcon(':/polySphere.svg'))
        self.sphereButton.setIconSize(QtCore.QSize(40, 40))
        self.sphereButton.setFixedSize(50, 50)

        self.circleButton = QtWidgets.QPushButton()
        self.nodeButtonLayout.addWidget(self.circleButton, 1, 0)
        self.circleButton.setIcon(QtGui.QIcon(':/circle.png'))
        self.circleButton.setIconSize(QtCore.QSize(40, 40))
        self.circleButton.setFixedSize(50, 50)

        self.coneButton = QtWidgets.QPushButton()
        self.nodeButtonLayout.addWidget(self.coneButton, 1, 1)
        self.coneButton.setIcon(QtGui.QIcon(':/polyPyramid.svg'))
        self.coneButton.setIconSize(QtCore.QSize(40, 40))
        self.coneButton.setFixedSize(50, 50)

        self.planeButton = QtWidgets.QPushButton()
        self.nodeButtonLayout.addWidget(self.planeButton, 1, 2)
        self.planeButton.setIcon(QtGui.QIcon(':/polyPlane.svg'))
        self.planeButton.setIconSize(QtCore.QSize(40, 40))
        self.planeButton.setFixedSize(50, 50)

        self.scaleWidget = QtWidgets.QWidget()
        self.mainLayout.addWidget(self.scaleWidget)
        self.scaleLayout = QtWidgets.QGridLayout()
        self.scaleWidget.setLayout(self.scaleLayout)
        self.scaleTitle = QtWidgets.QLabel('Scale')
        self.scaleXLabel = QtWidgets.QLabel('X')
        self.scaleYLabel = QtWidgets.QLabel('Y')
        self.scaleZLabel = QtWidgets.QLabel('Z')
        self.scaleXLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.scaleYLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.scaleZLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.scaleXLine = QtWidgets.QLineEdit()
        self.scaleYLine = QtWidgets.QLineEdit()
        self.scaleZLine = QtWidgets.QLineEdit()
        self.scaleXLine.setFixedWidth(30)
        self.scaleYLine.setFixedWidth(30)
        self.scaleZLine.setFixedWidth(30)
        self.scaleXLine.setText('1')
        self.scaleYLine.setText('1')
        self.scaleZLine.setText('1')
        self.scaleLayout.addWidget(self.scaleXLabel, 0, 2)
        self.scaleLayout.addWidget(self.scaleYLabel, 0, 3)
        self.scaleLayout.addWidget(self.scaleZLabel, 0, 4)
        self.scaleLayout.addWidget(self.scaleTitle, 1, 1)
        self.scaleLayout.addWidget(self.scaleXLine, 1, 2)
        self.scaleLayout.addWidget(self.scaleYLine, 1, 3)
        self.scaleLayout.addWidget(self.scaleZLine, 1, 4)
        self.scaleLayout.setColumnStretch(0, 100)

        self.buttonWidget = QtWidgets.QWidget()
        self.mainLayout.addWidget(self.buttonWidget)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonWidget.setLayout(self.buttonLayout)
        self.closeButton = QtWidgets.QPushButton('Close')
        self.buttonLayout.addWidget(self.closeButton)

        # connection
        self.diamondButton.clicked.connect(self.get_diamond)
        self.boxButton.clicked.connect(self.get_box)
        self.sphereButton.clicked.connect(self.get_sphere)
        self.circleButton.clicked.connect(self.get_circle)
        self.closeButton.clicked.connect(self.close_button_clicked)

    def close_button_clicked(self):
        self.close()

    def get_maya_window(self):
        u'''MAYAのメインウィンドウを取得し、QtWidgets.QMainWindow型で戻す'''
        ptr = omUI.MQtUtil.mainWindow()
        if ptr is not None:
            return shiboken2.wrapInstance(int(ptr), QtWidgets.QMainWindow)

    def get_diamond(self, name='', scale=[1, 1, 1]):
        coefficient = 5.0
        x = scale[0] * coefficient
        y = scale[1] * coefficient
        z = scale[2] * coefficient
        node = cmds.curve(
            degree=1,
            point=[
                (0.0 * x, 1.0 * y, 0.0 * z),
                (-1.0 * x, 0.0 * y, 0.0 * z),
                (0.0 * x, -1.0 * y, 0.0 * z),
                (1.0 * x, 0.0 * y, 0.0 * z),
                (0.0 * x, 1.0 * y, 0.0 * z),
                (0.0 * x, 0.0 * y, 1.0 * z),
                (0.0 * x, -1.0 * y, 0.0 * z),
                (0.0 * x, 0.0 * y, -1.0 * z),
                (-1.0 * x, 0.0 * y, 0.0 * z),
                (0.0 * x, 0.0 * y, 1.0 * z),
                (1.0 * x, 0.0 * y, 0.0 * z),
                (0.0 * x, 0.0 * y, -1.0 * z),
                (0.0 * x, 1.0 * y, 0.0 * z)
            ]
        )

        if name != '':
            cmds.rename(node, name)

    def get_box(self, name='', scale=[1, 1, 1]):
        coefficient = 5.0
        x = scale[0] * coefficient
        y = scale[1] * coefficient
        z = scale[2] * coefficient
        node = cmds.curve(
            degree=1,
            point=[
                (1 * x, 1 * y, 1 * z),
                (1 * x, -1 * y, 1 * z),
                (-1 * x, -1 * y, 1 * z),
                (-1 * x, 1 * y, 1 * z),
                (1 * x, 1 * y, 1 * z),
                (1 * x, 1 * y, -1 * z),
                (1 * x, -1 * y, -1 * z),
                (-1 * x, -1 * y, -1 * z),
                (-1 * x, 1 * y, -1 * z),
                (1 * x, 1 * y, -1 * z),
                (1 * x, -1 * y, -1 * z),
                (1 * x, -1 * y, 1 * z),
                (-1 * x, -1 * y, 1 * z),
                (-1 * x, -1 * y, -1 * z),
                (-1 * x, 1 * y, -1 * z),
                (-1 * x, 1 * y, 1 * z)
            ]
        )

        if name != '':
            cmds.rename(node, name)

    def get_sphere(self, name='', scale=[1, 1, 1]):
        coefficient = 2.0
        x = scale[0] * coefficient
        y = scale[1] * coefficient
        z = scale[2] * coefficient
        node = cmds.curve(
            degree=1,
            point=[
                (0.0 * x, 3.0 * y, 0.0 * z),
                (-2.0 * x, 2.0 * y, 0.0 * z),
                (-3.0 * x, 0.0 * y, 0.0 * z),
                (-2.0 * x, -2.0 * y, 0.0 * z),
                (0.0 * x, -3.0 * y, 0.0 * z),
                (2.0 * x, -2.0 * y, 0.0 * z),
                (3.0 * x, 0.0 * y, 0.0 * z),
                (2.0 * x, 2.0 * y, 0.0 * z),
                (0.0 * x, 3.0 * y, 0.0 * z),
                (0.0 * x, 2.0 * y, 2.0 * z),
                (0.0 * x, 0.0 * y, 3.0 * z),
                (0.0 * x, -2.0 * y, 2.0 * z),
                (0.0 * x, -3.0 * y, 0.0 * z),
                (0.0 * x, -2.0 * y, -2.0 * z),
                (0.0 * x, 0.0 * y, -3.0 * z),
                (-2.0 * x, 0.0 * y, -2.0 * z),
                (-3.0 * x, 0.0 * y, 0.0 * z),
                (-2.0 * x, 0.0 * y, 2.0 * z),
                (0.0 * x, 0.0 * y, 3.0 * z),
                (2.0 * x, 0.0 * y, 2.0 * z),
                (3.0 * x, 0.0 * y, 0.0 * z),
                (2.0 * x, 0.0 * y, -2.0 * z),
                (0.0 * x, 0.0 * y, -3.0 * z),
                (0.0 * x, 2.0 * y, -2.0 * z),
                (0.0 * x, 3.0 * y, 0.0 * z)
            ]
        )

        if name != '':
            cmds.rename(node, name)

    def get_circle(self, name='', scale=[1, 1, 1]):
        coefficient = 5.0
        x = scale[0] * coefficient
        y = scale[1] * coefficient
        z = scale[2] * coefficient
        node = cmds.curve(
            degree=1,
            point=[
                (0.0 * x, 0.0 * y, -1.0 * z),
                (-0.309017 * x, 0.0 * y, -0.951057 * z),
                (-0.587785 * x, 0.0 * y, -0.809017 * z),
                (-0.809017 * x, 0.0 * y, -0.587785 * z),
                (-0.951057 * x, 0.0 * y, -0.309017 * z),
                (-1.0 * x, 0.0 * y, 0.0 * z),
                (-0.951057 * x, 0.0 * y, 0.309017 * z),
                (-0.809017 * x, 0.0 * y, 0.587785 * z),
                (-0.587785 * x, 0.0 * y, 0.809017 * z),
                (-0.309017 * x, 0.0 * y, 0.951057 * z),
                (0.0 * x, 0.0 * y, 1.0 * z),
                (0.309017 * x, 0.0 * y, 0.951057 * z),
                (0.587785 * x, 0.0 * y, 0.809017 * z),
                (0.809017 * x, 0.0 * y, 0.587785 * z),
                (0.951057 * x, 0.0 * y, 0.309017 * z),
                (1.0 * x, 0.0 * y, 0.0 * z),
                (0.951057 * x, 0.0 * y, -0.309017 * z),
                (0.809018 * x, 0.0 * y, -0.587786 * z),
                (0.587786 * x, 0.0 * y, -0.809017 * z),
                (0.309017 * x, 0.0 * y, -0.951057 * z),
                (0.0 * x, 0.0 * y, -1.0 * z)
            ]
        )

        if name != '':
            cmds.rename(node, name)
