# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(812, 473)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_4_position = QLineEdit(Dialog)
        self.lineEdit_4_position.setObjectName(u"lineEdit_4_position")

        self.gridLayout.addWidget(self.lineEdit_4_position, 3, 0, 1, 1)

        self.lineEdit_3_comp = QLineEdit(Dialog)
        self.lineEdit_3_comp.setObjectName(u"lineEdit_3_comp")

        self.gridLayout.addWidget(self.lineEdit_3_comp, 1, 2, 1, 1)

        self.label_6_address = QLabel(Dialog)
        self.label_6_address.setObjectName(u"label_6_address")

        self.gridLayout.addWidget(self.label_6_address, 2, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 8, 2, 1, 1)

        self.lineEdit_8_code2 = QLineEdit(Dialog)
        self.lineEdit_8_code2.setObjectName(u"lineEdit_8_code2")

        self.gridLayout.addWidget(self.lineEdit_8_code2, 5, 1, 1, 1)

        self.lineEdit_2_fio = QLineEdit(Dialog)
        self.lineEdit_2_fio.setObjectName(u"lineEdit_2_fio")

        self.gridLayout.addWidget(self.lineEdit_2_fio, 1, 1, 1, 1)

        self.label_7_code1 = QLabel(Dialog)
        self.label_7_code1.setObjectName(u"label_7_code1")

        self.gridLayout.addWidget(self.label_7_code1, 4, 0, 1, 1)

        self.label_4_position = QLabel(Dialog)
        self.label_4_position.setObjectName(u"label_4_position")

        self.gridLayout.addWidget(self.label_4_position, 2, 0, 1, 1)

        self.lineEdit_9_country = QLineEdit(Dialog)
        self.lineEdit_9_country.setObjectName(u"lineEdit_9_country")

        self.gridLayout.addWidget(self.lineEdit_9_country, 5, 2, 1, 1)

        self.label_5_city = QLabel(Dialog)
        self.label_5_city.setObjectName(u"label_5_city")

        self.gridLayout.addWidget(self.label_5_city, 2, 1, 1, 1)

        self.lineEdit_10_phone1 = QLineEdit(Dialog)
        self.lineEdit_10_phone1.setObjectName(u"lineEdit_10_phone1")

        self.gridLayout.addWidget(self.lineEdit_10_phone1, 7, 0, 1, 1)

        self.lineEdit_7_code1 = QLineEdit(Dialog)
        self.lineEdit_7_code1.setObjectName(u"lineEdit_7_code1")

        self.gridLayout.addWidget(self.lineEdit_7_code1, 5, 0, 1, 1)

        self.lineEdit_11_phone2 = QLineEdit(Dialog)
        self.lineEdit_11_phone2.setObjectName(u"lineEdit_11_phone2")

        self.gridLayout.addWidget(self.lineEdit_11_phone2, 7, 1, 1, 1)

        self.label_ID = QLabel(Dialog)
        self.label_ID.setObjectName(u"label_ID")

        self.gridLayout.addWidget(self.label_ID, 0, 0, 1, 1)

        self.label_8_code2 = QLabel(Dialog)
        self.label_8_code2.setObjectName(u"label_8_code2")

        self.gridLayout.addWidget(self.label_8_code2, 4, 1, 1, 1)

        self.label_9_country = QLabel(Dialog)
        self.label_9_country.setObjectName(u"label_9_country")

        self.gridLayout.addWidget(self.label_9_country, 4, 2, 1, 1)

        self.label_3_comp = QLabel(Dialog)
        self.label_3_comp.setObjectName(u"label_3_comp")

        self.gridLayout.addWidget(self.label_3_comp, 0, 2, 1, 1)

        self.lineEdit_ID = QLineEdit(Dialog)
        self.lineEdit_ID.setObjectName(u"lineEdit_ID")
        self.lineEdit_ID.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_ID, 1, 0, 1, 1)

        self.label_2_fio = QLabel(Dialog)
        self.label_2_fio.setObjectName(u"label_2_fio")

        self.gridLayout.addWidget(self.label_2_fio, 0, 1, 1, 1)

        self.lineEdit_6_address = QLineEdit(Dialog)
        self.lineEdit_6_address.setObjectName(u"lineEdit_6_address")

        self.gridLayout.addWidget(self.lineEdit_6_address, 3, 2, 1, 1)

        self.lineEdit_5_city = QLineEdit(Dialog)
        self.lineEdit_5_city.setObjectName(u"lineEdit_5_city")

        self.gridLayout.addWidget(self.lineEdit_5_city, 3, 1, 1, 1)

        self.label_10_phone1 = QLabel(Dialog)
        self.label_10_phone1.setObjectName(u"label_10_phone1")

        self.gridLayout.addWidget(self.label_10_phone1, 6, 0, 1, 1)

        self.label_11_phone2 = QLabel(Dialog)
        self.label_11_phone2.setObjectName(u"label_11_phone2")

        self.gridLayout.addWidget(self.label_11_phone2, 6, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_6_address.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.label_7_code1.setText(QCoreApplication.translate("Dialog", u"Code", None))
        self.label_4_position.setText(QCoreApplication.translate("Dialog", u"Position", None))
        self.label_5_city.setText(QCoreApplication.translate("Dialog", u"City", None))
        self.label_ID.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_8_code2.setText(QCoreApplication.translate("Dialog", u"Second Code", None))
        self.label_9_country.setText(QCoreApplication.translate("Dialog", u"Country", None))
        self.label_3_comp.setText(QCoreApplication.translate("Dialog", u"Company", None))
        self.lineEdit_ID.setPlaceholderText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_2_fio.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_10_phone1.setText(QCoreApplication.translate("Dialog", u"Phone", None))
        self.label_11_phone2.setText(QCoreApplication.translate("Dialog", u"Phone2", None))
    # retranslateUi

