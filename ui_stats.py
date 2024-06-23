# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statsQgWcmC.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject, QSize)
from PySide6.QtWidgets import (QDialog, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(295, 207)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(True)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.maxLineEdit = QLineEdit(self.groupBox)
        self.maxLineEdit.setObjectName(u"maxLineEdit")
        self.maxLineEdit.setFrame(False)
        self.maxLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.maxLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.meanLineEdit = QLineEdit(self.groupBox)
        self.meanLineEdit.setObjectName(u"meanLineEdit")
        self.meanLineEdit.setFrame(False)
        self.meanLineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.meanLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))
        self.label_4.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.stdLineEdit = QLineEdit(self.groupBox)
        self.stdLineEdit.setObjectName(u"stdLineEdit")
        self.stdLineEdit.setFrame(False)
        self.stdLineEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.stdLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(self.groupBox)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_5.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Statistics", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Max:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Mean:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Standard Deviation:", None))
        self.closeButton.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

class statsUI(QDialog):
    def __init__(self, parent, dataDict):
        super().__init__(parent)

        # Set up window
        self.dataDict = dataDict

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Image Histogram Statistics")

        # Populate the data
        self.ui.maxLineEdit.setText(str(dataDict["max"]))
        self.ui.meanLineEdit.setText(str(dataDict["mean"]))
        self.ui.stdLineEdit.setText(str(dataDict["std"]))

        # Connect signals to slots
        self.ui.closeButton.clicked.connect(self.closeButtonClicked)

    def closeButtonClicked(self):
        self.close()

