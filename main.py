from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication([])
interface = uic.loadUi("src/ui/interface.ui")

interface.show()

app.exec()
