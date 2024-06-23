# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ColorSettingsDialognIhKBd.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Signal, Slot, QSize, Qt)
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QDialog, QHBoxLayout, QLabel, QColorDialog,
                             QPushButton, QVBoxLayout)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        Dialog.resize(328, 88)
        Dialog.setModal(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.graphColorButton = QPushButton(Dialog)
        self.graphColorButton.setObjectName(u"graphColorButton")
        self.graphColorButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.graphColorButton)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.applyButton = QPushButton(Dialog)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.applyButton)

        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.cancelButton)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Color Settings", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Graph bar Color:", None))
        self.graphColorButton.setText("")
        self.applyButton.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi


class ColorSettingsDialog(QDialog):
    dataReady = Signal(str)

    def __init__(self, parent=None, oldColor="#FFFFFF"):
        super().__init__(parent)

        self.graphBarColor = oldColor

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Change text to current color
        self.ui.graphColorButton.setText(self.graphBarColor)

        # Connect signals and slots
        self.ui.graphColorButton.clicked.connect(self.graphBarColorButtonClicked)
        self.ui.applyButton.clicked.connect(self.applyButtonClicked)
        self.ui.cancelButton.clicked.connect(self.cancelButtonClicked)

    @Slot()
    def graphBarColorButtonClicked(self):
        new_color = QColorDialog.getColor(QColor(self.graphBarColor), self, "Edit Colors")
        self.graphBarColor = new_color.name()
        self.ui.graphColorButton.setText(new_color.name())

    @Slot()
    def applyButtonClicked(self):
        self.dataReady.emit(self.graphBarColor)
        self.close()

    @Slot()
    def cancelButtonClicked(self):
        self.close()
