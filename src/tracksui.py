# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tracks.ui'
#
# Created: Sun Sep 19 01:36:43 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtGui.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.home_tab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtGui.QStackedWidget(self.home_tab)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scrollArea = QtGui.QScrollArea(self.page_2)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 758, 553))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_6.addWidget(self.scrollArea)
        self.widget_2 = QtGui.QWidget(self.page_2)
        self.widget_2.setMinimumSize(QtCore.QSize(20, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6.addWidget(self.widget_2)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.tabWidget.addTab(self.home_tab, "")
        self.starred_tab = QtGui.QWidget()
        self.starred_tab.setEnabled(True)
        self.starred_tab.setObjectName("starred_tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.starred_tab)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.starred_mainpane = QtGui.QScrollArea(self.starred_tab)
        self.starred_mainpane.setFrameShape(QtGui.QFrame.NoFrame)
        self.starred_mainpane.setWidgetResizable(True)
        self.starred_mainpane.setObjectName("starred_mainpane")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.starred_mainpane)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 768, 553))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.starred_mainpane_layout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.starred_mainpane_layout.setObjectName("starred_mainpane_layout")
        self.starred_mainpane.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.starred_mainpane)
        self.starred_sidepane = QtGui.QWidget(self.starred_tab)
        self.starred_sidepane.setMinimumSize(QtCore.QSize(10, 0))
        self.starred_sidepane.setObjectName("starred_sidepane")
        self.starred_sidepane_layout = QtGui.QVBoxLayout(self.starred_sidepane)
        self.starred_sidepane_layout.setSpacing(0)
        self.starred_sidepane_layout.setMargin(0)
        self.starred_sidepane_layout.setObjectName("starred_sidepane_layout")
        self.horizontalLayout_2.addWidget(self.starred_sidepane)
        self.tabWidget.addTab(self.starred_tab, "")
        self.projects_tab = QtGui.QWidget()
        self.projects_tab.setObjectName("projects_tab")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.projects_tab)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget_2 = QtGui.QStackedWidget(self.projects_tab)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.projects_page = QtGui.QWidget()
        self.projects_page.setObjectName("projects_page")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.projects_page)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.scrollArea_5 = QtGui.QScrollArea(self.projects_page)
        self.scrollArea_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_7 = QtGui.QWidget(self.scrollArea_5)
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 758, 553))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.projects_mainpane_layout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.projects_mainpane_layout.setObjectName("projects_mainpane_layout")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_9.addWidget(self.scrollArea_5)
        self.widget_5 = QtGui.QWidget(self.projects_page)
        self.widget_5.setMinimumSize(QtCore.QSize(20, 0))
        self.widget_5.setObjectName("widget_5")
        self.projects_sidepane_layout = QtGui.QVBoxLayout(self.widget_5)
        self.projects_sidepane_layout.setSpacing(0)
        self.projects_sidepane_layout.setMargin(0)
        self.projects_sidepane_layout.setObjectName("projects_sidepane_layout")
        self.horizontalLayout_9.addWidget(self.widget_5)
        self.stackedWidget_2.addWidget(self.projects_page)
        self.projectview_page = QtGui.QWidget()
        self.projectview_page.setObjectName("projectview_page")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.projectview_page)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.projectBackButton = QtGui.QPushButton(self.projectview_page)
        self.projectBackButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.projectBackButton.setObjectName("projectBackButton")
        self.horizontalLayout_8.addWidget(self.projectBackButton)
        self.projectLabel = QtGui.QLabel(self.projectview_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectLabel.sizePolicy().hasHeightForWidth())
        self.projectLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        self.projectLabel.setFont(font)
        self.projectLabel.setObjectName("projectLabel")
        self.horizontalLayout_8.addWidget(self.projectLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.projectDescription = QtGui.QLabel(self.projectview_page)
        self.projectDescription.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.projectDescription.setWordWrap(True)
        self.projectDescription.setObjectName("projectDescription")
        self.verticalLayout.addWidget(self.projectDescription)
        self.scrollArea_2 = QtGui.QScrollArea(self.projectview_page)
        self.scrollArea_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtGui.QWidget(self.scrollArea_2)
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.projectview_verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.projectview_verticalLayout.setMargin(0)
        self.projectview_verticalLayout.setObjectName("projectview_verticalLayout")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        self.widget = QtGui.QWidget(self.projectview_page)
        self.widget.setMinimumSize(QtCore.QSize(20, 0))
        self.widget.setObjectName("widget")
        self.projectDetails_sidepane_layout = QtGui.QVBoxLayout(self.widget)
        self.projectDetails_sidepane_layout.setSpacing(0)
        self.projectDetails_sidepane_layout.setMargin(0)
        self.projectDetails_sidepane_layout.setObjectName("projectDetails_sidepane_layout")
        self.horizontalLayout_12.addWidget(self.widget)
        self.stackedWidget_2.addWidget(self.projectview_page)
        self.horizontalLayout_4.addWidget(self.stackedWidget_2)
        self.tabWidget.addTab(self.projects_tab, "")
        self.contexts_tab = QtGui.QWidget()
        self.contexts_tab.setObjectName("contexts_tab")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.contexts_tab)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.stackedWidget_3 = QtGui.QStackedWidget(self.contexts_tab)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.contexts_page = QtGui.QWidget()
        self.contexts_page.setObjectName("contexts_page")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.contexts_page)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.scrollArea_6 = QtGui.QScrollArea(self.contexts_page)
        self.scrollArea_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_8 = QtGui.QWidget(self.scrollArea_6)
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 758, 553))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.contexts_mainpane_layout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.contexts_mainpane_layout.setObjectName("contexts_mainpane_layout")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_10.addWidget(self.scrollArea_6)
        self.widget_6 = QtGui.QWidget(self.contexts_page)
        self.widget_6.setMinimumSize(QtCore.QSize(20, 0))
        self.widget_6.setObjectName("widget_6")
        self.contexts_sidepane_layout = QtGui.QVBoxLayout(self.widget_6)
        self.contexts_sidepane_layout.setSpacing(0)
        self.contexts_sidepane_layout.setMargin(0)
        self.contexts_sidepane_layout.setObjectName("contexts_sidepane_layout")
        self.horizontalLayout_10.addWidget(self.widget_6)
        self.stackedWidget_3.addWidget(self.contexts_page)
        self.contextview_page = QtGui.QWidget()
        self.contextview_page.setObjectName("contextview_page")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.contextview_page)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setMargin(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.contextBackButton = QtGui.QPushButton(self.contextview_page)
        self.contextBackButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.contextBackButton.setObjectName("contextBackButton")
        self.horizontalLayout_11.addWidget(self.contextBackButton)
        self.contextLabel = QtGui.QLabel(self.contextview_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contextLabel.sizePolicy().hasHeightForWidth())
        self.contextLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        self.contextLabel.setFont(font)
        self.contextLabel.setObjectName("contextLabel")
        self.horizontalLayout_11.addWidget(self.contextLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.scrollArea_7 = QtGui.QScrollArea(self.contextview_page)
        self.scrollArea_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_9 = QtGui.QWidget(self.scrollArea_7)
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.contextview_verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.contextview_verticalLayout.setMargin(0)
        self.contextview_verticalLayout.setObjectName("contextview_verticalLayout")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayout_2.addWidget(self.scrollArea_7)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        self.widget_7 = QtGui.QWidget(self.contextview_page)
        self.widget_7.setMinimumSize(QtCore.QSize(20, 0))
        self.widget_7.setObjectName("widget_7")
        self.contextDetails_sidepane_layout = QtGui.QVBoxLayout(self.widget_7)
        self.contextDetails_sidepane_layout.setSpacing(0)
        self.contextDetails_sidepane_layout.setMargin(0)
        self.contextDetails_sidepane_layout.setObjectName("contextDetails_sidepane_layout")
        self.horizontalLayout_13.addWidget(self.widget_7)
        self.stackedWidget_3.addWidget(self.contextview_page)
        self.verticalLayout_12.addWidget(self.stackedWidget_3)
        self.tabWidget.addTab(self.contexts_tab, "")
        self.calendar_tab = QtGui.QWidget()
        self.calendar_tab.setObjectName("calendar_tab")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.calendar_tab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.scrollArea_4 = QtGui.QScrollArea(self.calendar_tab)
        self.scrollArea_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_6 = QtGui.QWidget(self.scrollArea_4)
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 654, 535))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_7.addWidget(self.scrollArea_4)
        self.widget_4 = QtGui.QWidget(self.calendar_tab)
        self.widget_4.setMinimumSize(QtCore.QSize(100, 0))
        self.widget_4.setObjectName("widget_4")
        self.calendar_sidepane_layout = QtGui.QVBoxLayout(self.widget_4)
        self.calendar_sidepane_layout.setObjectName("calendar_sidepane_layout")
        self.horizontalLayout_7.addWidget(self.widget_4)
        self.tabWidget.addTab(self.calendar_tab, "")
        self.tickler_tab = QtGui.QWidget()
        self.tickler_tab.setObjectName("tickler_tab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tickler_tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tickler_mainpane = QtGui.QScrollArea(self.tickler_tab)
        self.tickler_mainpane.setFrameShape(QtGui.QFrame.NoFrame)
        self.tickler_mainpane.setWidgetResizable(True)
        self.tickler_mainpane.setObjectName("tickler_mainpane")
        self.scrollAreaWidgetContents_3 = QtGui.QWidget(self.tickler_mainpane)
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 654, 535))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.tickler_mainpane_layout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.tickler_mainpane_layout.setObjectName("tickler_mainpane_layout")
        self.tickler_mainpane.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.addWidget(self.tickler_mainpane)
        self.tickler_sidepane = QtGui.QWidget(self.tickler_tab)
        self.tickler_sidepane.setMinimumSize(QtCore.QSize(100, 0))
        self.tickler_sidepane.setObjectName("tickler_sidepane")
        self.tickler_sidepane_layout = QtGui.QVBoxLayout(self.tickler_sidepane)
        self.tickler_sidepane_layout.setObjectName("tickler_sidepane_layout")
        self.horizontalLayout_3.addWidget(self.tickler_sidepane)
        self.tabWidget.addTab(self.tickler_tab, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_6)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scrollArea_3 = QtGui.QScrollArea(self.tab_6)
        self.scrollArea_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_5 = QtGui.QWidget(self.scrollArea_3)
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 778, 553))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.done_mainpane_layout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.done_mainpane_layout.setObjectName("done_mainpane_layout")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_5.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.tab_6, "")
        self.statistics_tab = QtGui.QWidget()
        self.statistics_tab.setObjectName("statistics_tab")
        self.tabWidget.addTab(self.statistics_tab, "")
        self.settings_tab = QtGui.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.settings_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label = QtGui.QLabel(self.settings_tab)
        self.label.setObjectName("label")
        self.horizontalLayout_14.addWidget(self.label)
        self.settingsUserSelectBox = QtGui.QComboBox(self.settings_tab)
        self.settingsUserSelectBox.setObjectName("settingsUserSelectBox")
        self.horizontalLayout_14.addWidget(self.settingsUserSelectBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        spacerItem1 = QtGui.QSpacerItem(20, 500, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.tabWidget.addTab(self.settings_tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.starred_tab), QtGui.QApplication.translate("MainWindow", "Starred", None, QtGui.QApplication.UnicodeUTF8))
        self.projectBackButton.setText(QtGui.QApplication.translate("MainWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.projectLabel.setText(QtGui.QApplication.translate("MainWindow", "Specific Project View Page", None, QtGui.QApplication.UnicodeUTF8))
        self.projectDescription.setText(QtGui.QApplication.translate("MainWindow", "Sample project description", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.projects_tab), QtGui.QApplication.translate("MainWindow", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.contextBackButton.setText(QtGui.QApplication.translate("MainWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.contextLabel.setText(QtGui.QApplication.translate("MainWindow", "Specific Context View Page", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contexts_tab), QtGui.QApplication.translate("MainWindow", "Contexts", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calendar_tab), QtGui.QApplication.translate("MainWindow", "Calendar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tickler_tab), QtGui.QApplication.translate("MainWindow", "Tickler", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("MainWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statistics_tab), QtGui.QApplication.translate("MainWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Active User", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))

