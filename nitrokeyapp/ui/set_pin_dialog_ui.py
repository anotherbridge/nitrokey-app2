# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_pin_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePinDialog(object):
    def setupUi(self, ChangePinDialog):
        ChangePinDialog.setObjectName("ChangePinDialog")
        ChangePinDialog.setWindowModality(QtCore.Qt.WindowModal)
        ChangePinDialog.resize(388, 211)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChangePinDialog.sizePolicy().hasHeightForWidth())
        ChangePinDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ChangePinDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_new_pin_set = QtWidgets.QLineEdit(ChangePinDialog)
        self.lineEdit_new_pin_set.setObjectName("lineEdit_new_pin_set")
        self.gridLayout.addWidget(self.lineEdit_new_pin_set, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(ChangePinDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_confirm_new_pin_set = QtWidgets.QLineEdit(ChangePinDialog)
        self.lineEdit_confirm_new_pin_set.setObjectName("lineEdit_confirm_new_pin_set")
        self.gridLayout.addWidget(self.lineEdit_confirm_new_pin_set, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(ChangePinDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ChangePinDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ChangePinDialog)
        self.buttonBox.accepted.connect(ChangePinDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ChangePinDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ChangePinDialog)

    def retranslateUi(self, ChangePinDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangePinDialog.setWindowTitle(_translate("ChangePinDialog", "Dialog"))
        self.label_3.setText(_translate("ChangePinDialog", "New PIN:"))
        self.label.setText(_translate("ChangePinDialog", "Confirm New PIN:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePinDialog = QtWidgets.QDialog()
    ui = Ui_ChangePinDialog()
    ui.setupUi(ChangePinDialog)
    ChangePinDialog.show()
    sys.exit(app.exec_())
