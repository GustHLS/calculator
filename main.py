from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication([])
interface = uic.loadUi("src/ui/interface.ui")

display = ""
operation = False
signs = ["+", "-", "*", "/"]

def click_number(num, interface):
    global display
    display += str(num)
    interface.display.setText(display)

def click_operation(op, interface):
    global operation
    global display
    if not operation or (display[-1] == "%" and op != "%"):
        display += str(op)
        interface.display.setText(display)
        operation = True

def click_result(interface):
    try:
        global operation
        global display
        if display[-1] != "%":
            result = str(eval(display))
            display = result
            interface.display.setText(result)
            operation = False
    except:
        interface.display.setText("Error")

def click_clear(interface):
    global operation
    global display
    interface.display.setText("")
    display = ""
    operation = False

def click_del(interface):
    global display
    if len(display) != 0:
        global signs
        global operation
        operation = False if display[-1] in signs else operation
        display = display[:-1]
        interface.display.setText(display)

interface.bt0.clicked.connect(lambda: click_number(0, interface))
interface.bt1.clicked.connect(lambda: click_number(1, interface))
interface.bt2.clicked.connect(lambda: click_number(2, interface))
interface.bt3.clicked.connect(lambda: click_number(3, interface))
interface.bt4.clicked.connect(lambda: click_number(4, interface))
interface.bt5.clicked.connect(lambda: click_number(5, interface))
interface.bt6.clicked.connect(lambda: click_number(6, interface))
interface.bt7.clicked.connect(lambda: click_number(7, interface))
interface.bt8.clicked.connect(lambda: click_number(8, interface))
interface.bt9.clicked.connect(lambda: click_number(9, interface))

interface.bt_plus.clicked.connect(lambda: click_operation("+", interface))
interface.bt_minus.clicked.connect(lambda: click_operation("-", interface))
interface.bt_times.clicked.connect(lambda: click_operation("*", interface))
interface.bt_divided.clicked.connect(lambda: click_operation("/", interface))
interface.bt_negative.clicked.connect(lambda: click_operation("*-1", interface))
interface.bt_sqt.clicked.connect(lambda: click_operation("**0.5", interface))
interface.bt_power.clicked.connect(lambda: click_operation("**2", interface))
interface.bt_fraction.clicked.connect(lambda: click_operation("1/", interface))
interface.bt_percentage.clicked.connect(lambda: click_operation("%", interface))

interface.bt_equal.clicked.connect(lambda: click_result(interface))
interface.bt_clear.clicked.connect(lambda: click_clear(interface))
interface.bt_del.clicked.connect(lambda: click_del(interface))

interface.show()
app.exec()
