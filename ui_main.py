# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMZJRTA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 660)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_18 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout.addWidget(self.label_24)

        self.dataSearchEdit = QDateEdit(self.frame_4)
        self.dataSearchEdit.setObjectName(u"dataSearchEdit")

        self.horizontalLayout.addWidget(self.dataSearchEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.dataSearchButton = QPushButton(self.frame_4)
        self.dataSearchButton.setObjectName(u"dataSearchButton")

        self.horizontalLayout.addWidget(self.dataSearchButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.preDate = QPushButton(self.frame_5)
        self.preDate.setObjectName(u"preDate")

        self.horizontalLayout_17.addWidget(self.preDate)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)

        self.nextDate = QPushButton(self.frame_5)
        self.nextDate.setObjectName(u"nextDate")

        self.horizontalLayout_17.addWidget(self.nextDate)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.dataTable = QTableWidget(self.widget)
        if (self.dataTable.columnCount() < 6):
            self.dataTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.dataTable.setObjectName(u"dataTable")
        self.dataTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dataTable.setProperty("showDropIndicator", False)
        self.dataTable.setDragDropOverwriteMode(False)
        self.dataTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dataTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dataTable.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTable.horizontalHeader().setDefaultSectionSize(115)

        self.verticalLayout_6.addWidget(self.dataTable)


        self.horizontalLayout_18.addWidget(self.widget)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(400, 16777215))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.reportDate = QDateEdit(self.frame)
        self.reportDate.setObjectName(u"reportDate")

        self.horizontalLayout_2.addWidget(self.reportDate)


        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.reportProgram = QComboBox(self.frame)
        self.reportProgram.setObjectName(u"reportProgram")

        self.horizontalLayout_4.addWidget(self.reportProgram)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_13.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.reportStartTime = QTimeEdit(self.frame)
        self.reportStartTime.setObjectName(u"reportStartTime")

        self.horizontalLayout_3.addWidget(self.reportStartTime)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.reportEndTime = QTimeEdit(self.frame)
        self.reportEndTime.setObjectName(u"reportEndTime")

        self.horizontalLayout_3.addWidget(self.reportEndTime)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.disasterType = QLineEdit(self.groupBox)
        self.disasterType.setObjectName(u"disasterType")

        self.horizontalLayout_6.addWidget(self.disasterType)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.disasterDetail = QLineEdit(self.groupBox)
        self.disasterDetail.setObjectName(u"disasterDetail")

        self.horizontalLayout_5.addWidget(self.disasterDetail)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.disasterInputButton = QPushButton(self.groupBox)
        self.disasterInputButton.setObjectName(u"disasterInputButton")

        self.verticalLayout_3.addWidget(self.disasterInputButton)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.spotDetail = QComboBox(self.groupBox_2)
        self.spotDetail.setObjectName(u"spotDetail")

        self.horizontalLayout_9.addWidget(self.spotDetail)

        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.spotInputButton = QPushButton(self.groupBox_2)
        self.spotInputButton.setObjectName(u"spotInputButton")

        self.verticalLayout_4.addWidget(self.spotInputButton)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.programType = QLineEdit(self.groupBox_3)
        self.programType.setObjectName(u"programType")

        self.horizontalLayout_13.addWidget(self.programType)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_13.addWidget(self.label_19)

        self.programSpeaker = QLineEdit(self.groupBox_3)
        self.programSpeaker.setObjectName(u"programSpeaker")

        self.horizontalLayout_13.addWidget(self.programSpeaker)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_14.addWidget(self.label_20)

        self.programDetail = QLineEdit(self.groupBox_3)
        self.programDetail.setObjectName(u"programDetail")

        self.horizontalLayout_14.addWidget(self.programDetail)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.programInputButton = QPushButton(self.groupBox_3)
        self.programInputButton.setObjectName(u"programInputButton")

        self.verticalLayout_5.addWidget(self.programInputButton)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.modifyDisasterButton = QPushButton(self.tab)
        self.modifyDisasterButton.setObjectName(u"modifyDisasterButton")

        self.horizontalLayout_8.addWidget(self.modifyDisasterButton)

        self.delDisasterButton = QPushButton(self.tab)
        self.delDisasterButton.setObjectName(u"delDisasterButton")

        self.horizontalLayout_8.addWidget(self.delDisasterButton)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_6 = QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tagTable = QTableWidget(self.groupBox_6)
        if (self.tagTable.columnCount() < 3):
            self.tagTable.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tagTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tagTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tagTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.tagTable.setObjectName(u"tagTable")
        self.tagTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tagTable.setProperty("showDropIndicator", False)
        self.tagTable.setDragDropOverwriteMode(False)
        self.tagTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tagTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tagTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.tagTable.verticalHeader().setVisible(False)

        self.verticalLayout_11.addWidget(self.tagTable)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_25.addWidget(self.label_15)

        self.tagInput = QLineEdit(self.groupBox_6)
        self.tagInput.setObjectName(u"tagInput")

        self.horizontalLayout_25.addWidget(self.tagInput)


        self.verticalLayout_11.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_20.addWidget(self.label_25)

        self.tagStartDate = QDateEdit(self.groupBox_6)
        self.tagStartDate.setObjectName(u"tagStartDate")

        self.horizontalLayout_20.addWidget(self.tagStartDate)

        self.label_31 = QLabel(self.groupBox_6)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_31)

        self.tagEndDate = QDateEdit(self.groupBox_6)
        self.tagEndDate.setObjectName(u"tagEndDate")

        self.horizontalLayout_20.addWidget(self.tagEndDate)


        self.verticalLayout_11.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tagAddButton = QPushButton(self.groupBox_6)
        self.tagAddButton.setObjectName(u"tagAddButton")

        self.horizontalLayout_15.addWidget(self.tagAddButton)

        self.tagModifyButton = QPushButton(self.groupBox_6)
        self.tagModifyButton.setObjectName(u"tagModifyButton")

        self.horizontalLayout_15.addWidget(self.tagModifyButton)

        self.tagDelButton = QPushButton(self.groupBox_6)
        self.tagDelButton.setObjectName(u"tagDelButton")

        self.horizontalLayout_15.addWidget(self.tagDelButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)


        self.verticalLayout_7.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.tagList = QComboBox(self.groupBox_7)
        self.tagList.setObjectName(u"tagList")

        self.horizontalLayout_26.addWidget(self.tagList)

        self.findTaggedProgram = QPushButton(self.groupBox_7)
        self.findTaggedProgram.setObjectName(u"findTaggedProgram")

        self.horizontalLayout_26.addWidget(self.findTaggedProgram)


        self.verticalLayout_12.addLayout(self.horizontalLayout_26)

        self.programNameTable = QTableWidget(self.groupBox_7)
        if (self.programNameTable.columnCount() < 3):
            self.programNameTable.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.programNameTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.programNameTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.programNameTable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        self.programNameTable.setObjectName(u"programNameTable")
        self.programNameTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.programNameTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.programNameTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.programNameTable.horizontalHeader().setDefaultSectionSize(100)
        self.programNameTable.verticalHeader().setVisible(False)

        self.verticalLayout_12.addWidget(self.programNameTable)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.locationBox = QCheckBox(self.groupBox_7)
        self.locationBox.setObjectName(u"locationBox")

        self.horizontalLayout_7.addWidget(self.locationBox)

        self.weekendBox = QCheckBox(self.groupBox_7)
        self.weekendBox.setObjectName(u"weekendBox")

        self.horizontalLayout_7.addWidget(self.weekendBox)

        self.programNameInput = QLineEdit(self.groupBox_7)
        self.programNameInput.setObjectName(u"programNameInput")

        self.horizontalLayout_7.addWidget(self.programNameInput)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.programNameAddButton = QPushButton(self.groupBox_7)
        self.programNameAddButton.setObjectName(u"programNameAddButton")

        self.horizontalLayout_10.addWidget(self.programNameAddButton)

        self.programModifyButton = QPushButton(self.groupBox_7)
        self.programModifyButton.setObjectName(u"programModifyButton")

        self.horizontalLayout_10.addWidget(self.programModifyButton)

        self.programNameDelButton = QPushButton(self.groupBox_7)
        self.programNameDelButton.setObjectName(u"programNameDelButton")

        self.horizontalLayout_10.addWidget(self.programNameDelButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)


        self.verticalLayout_7.addWidget(self.groupBox_7)


        self.verticalLayout_9.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.spotTable = QTableWidget(self.groupBox_5)
        if (self.spotTable.columnCount() < 2):
            self.spotTable.setColumnCount(2)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.spotTable.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.spotTable.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        self.spotTable.setObjectName(u"spotTable")
        self.spotTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.spotTable.horizontalHeader().setDefaultSectionSize(160)
        self.spotTable.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.spotTable)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.spotInput = QLineEdit(self.groupBox_5)
        self.spotInput.setObjectName(u"spotInput")

        self.horizontalLayout_12.addWidget(self.spotInput)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_21.addWidget(self.label_9)

        self.spotTypeInput = QLineEdit(self.groupBox_5)
        self.spotTypeInput.setObjectName(u"spotTypeInput")

        self.horizontalLayout_21.addWidget(self.spotTypeInput)

        self.spotAddButton = QPushButton(self.groupBox_5)
        self.spotAddButton.setObjectName(u"spotAddButton")

        self.horizontalLayout_21.addWidget(self.spotAddButton)

        self.spotModifyButton = QPushButton(self.groupBox_5)
        self.spotModifyButton.setObjectName(u"spotModifyButton")

        self.horizontalLayout_21.addWidget(self.spotModifyButton)

        self.spotDelButton = QPushButton(self.groupBox_5)
        self.spotDelButton.setObjectName(u"spotDelButton")

        self.horizontalLayout_21.addWidget(self.spotDelButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)


        self.verticalLayout_9.addWidget(self.groupBox_5)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_10 = QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_23 = QLabel(self.tab_3)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_11.addWidget(self.label_23)

        self.createTagNameList = QComboBox(self.tab_3)
        self.createTagNameList.setObjectName(u"createTagNameList")

        self.horizontalLayout_11.addWidget(self.createTagNameList)

        self.createTagSearchButton = QPushButton(self.tab_3)
        self.createTagSearchButton.setObjectName(u"createTagSearchButton")

        self.horizontalLayout_11.addWidget(self.createTagSearchButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_24.addWidget(self.label_4)

        self.createProgramNameList = QComboBox(self.tab_3)
        self.createProgramNameList.setObjectName(u"createProgramNameList")

        self.horizontalLayout_24.addWidget(self.createProgramNameList)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_27 = QLabel(self.tab_3)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_22.addWidget(self.label_27)

        self.createStartDate = QDateEdit(self.tab_3)
        self.createStartDate.setObjectName(u"createStartDate")

        self.horizontalLayout_22.addWidget(self.createStartDate)

        self.label_28 = QLabel(self.tab_3)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_28)

        self.createEndDate = QDateEdit(self.tab_3)
        self.createEndDate.setObjectName(u"createEndDate")

        self.horizontalLayout_22.addWidget(self.createEndDate)


        self.verticalLayout_10.addLayout(self.horizontalLayout_22)

        self.frame_7 = QFrame(self.tab_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_16.addWidget(self.label_29)

        self.filePath = QLabel(self.frame_7)
        self.filePath.setObjectName(u"filePath")

        self.horizontalLayout_16.addWidget(self.filePath)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)

        self.filePathButton = QPushButton(self.frame_7)
        self.filePathButton.setObjectName(u"filePathButton")

        self.horizontalLayout_16.addWidget(self.filePathButton)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)

        self.createFileButton = QPushButton(self.frame_7)
        self.createFileButton.setObjectName(u"createFileButton")

        self.verticalLayout_14.addWidget(self.createFileButton)


        self.verticalLayout_10.addWidget(self.frame_7)

        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout_18.addWidget(self.tabWidget)

        self.horizontalLayout_18.setStretch(0, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc7ac\ub09c\ucde8\ud569\uc11c\ubc84", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\uc870\ud68c \uc77c\uc790", None))
        self.dataSearchButton.setText(QCoreApplication.translate("MainWindow", u"\uc870\ud68c", None))
        self.preDate.setText(QCoreApplication.translate("MainWindow", u"\uc774\uc804 \ub0a0\uc9dc", None))
        self.nextDate.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc74c \ub0a0\uc9dc", None))
        ___qtablewidgetitem = self.dataTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8", None));
        ___qtablewidgetitem1 = self.dataTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\ub09c\uc720\ud615", None));
        ___qtablewidgetitem2 = self.dataTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc138\ubd80\ub0b4\uc6a9", None));
        ___qtablewidgetitem3 = self.dataTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\ucd9c\uc5f0\uc790\uba85", None));
        ___qtablewidgetitem4 = self.dataTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\ubc29\uc1a1\uc2dc\uac04", None));
        ___qtablewidgetitem5 = self.dataTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04(\ubd84)", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ubc29\uc1a1\uc77c\uc790", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8\uba85", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ubc29\uc1a1\uc2dc\uac04", None))
        self.reportStartTime.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm:ss", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.reportEndTime.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm:ss", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\uc7ac\ub09c\uc218\uc2e0\ud074\ub77c\uc774\uc5b8\ud2b8", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\ub09c\uc720\ud615", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc138\ubd80\ub0b4\uc6a9", None))
        self.disasterInputButton.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"SPOT", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\uc138\ubd80\ub0b4\uc6a9", None))
        self.spotInputButton.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \uba58\ud2b8", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\ub09c\uc720\ud615", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\ucd9c\uc5f0\uc790\uba85", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\uc138\ubd80\ub0b4\uc6a9", None))
        self.programInputButton.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.modifyDisasterButton.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.delDisasterButton.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\ubc29\uc1a1 \uc2e4\uc801 \uc785\ub825", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \uad00\ub9ac", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\ud0dc\uadf8 \uad00\ub9ac", None))
        ___qtablewidgetitem6 = self.tagTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\ud0dc\uadf8\uba85", None));
        ___qtablewidgetitem7 = self.tagTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791\uc77c\uc790", None));
        ___qtablewidgetitem8 = self.tagTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc\uc77c\uc790", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\uac1c\ud3b8 \ud0dc\uadf8", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\uae30\uac04", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.tagAddButton.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.tagModifyButton.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.tagDelButton.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \uba85 \uad00\ub9ac", None))
        self.findTaggedProgram.setText(QCoreApplication.translate("MainWindow", u"\uc870\ud68c", None))
        ___qtablewidgetitem9 = self.programNameTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8\uba85", None));
        ___qtablewidgetitem10 = self.programNameTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ub9d0\uc720\ubb34", None));
        ___qtablewidgetitem11 = self.programNameTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uceec\uc720\ubb34", None));
        self.locationBox.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uceec", None))
        self.weekendBox.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ub9d0", None))
        self.programNameAddButton.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.programModifyButton.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.programNameDelButton.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"SPOT \uad00\ub9ac", None))
        ___qtablewidgetitem12 = self.spotTable.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"SPOT\uba85", None));
        ___qtablewidgetitem13 = self.spotTable.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\ub09c\uc720\ud615", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"SPOT\uba85", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\ub09c\uc720\ud615", None))
        self.spotAddButton.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.spotModifyButton.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.spotDelButton.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\uad00\ub9ac \uc815\ubcf4 \uc785\ub825", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\ud0dc\uadf8 \uc870\ud68c", None))
        self.createTagSearchButton.setText(QCoreApplication.translate("MainWindow", u"\uc870\ud68c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \uc120\ud0dd", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc0dd\uc131 \uae30\uac04", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc0dd\uc131 \uacbd\ub85c", None))
        self.filePath.setText(QCoreApplication.translate("MainWindow", u"C:\\", None))
        self.filePathButton.setText(QCoreApplication.translate("MainWindow", u"\ucc3e\uae30", None))
        self.createFileButton.setText(QCoreApplication.translate("MainWindow", u"\uc0dd\uc131", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc0dd\uc131", None))
    # retranslateUi

