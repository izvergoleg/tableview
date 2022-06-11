# Наличие этого файла в текущей папке указывает Питону, что эта папка (gui) является не просто папкой, а пакетом gui
#Этот файл может быть пустым

from .main import Ui_MainWindow # для удобства к обращению из Qtable.py к Ui_MainWindow,  Ui_MainWindow в gui/main.py

from .dialog import Ui_Dialog