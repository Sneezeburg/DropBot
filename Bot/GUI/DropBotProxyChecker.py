# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proxy checker.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProxyChecker(object):
    def setupUi(self, ProxyChecker):
        ProxyChecker.setObjectName("ProxyChecker")
        ProxyChecker.resize(844, 519)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProxyChecker)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ProxyChecker)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(ProxyChecker)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 824, 422))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.ipLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.ipLabel.setFont(font)
        self.ipLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ipLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ipLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ipLabel.setObjectName("ipLabel")
        self.gridLayout.addWidget(self.ipLabel, 0, 2, 1, 1)
        self.idLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idLabel.sizePolicy().hasHeightForWidth())
        self.idLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.idLabel.setFont(font)
        self.idLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.idLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.idLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout.addWidget(self.idLabel, 0, 0, 1, 1)
        self.delayList = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.delayList.setFont(font)
        self.delayList.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.delayList.setStyleSheet("border: 0px;")
        self.delayList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.delayList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.delayList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.delayList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.delayList.setProperty("showDropIndicator", False)
        self.delayList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.delayList.setAlternatingRowColors(True)
        self.delayList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.delayList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.delayList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.delayList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.delayList.setMovement(QtWidgets.QListView.Static)
        self.delayList.setFlow(QtWidgets.QListView.TopToBottom)
        self.delayList.setProperty("isWrapping", False)
        self.delayList.setResizeMode(QtWidgets.QListView.Adjust)
        self.delayList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.delayList.setViewMode(QtWidgets.QListView.ListMode)
        self.delayList.setUniformItemSizes(False)
        self.delayList.setWordWrap(False)
        self.delayList.setSelectionRectVisible(True)
        self.delayList.setItemAlignment(QtCore.Qt.AlignCenter)
        self.delayList.setObjectName("delayList")
        self.gridLayout.addWidget(self.delayList, 2, 8, 1, 1)
        self.locationList = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.locationList.setFont(font)
        self.locationList.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.locationList.setStyleSheet("border: 0px;")
        self.locationList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.locationList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.locationList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.locationList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.locationList.setProperty("showDropIndicator", False)
        self.locationList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.locationList.setAlternatingRowColors(True)
        self.locationList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.locationList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.locationList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.locationList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.locationList.setMovement(QtWidgets.QListView.Static)
        self.locationList.setFlow(QtWidgets.QListView.TopToBottom)
        self.locationList.setProperty("isWrapping", False)
        self.locationList.setResizeMode(QtWidgets.QListView.Adjust)
        self.locationList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.locationList.setViewMode(QtWidgets.QListView.ListMode)
        self.locationList.setUniformItemSizes(False)
        self.locationList.setWordWrap(False)
        self.locationList.setSelectionRectVisible(True)
        self.locationList.setItemAlignment(QtCore.Qt.AlignCenter)
        self.locationList.setObjectName("locationList")
        self.gridLayout.addWidget(self.locationList, 2, 4, 1, 1)
        self.credsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.credsLabel.setFont(font)
        self.credsLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.credsLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.credsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.credsLabel.setObjectName("credsLabel")
        self.gridLayout.addWidget(self.credsLabel, 0, 3, 1, 1)
        self.delayLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.delayLabel.setFont(font)
        self.delayLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.delayLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.delayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.delayLabel.setObjectName("delayLabel")
        self.gridLayout.addWidget(self.delayLabel, 0, 8, 1, 1)
        self.locationLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.locationLabel.setFont(font)
        self.locationLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.locationLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.locationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.locationLabel.setObjectName("locationLabel")
        self.gridLayout.addWidget(self.locationLabel, 0, 4, 1, 1)
        self.idList = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idList.sizePolicy().hasHeightForWidth())
        self.idList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.idList.setFont(font)
        self.idList.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.idList.setStyleSheet("border: 0px;")
        self.idList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.idList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.idList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.idList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.idList.setProperty("showDropIndicator", False)
        self.idList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.idList.setAlternatingRowColors(True)
        self.idList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.idList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.idList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.idList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.idList.setMovement(QtWidgets.QListView.Static)
        self.idList.setFlow(QtWidgets.QListView.TopToBottom)
        self.idList.setProperty("isWrapping", False)
        self.idList.setResizeMode(QtWidgets.QListView.Adjust)
        self.idList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.idList.setViewMode(QtWidgets.QListView.ListMode)
        self.idList.setUniformItemSizes(False)
        self.idList.setWordWrap(False)
        self.idList.setSelectionRectVisible(True)
        self.idList.setItemAlignment(QtCore.Qt.AlignCenter)
        self.idList.setObjectName("idList")
        self.gridLayout.addWidget(self.idList, 2, 0, 1, 1)
        self.credsList = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.credsList.setFont(font)
        self.credsList.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.credsList.setStyleSheet("border: 0px;")
        self.credsList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.credsList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.credsList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.credsList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.credsList.setProperty("showDropIndicator", False)
        self.credsList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.credsList.setAlternatingRowColors(True)
        self.credsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.credsList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.credsList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.credsList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.credsList.setMovement(QtWidgets.QListView.Static)
        self.credsList.setFlow(QtWidgets.QListView.TopToBottom)
        self.credsList.setProperty("isWrapping", False)
        self.credsList.setResizeMode(QtWidgets.QListView.Adjust)
        self.credsList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.credsList.setViewMode(QtWidgets.QListView.ListMode)
        self.credsList.setUniformItemSizes(False)
        self.credsList.setWordWrap(False)
        self.credsList.setSelectionRectVisible(True)
        self.credsList.setItemAlignment(QtCore.Qt.AlignCenter)
        self.credsList.setObjectName("credsList")
        self.gridLayout.addWidget(self.credsList, 2, 3, 1, 1)
        self.typeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.typeLabel.setFont(font)
        self.typeLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.typeLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.typeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.typeLabel.setObjectName("typeLabel")
        self.gridLayout.addWidget(self.typeLabel, 0, 6, 1, 1)
        self.ipList = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ipList.setFont(font)
        self.ipList.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ipList.setStyleSheet("border: 0px;")
        self.ipList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ipList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ipList.setProperty("showDropIndicator", False)
        self.ipList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.ipList.setAlternatingRowColors(True)
        self.ipList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ipList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ipList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.ipList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ipList.setMovement(QtWidgets.QListView.Static)
        self.ipList.setFlow(QtWidgets.QListView.TopToBottom)
        self.ipList.setProperty("isWrapping", False)
        self.ipList.setResizeMode(QtWidgets.QListView.Adjust)
        self.ipList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.ipList.setViewMode(QtWidgets.QListView.ListMode)
        self.ipList.setUniformItemSizes(False)
        self.ipList.setWordWrap(False)
        self.ipList.setSelectionRectVisible(True)
        self.ipList.setItemAlignment(QtCore.Qt.AlignCenter)
        self.ipList.setObjectName("ipList")
        self.gridLayout.addWidget(self.ipList, 2, 2, 1, 1)
        self.typeList = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.typeList.setFont(font)
        self.typeList.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.typeList.setStyleSheet("border: 0px;")
        self.typeList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.typeList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.typeList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.typeList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.typeList.setProperty("showDropIndicator", False)
        self.typeList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.typeList.setAlternatingRowColors(True)
        self.typeList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.typeList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.typeList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.typeList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.typeList.setMovement(QtWidgets.QListView.Static)
        self.typeList.setFlow(QtWidgets.QListView.TopToBottom)
        self.typeList.setProperty("isWrapping", False)
        self.typeList.setResizeMode(QtWidgets.QListView.Adjust)
        self.typeList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.typeList.setViewMode(QtWidgets.QListView.ListMode)
        self.typeList.setUniformItemSizes(False)
        self.typeList.setWordWrap(False)
        self.typeList.setSelectionRectVisible(True)
        self.typeList.setItemAlignment(QtCore.Qt.AlignCenter)
        self.typeList.setObjectName("typeList")
        self.gridLayout.addWidget(self.typeList, 2, 6, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(ProxyChecker)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(ProxyChecker)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.cancel = QtWidgets.QPushButton(ProxyChecker)
        self.cancel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ProxyChecker)
        QtCore.QMetaObject.connectSlotsByName(ProxyChecker)

    def retranslateUi(self, ProxyChecker):
        _translate = QtCore.QCoreApplication.translate
        ProxyChecker.setWindowTitle(_translate("ProxyChecker", "Proxy Test Tool"))
        self.label.setText(_translate("ProxyChecker", "Proxy tester"))
        self.ipLabel.setText(_translate("ProxyChecker", "IP adress & Port"))
        self.idLabel.setText(_translate("ProxyChecker", "ID"))
        self.delayList.setSortingEnabled(False)
        self.locationList.setSortingEnabled(False)
        self.credsLabel.setText(_translate("ProxyChecker", "Username & Password"))
        self.delayLabel.setText(_translate("ProxyChecker", "Delay "))
        self.locationLabel.setText(_translate("ProxyChecker", "Country, City "))
        self.idList.setSortingEnabled(False)
        self.credsList.setSortingEnabled(False)
        self.typeLabel.setText(_translate("ProxyChecker", "Type "))
        self.ipList.setSortingEnabled(False)
        self.typeList.setSortingEnabled(False)
        self.pushButton.setText(_translate("ProxyChecker", "   Import proxy from profiile   "))
        self.cancel.setText(_translate("ProxyChecker", "Cancel"))
        self.listwidgets = [self.idList, self.ipList,self.credsList,self.locationList,self.typeList, self.delayList]
        for item in self.listwidgets:
            item.verticalScrollBar().valueChanged.connect(self.__chnge_position)

    def __chnge_position(self,index):
        #slot to change the scroll bar  position of all table
        self.idList.verticalScrollBar().setValue(index)
        self.ipList.verticalScrollBar().setValue(index)
        self.credsList.verticalScrollBar().setValue(index)
        self.locationList.verticalScrollBar().setValue(index)
        self.typeList.verticalScrollBar().setValue(index)
        self.delayList.verticalScrollBar().setValue(index)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    import qdarkstyle
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ProxyChecker = QtWidgets.QDialog()
    ui = Ui_ProxyChecker()
    ui.setupUi(ProxyChecker)
    ProxyChecker.show()
    sys.exit(app.exec_())
