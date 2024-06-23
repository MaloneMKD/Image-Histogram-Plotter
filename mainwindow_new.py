# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainguivdZmyc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QSlider, QSpacerItem, QStatusBar,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbox_layout = QHBoxLayout()
        self.toolbox_layout.setObjectName(u"toolbox_layout")

        self.verticalLayout.addLayout(self.toolbox_layout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.importTypeComboBox = QComboBox(self.centralwidget)
        self.importTypeComboBox.setObjectName(u"importTypeComboBox")
        self.importTypeComboBox.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_4.addWidget(self.importTypeComboBox)

        self.importCSVButton = QPushButton(self.centralwidget)
        self.importCSVButton.setObjectName(u"importCSVButton")
        self.importCSVButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.importCSVButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.scrollSlider = QSlider(self.centralwidget)
        self.scrollSlider.setObjectName(u"scrollSlider")
        self.scrollSlider.setMinimumSize(QSize(200, 30))
        self.scrollSlider.setMaximum(511)
        self.scrollSlider.setSingleStep(1)
        self.scrollSlider.setOrientation(Qt.Orientation.Horizontal)
        self.scrollSlider.setInvertedAppearance(False)
        self.scrollSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)

        self.horizontalLayout.addWidget(self.scrollSlider)

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.gainSlider = QSlider(self.centralwidget)
        self.gainSlider.setObjectName(u"gainSlider")
        self.gainSlider.setMinimumSize(QSize(200, 30))
        self.gainSlider.setMaximum(512)
        self.gainSlider.setOrientation(Qt.Orientation.Horizontal)
        self.gainSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)

        self.horizontalLayout_2.addWidget(self.gainSlider)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.clearButton)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Color Settings", None))
        self.importCSVButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Scroll:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gain:", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
