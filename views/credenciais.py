# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../view.guide.ui/credenciais.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_credenciais(object):
    def setupUi(self, form_credenciais):
        form_credenciais.setObjectName("form_credenciais")
        form_credenciais.resize(400, 198)
        form_credenciais.setMaximumSize(QtCore.QSize(400, 198))
        self.link_adquirir = QtWidgets.QCommandLinkButton(form_credenciais)
        self.link_adquirir.setGeometry(QtCore.QRect(150, 20, 81, 31))
        self.link_adquirir.setObjectName("link_adquirir")
        self.widget = QtWidgets.QWidget(form_credenciais)
        self.widget.setGeometry(QtCore.QRect(11, 60, 381, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.field_jwt = QtWidgets.QLineEdit(self.widget)
        self.field_jwt.setObjectName("field_jwt")
        self.horizontalLayout.addWidget(self.field_jwt)
        self.widget1 = QtWidgets.QWidget(form_credenciais)
        self.widget1.setGeometry(QtCore.QRect(10, 110, 381, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.field_token = QtWidgets.QLineEdit(self.widget1)
        self.field_token.setObjectName("field_token")
        self.horizontalLayout_2.addWidget(self.field_token)
        self.widget2 = QtWidgets.QWidget(form_credenciais)
        self.widget2.setGeometry(QtCore.QRect(10, 160, 381, 27))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_fechar = QtWidgets.QPushButton(self.widget2)
        self.btn_fechar.setObjectName("btn_fechar")
        self.horizontalLayout_3.addWidget(self.btn_fechar)
        self.btn_salvar = QtWidgets.QPushButton(self.widget2)
        self.btn_salvar.setObjectName("btn_salvar")
        self.horizontalLayout_3.addWidget(self.btn_salvar)

        self.retranslateUi(form_credenciais)
        QtCore.QMetaObject.connectSlotsByName(form_credenciais)

    def retranslateUi(self, form_credenciais):
        _translate = QtCore.QCoreApplication.translate
        form_credenciais.setWindowTitle(_translate("form_credenciais", "Credenciais"))
        self.link_adquirir.setText(_translate("form_credenciais", "Adquiri"))
        self.label.setText(_translate("form_credenciais", "JWT"))
        self.label_2.setText(_translate("form_credenciais", "Token"))
        self.btn_fechar.setText(_translate("form_credenciais", "Fechar"))
        self.btn_salvar.setText(_translate("form_credenciais", "Salvar"))

