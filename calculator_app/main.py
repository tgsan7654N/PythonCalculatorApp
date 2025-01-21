import sys
from PyQt5.QtWidgets import QApplication
from calculator_app.calculator import Calculator

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()