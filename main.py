from PyQt6 import QtWidgets, uic
import math

app = QtWidgets.QApplication([])
interface = uic.loadUi("src/ui/interface.ui")

display = "0"
operation = False
signs = ["+", "-", "*", "/"]
text_max_len, text_min_len = 20, 14

def check_text_size(interface):
    global text_max_len, text_min_len, display
    font = interface.display.font()
    text_length = len(display)
    default_size = 30
    reduction = 0.96
    limit_reach = 7 - text_max_len - text_length + 1

    if text_min_len < text_length <= text_max_len:
        new_size = int(default_size * (reduction ** limit_reach))
    else:
        new_size = default_size
    font.setPointSize(new_size)

    return interface.display.setFont(font)


def click_number(num, interface):
    global display, text_max_len
    try:
        if len(display) >= text_max_len or display[-1] == "%":
            return
        elif display[-1] == "0" and (len(display) == 1):
            display = display[:-1]
        display += str(num)
        interface.display.setText(display)
        check_text_size(interface)
    except:
        interface.display.setText("Error")
        display = "0"

def click_operation(op, interface):
    global operation, display
    if len(display) >= text_max_len or len(display) == 0:
        return
    if not operation or (display[-1] == "%" and op != "%"):
        display += str(op)
        interface.display.setText(display)
        operation = True

def click_result(interface):
    try:
        global operation, display
        if display[-1] != "%":
            result = str(eval(display))
            display = result
            interface.display.setText(result)
            operation = False
            check_text_size(interface)
    except:
        interface.display.setText("Error")

def click_clear(interface):
    global operation
    global display
    display = "0"
    interface.display.setText(display)
    operation = False
    check_text_size(interface)

def click_del(interface):
    global display, signs, operation
    if len(display) != 0:
        operation = False if display[-1] in signs else operation
        display = display[:-1]
        if len(display) <= 0:
            display = "0"
        interface.display.setText(display)
        check_text_size(interface)


def click_factorial(interface):
    global operation, display
    if operation:
        return

    num = int(display)
    for i in range(num-1, 0, -1):
        num *= i
    display = str(num)
    interface.display.setText(display)
    check_text_size(interface)

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
interface.bt_factorial.clicked.connect(lambda: click_factorial(interface))

interface.bt_equal.clicked.connect(lambda: click_result(interface))
interface.bt_clear.clicked.connect(lambda: click_clear(interface))
interface.bt_del.clicked.connect(lambda: click_del(interface))

interface.show()
app.exec()
