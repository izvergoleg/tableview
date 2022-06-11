from PySide6 import QtCore
from lib import databaseOperations
from gui import myDialogs

'''
Создаем свой класс CustomTableModel наследуемся от абстрактной модели.
обязательно наличие минимум трех функций: rowCount, columnCount, data
CustomTableModel класс используется представлением tableView
то есть tableView обращается к нашей кастомной модели CustomTableModel
'''

class CustomTableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self.user_data = data
        self.columns = self.user_data[0]

    def rowCount(self, *args, **kwargs):
        return len(self.user_data)

    def columnCount(self, *args, **kwargs):
        return len(self.columns)

    def data(self, index, role):

        if not index.isValid():
            return None

        elif role != QtCore.Qt.DisplayRole:
            return None

        return self.user_data[index.row()][index.column()]

    def removeRows(self, position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        row_id = position.row()
        document_id = self.user_data[row_id][11]
        databaseOperations.delete_pers(int(document_id))
        self.user_data.pop(row_id)
        self.endRemoveRows()
        return True


    def changeData(self, id):

        self.beginResetModel()
        print('data change')
        self.id = id
        dlg = myDialogs.DialogWindowChange(self.id)
        dlg.setWindowTitle("Changing data")
        dlg.exec()
        self.endResetModel()
        return(True)

    def setData(self, index, value, role=QtCore.Qt.EditRole):

        if index.isValid():
            selected_row = self.user_data[index.row()]
            selected_column = self.columns[index.column()]
            selected_row[selected_column] = value
            self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
            ok = databaseOperations.update_existing(selected_row['_id'], selected_row)
            if ok:
                return True
        return False

    def newData(self):

        print('data new')
        dlg = myDialogs.DialogWindowNew()
        dlg.setWindowTitle("New data")
        dlg.exec()
