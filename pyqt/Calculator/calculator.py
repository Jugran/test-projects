from PyQt5.QtWidgets import (QWidget, QGridLayout, QLineEdit,
                             QApplication, QPushButton)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.start()

        self.show()

    def start(self):
        layout = QGridLayout()

        buttons = ['AC', 'Del', '√', '/',
                   '7', '8', '9', '*',
                   '4', '5', '6', '-',
                   '1', '2', '3', '+',
                   '0', '.', '=']

        self.text_line = QLineEdit()
        layout.addWidget(self.text_line, 0, 0, 1, 4)

        row = 1
        col = 0

        for button in buttons:
            if col > 3:
                col = 0
                row += 1
            bt = QPushButton(button)
            bt.clicked.connect(self.on_button_click)

            if button == '0':
                layout.addWidget(bt, row, col, 1, 2)
                col += 1
            else:
                layout.addWidget(bt, row, col, 1, 1)

            col += 1

        self.setLayout(layout)

    def on_button_click(self):
        sender_name = self.sender().text()
        text = self.text_line.text()

        if sender_name == 'AC':
            text = ''
        elif sender_name == '=':
            text = str(eval(text))
        elif sender_name == 'Del':
            text = text[:-1]
        elif sender_name == '√':
            text = str(eval(text + '**0.5'))
        else:
            text = text + sender_name

        self.text_line.setText(text)


if __name__ == '__main__':
    app = QApplication([])

    window = Window()
    app.exec_()
