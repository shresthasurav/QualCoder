# Form implementation generated from reading ui file 'ui_dialog_charts.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogCharts(object):
    def setupUi(self, DialogCharts):
        DialogCharts.setObjectName("DialogCharts")
        DialogCharts.resize(1024, 600)
        self.gridLayout = QtWidgets.QGridLayout(DialogCharts)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_header = QtWidgets.QGroupBox(DialogCharts)
        self.groupBox_header.setMinimumSize(QtCore.QSize(0, 70))
        self.groupBox_header.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox_header.setTitle("")
        self.groupBox_header.setObjectName("groupBox_header")
        self.pushButton_export = QtWidgets.QPushButton(self.groupBox_header)
        self.pushButton_export.setGeometry(QtCore.QRect(840, 6, 28, 28))
        self.pushButton_export.setText("")
        self.pushButton_export.setObjectName("pushButton_export")
        self.label_chart_types = QtWidgets.QLabel(self.groupBox_header)
        self.label_chart_types.setGeometry(QtCore.QRect(10, 9, 101, 20))
        self.label_chart_types.setObjectName("label_chart_types")
        self.comboBox_chart_types = QtWidgets.QComboBox(self.groupBox_header)
        self.comboBox_chart_types.setGeometry(QtCore.QRect(117, 6, 271, 25))
        self.comboBox_chart_types.setObjectName("comboBox_chart_types")
        self.gridLayout.addWidget(self.groupBox_header, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(DialogCharts)
        self.graphicsView.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)

        self.retranslateUi(DialogCharts)
        QtCore.QMetaObject.connectSlotsByName(DialogCharts)

    def retranslateUi(self, DialogCharts):
        _translate = QtCore.QCoreApplication.translate
        DialogCharts.setWindowTitle(_translate("DialogCharts", "Charts"))
        self.pushButton_export.setToolTip(_translate("DialogCharts", "Export image"))
        self.label_chart_types.setText(_translate("DialogCharts", "Chart types:"))
