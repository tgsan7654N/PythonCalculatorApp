from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)
        self.create_ui()

    def create_ui(self):
        self.layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; padding: 5px;")
        self.layout.addWidget(self.display)

        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), 'C': (3, 2), '+': (3, 3),
            '=': (4, 0, 1, 4)
        }

        for text, pos in buttons.items():
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; padding: 10px;")
            button.clicked.connect(self.on_button_click)
            if len(pos) == 2:
                self.grid_layout.addWidget(button, pos[0], pos[1])
            else:
                self.grid_layout.addWidget(button, pos[0], pos[1], pos[2], pos[3])

        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)