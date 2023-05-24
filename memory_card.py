from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QRadioButton,
                            QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QButtonGroup)



class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q = Question('Сколько лет городу Бухара?', '2500', '1200', '3000', '2100')
q1 = Question('Когда закончилась вторая мировая война?', '1945', '1942', '1943', '1940')
q2 = Question('Самая дорогая машина?', 'Rolse Rouse Gost ', 'Ferarri Spider', 'McLaren', 'Cevrolet Matiz')
q3 = Question('Кто лучший футболист в мире?', 'Ronaldo', 'Messi', 'Mbappe', 'Hakimi')

question_list.append(q)
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400, 200)

question = QLabel('Сколько лет Ташкенту?')
r_btn1 = QRadioButton('2700')
r_btn2 = QRadioButton('10600')
r_btn3 = QRadioButton('1000')
r_btn4 = QRadioButton('5200')

btn = QPushButton("ответить")

RadioGroupBox = QGroupBox('Варианты ответов:')
h_line_group = QHBoxLayout()
v_line_group1 = QVBoxLayout()
v_line_group2 = QVBoxLayout()

v_line_group1.addWidget(r_btn1)
v_line_group1.addWidget(r_btn2)
v_line_group2.addWidget(r_btn3)
v_line_group2.addWidget(r_btn4)

h_line_group.addLayout(v_line_group1)
h_line_group.addLayout(v_line_group2)

RadioGroupBox.setLayout(h_line_group)

AnsGroupBox = QGroupBox('Правильный ответ')
result = QLabel('Прав ты или нет?')
correct = QLabel('Ответ будет здесь!')
ans_v_line = QHBoxLayout()
ans_v_line.addWidget(result, alignment=(Qt.AlignHCenter | Qt.AlignVCenter ))
ans_v_line.addWidget(correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(ans_v_line)

#######################################
ButtonGroup = QButtonGroup()
ButtonGroup.addButton(r_btn1)
ButtonGroup.addButton(r_btn2)
ButtonGroup.addButton(r_btn3)
ButtonGroup.addButton(r_btn4)
#######################################
