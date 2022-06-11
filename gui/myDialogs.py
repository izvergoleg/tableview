from PySide6 import QtWidgets
from gui import Ui_Dialog
from lib import databaseOperations


class DialogWindowChange(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self, pers_id) -> None:
        super().__init__()
        self.setupUi(self)
        self.pers_id = pers_id
        self.person_data = databaseOperations.getRowData(self.pers_id) #создать словарь из данных нужной строки из БД
        print('В диалог идет это:', self.person_data[2])
        self.label_ID.setText('ID:' + ' ' + str(self.pers_id))
        self.lineEdit_2_fio.setText(str(self.person_data[2]))
        self.lineEdit_ID.setText(str(self.person_data[0]))
        self.lineEdit_3_comp.setText(str(self.person_data[1]))
        self.lineEdit_4_position.setText(str(self.person_data[3]))
        self.lineEdit_5_city.setText(str(self.person_data[5]))
        self.lineEdit_6_address.setText(str(self.person_data[4]))
        self.lineEdit_7_code1.setText(str(self.person_data[6]))
        self.lineEdit_8_code2.setText(str(self.person_data[7]))
        self.lineEdit_9_country.setText(str(self.person_data[8]))
        self.lineEdit_10_phone1.setText(str(self.person_data[9]))
        self.lineEdit_11_phone2.setText(str(self.person_data[10]))



    def accept(self) -> None:

        print("OK clicked")
        self.fio = self.lineEdit_2_fio.text()
        print(self.pers_id, self.fio)
        databaseOperations.update_row(self.pers_id, self.fio)
        self.done(True)


class DialogWindowNew(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = QtWidgets.QDialogButtonBox.Apply | QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)