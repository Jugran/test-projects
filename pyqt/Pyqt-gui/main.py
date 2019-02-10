#######################################################
#	Demo PyQt5 GUI created by Samarth Jugran
#	
#
#	requirements- 
#				PyQt5 - version 5.9.2
#				matplotlib - version 3.0.2
#
#
#######################################################



#!/usr/bin/env python3
import random

import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QHBoxLayout,
                             QTableWidget, QVBoxLayout, QLabel, QComboBox,
                             QLineEdit, QGridLayout, QSlider, QDial, QPushButton,
                             QRadioButton)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout()

        self.setGeometry(400, 400, 800, 600)

        self.setup_gui()
        self.setWindowTitle("Demo PyQt GUI")
        self.show()

    def setup_gui(self):
        self.setup_topbar()
        self.setup_tabs()

        self.setLayout(self.mainLayout)

    def setup_topbar(self):
        top_bar = QHBoxLayout()

        drop_down_label = QLabel('Drop Down')

        drop_down = QComboBox()
        drop_down_list = ['option ' + str(i) for i in range(10)]
        drop_down.addItems(drop_down_list)

        top_bar.addWidget(drop_down_label)
        top_bar.addWidget(drop_down)
        top_bar.addStretch()

        self.mainLayout.addLayout(top_bar)

    def setup_tabs(self):
        tab_widget = QTabWidget()

        tab1 = QWidget()
        table = QTableWidget(10, 10)
        tab1_box = QHBoxLayout()
        tab1_box.addWidget(table)
        tab1.setLayout(tab1_box)

        tab2 = QWidget()
        tab2_box = QVBoxLayout()

        tab2_grid = QGridLayout()
        tab2_grid.setSpacing(10)

        line_label = QLabel('Text Field')
        line_edit = QLineEdit()

        slider_label = QLabel('Slider Value: 50')
        slider = QSlider(Qt.Horizontal)
        slider.setValue(50)
        slider.valueChanged[int].connect(lambda: self.change_value('Slider', slider.value(), slider_label))

        dial_label = QLabel('Dial Value: 50')
        dial = QDial()
        dial.setValue(50)
        dial.valueChanged[int].connect(lambda: self.change_value('Dial', dial.value(), dial_label))

        radio_button1 = QRadioButton('Radio Button 1')
        radio_button2 = QRadioButton('Radio Button 2')
        radio_button3 = QRadioButton('Radio Button 3')

        button_label = QLabel('None Selected')

        radio_button1.clicked.connect(lambda: self.radio_button(radio_button1, button_label))
        radio_button2.clicked.connect(lambda: self.radio_button(radio_button2, button_label))
        radio_button3.clicked.connect(lambda: self.radio_button(radio_button3, button_label))

        tab2_grid.addWidget(line_label, 1, 1, 1, 1)
        tab2_grid.addWidget(line_edit, 1, 2, 1, 3)
        tab2_grid.addWidget(slider_label, 2, 1, 1, 1)
        tab2_grid.addWidget(slider, 2, 2, 1, 2)
        tab2_grid.addWidget(dial_label, 3, 1, 1, 1)
        tab2_grid.addWidget(dial, 3, 2, 2, 2)
        tab2_grid.addWidget(button_label, 5, 1, 1, 1)
        tab2_grid.addWidget(radio_button1, 6, 2, 1, 1)
        tab2_grid.addWidget(radio_button2, 7, 2, 1, 1)
        tab2_grid.addWidget(radio_button3, 8, 2, 1, 1)

        tab2_box.addLayout(tab2_grid)
        tab2_box.addStretch()
        tab2.setLayout(tab2_box)

        tab3 = QWidget()
        tab3_box = QVBoxLayout()

        figure, axes = plt.subplots()
        self.canvas = FigureCanvas(figure)

        random_button = QPushButton('Random')
        random_button.clicked.connect(lambda: self.set_graph_values(figure, axes))

        tab3_box.addWidget(random_button)
        tab3_box.addWidget(self.canvas)

        tab3.setLayout(tab3_box)

        tab_widget.addTab(tab1, 'tab 1')
        tab_widget.addTab(tab2, 'tab 2')
        tab_widget.addTab(tab3, 'tab 3')
        self.mainLayout.addWidget(tab_widget)

    def change_value(self, name, value, label):
        new_value = name + ' Value: ' + str(value)
        label.setText(new_value)

    def set_graph_values(self, fig, ax):
        plt.cla()
        data = [random.random() for i in range(25)]
        ax.plot(data)
        ax.set_title('Random Plot')
        self.canvas.draw()

    def radio_button(self, button, label):
        text = 'Selected: ' + button.text()
        label.setText(text)


if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    app.exec_()
