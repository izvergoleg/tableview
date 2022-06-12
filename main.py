import sys
import xlsxwriter
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QToolBar, QFileDialog, QHeaderView)
from gui import Ui_MainWindow
from core import customModel, databaseOperations


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Accounting for everything!")
        self.setWindowIcon(QtGui.QIcon("icons/database.png"))
        self.showMaximized()
        databaseOperations.connect()
        self.user_data = databaseOperations.get_data()
        self.model = customModel.CustomTableModel(self.user_data)
        self.proxymodel = QtCore.QSortFilterProxyModel()
        self.proxymodel.setSourceModel(self.model)
        self.proxymodel.setFilterKeyColumn(-1)  # -1 this means that the filter is applied to all columns
        self.proxymodel.setFilterCaseSensitivity(
            QtCore.Qt.CaseInsensitive)
        self.tableView.setModel(self.proxymodel)

        # creating a custom table header #
        self.modelHeader = QtGui.QStandardItemModel()  # first, let's create a header model and put the titles of the headers into this model
        self.modelHeader.setHorizontalHeaderLabels(
            ['     Code Name   ', '           Company        ', 'Name and Surname', 'Position', 'Address', 'City',
             'Code', 'Second Code', 'Country', 'Phone #', 'Phone2 #', 'ID'])


        self.header = QHeaderView(QtCore.Qt.Horizontal)
        self.header.setModel(self.modelHeader)
        self.header.setSectionsClickable(True)
        self.header.setSectionsMovable(True)
        self.header.setStretchLastSection(True)
        self.tableView.setHorizontalHeader(self.header)
        self.tableView.setGridStyle(QtCore.Qt.DashLine)
        self.tableView.showGrid()
        self.tableView.horizontalHeader().setVisible(True)
        self.comboBox.addItems(["Column {0}".format(x) for x in range(self.proxymodel.columnCount())])

        self.searchbar.setStatusTip(u"searchbar")
        self.searchbar.setToolTip(u"Filter all columns")
        # the slot that is waiting for a fixed text in the search system
        # I can try using regexpressions PySide.QtGui.QSortFilterProxyModel.setFilterRegExp()
        self.searchbar.textChanged.connect(self.proxymodel.setFilterFixedString)
        self.font = QtGui.QFont("Segoe ui", 11)

        self.tableView.setFont(self.font)
        self.tableView.resizeColumnsToContents()  # set column width to fit contents (set font first!)
        self.tableView.setSortingEnabled(True)  # does not work without a proxy model

        self.tableView.sortByColumn(0,
                                    QtCore.Qt.AscendingOrder)
        self.tableView.verticalHeader().setDefaultSectionSize(20)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.context_menu)

        self.toolbar = QToolBar("My main toolbar")
        self.addToolBar(self.toolbar)

        self.button_action = QtGui.QAction("Export to Excel", self)
        self.button_action = QtGui.QAction(QtGui.QIcon("icons/report-excel.png"), "Export to Excel", self)
        self.button_action.setStatusTip("Export to Excel")
        self.button_action.triggered.connect(self.onMyToolBarButtonClickExport)
        self.toolbar.addAction(self.button_action)

        self.button_action_hide_row = QtGui.QAction("Hide Row", self)
        self.button_action_hide_row = QtGui.QAction(QtGui.QIcon("icons/table-delete-row.png"), "Hide Row", self)
        self.button_action_hide_row.setStatusTip("Hide Row")
        self.button_action_hide_row.triggered.connect(self.onMyToolBarButtonClickHideRow)
        self.toolbar.addAction(self.button_action_hide_row)

        self.button_action_hide_column = QtGui.QAction("Hide Column", self)
        self.button_action_hide_column = QtGui.QAction(QtGui.QIcon("icons/table-delete-column.png"), "Hide Column",
                                                       self)
        self.button_action_hide_column.setStatusTip("Hide Column")
        self.button_action_hide_column.triggered.connect(self.onMyToolBarButtonClickHideColumn)
        self.toolbar.addAction(self.button_action_hide_column)

        self.button_action_reload = QtGui.QAction("Unhide All", self)
        self.button_action_reload = QtGui.QAction(QtGui.QIcon("icons/arrow-circle-double.png"), "Unhide All",
                                                  self)
        self.button_action_reload.setStatusTip("Unhide All")
        self.button_action_reload.triggered.connect(self.onMyToolBarButtonClickShowAll)
        self.toolbar.addAction(self.button_action_reload)


    def context_menu(self):
        menu = QtWidgets.QMenu()

        if self.tableView.selectedIndexes():
            change_data = menu.addAction("Change record")
            change_data.setIcon(QtGui.QIcon("icons/document--pencil.png"))
            rows = sorted(set(index.row() for index in self.tableView.selectedIndexes()))
            for row in rows:
                # print('Row %d is selected' % row)
                newindex = self.tableView.model().index(row, 11)
            print('Index is :', newindex)
            self.dataId = self.tableView.model().data(newindex)
            print('Data from row:', self.dataId)
            print(set(index.row() for index in self.tableView.selectedIndexes()))
            change_data.triggered.connect(lambda: self.model.changeData(self.dataId))

            delete_data = menu.addAction("Delete record")
            delete_data.setIcon(QtGui.QIcon("icons/minus.png"))
            delete_data.triggered.connect(lambda: self.model.removeRows(self.tableView.currentIndex()))

        add_new = menu.addAction("Add new record")
        add_new.setIcon(QtGui.QIcon("icons/plus.png"))
        add_new.triggered.connect(lambda: self.model.newData())

        export_to_excel = menu.addAction("Export to Excel")
        export_to_excel.setIcon(QtGui.QIcon("icons/report-excel.png"))
        export_to_excel.triggered.connect(lambda: self.onMyToolBarButtonClick())

        cursor = QtGui.QCursor()
        menu.exec(cursor.pos())


    def onMyToolBarButtonClickExport(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save File', '',
                                               ".xlsx(*.xlsx)")  # I don't understand why a comma and an underscore are needed

        workbook = xlsxwriter.Workbook(fname)
        sheet = workbook.add_worksheet("sheet")

        model = self.tableView.model()  # our entire tableView table is passed to the model variable, which is then iterated through the cells in cycles and written to a file

        for c in range(model.columnCount()):
            if not self.tableView.isColumnHidden(c):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text)

        for r in range(model.rowCount()):
            if not self.tableView.isRowHidden(r):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text)

        for c in range(model.columnCount()):
            if not self.tableView.isColumnHidden(c):
                for r in range(model.rowCount()):
                    if not self.tableView.isRowHidden(r):
                        text = model.data(model.index(r, c))
                        sheet.write(r + 1, c + 1, text)
                    else:
                        pass
        workbook.close()
        self.label.setText("Exported to Excel, file:" + fname)


    def onMyToolBarButtonClickHideRow(self):
        self.label.setText("The rows are hidden")
        print('Hide row Clicked')
        print(sorted(set(index.row() for index in self.tableView.selectedIndexes())))
        rows = sorted(set(index.row() for index in self.tableView.selectedIndexes()))
        for rows_to_hide in rows:
            self.tableView.hideRow(rows_to_hide)


    def onMyToolBarButtonClickHideColumn(self):
        self.label.setText("The columns are hidden")
        print('Hide column Clicked')
        print(sorted(set(index.column() for index in self.tableView.selectedIndexes())))
        columns = sorted(set(index.column() for index in self.tableView.selectedIndexes()))
        for columns_to_hide in columns:
            self.tableView.hideColumn(columns_to_hide)


    def onMyToolBarButtonClickShowAll(self):
        self.label.setText("Show All")
        # TODO: #  It should be done normally. By searching (checking) all hidden
        for hided in range(1000):
            self.tableView.showColumn(hided)
            self.tableView.showRow(hided)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    # Open the style sheet file and read it
    with open('.\configs\style.qss', 'r') as f:
        style = f.read()
        # Set the current style sheet
    # app.setStyleSheet(style) # Experiments with the design style. You can uncomment this line and the style will change

    window = MainWindow()
    window.show()
    app.exec()

# TODO: # # creating a custom first column of the table - it sucks#
# self.modelHeaderV = QtGui.QStandardItemModel()
# numbers = [i for i in range(1, len(self.user_data) + 1)]
# str(numbers).replace(',', '.').replace('[', '').replace(']', '.').split()
# self.modelHeaderV.setVerticalHeaderLabels(str(numbers).replace(',', '.').replace('[', '').replace(']',
#                                                                                                   '.').split())  # i for i in range(0, len(self.user_data))
# self.headerV = QHeaderView(QtCore.Qt.Vertical)
# self.headerV.setModel(self.modelHeaderV)
# self.headerV.setSectionsClickable(True)
# self.headerV.setHighlightSections(True)
# self.headerV.setSectionsMovable(False)
#
# self.tableView.setVerticalHeader(self.headerV)
# self.tableView.verticalHeader().setVisible(False)