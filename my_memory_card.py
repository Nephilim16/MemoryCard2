from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from random import shuffle, randint

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Какой модуль в Python используется для работы с операционной системой?', 'os', 'sys', 'math', 'datetime'))
questions_list.append(Question('Как называется игра, созданная Маркусом Перссоном?', 'Minecraft', 'Terraria', 'Stardew Valley', 'Subnautica'))
questions_list.append(Question('Год создания 🦽Minecraft Dungeons🦽', '2020', '2018', '2019', '2015'))
questions_list.append(Question('Кому принадлежит Minecraft?', 'Microsoft', 'Mojang', 'Sony', 'Bethesda'))
questions_list.append(Question('Год создания Python', '1991', '2000', '1990', '2077'))

app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("прав ты или нет?")
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

total = 0
correct = 0

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
    update_stats()

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    global correct
    if answers[0].isChecked():
        correct += 1
        show_correct('Правильно!')
    else:
        show_correct('Неверно!')

def next_question():
    global total
    total += 1
    print('Статистика\n-Всего вопросов:', total, '\n-Правильных ответов:', correct, '\n-Рейтинг:', int(correct/total*100), '%')
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def update_stats():
    global total, correct
    lb_Result.setText('Правильных ответов: ' + str(correct) + ' из ' + str(total) + ' (' + str(int(correct/total*100)) + '%)')
    lb_Result.setAlignment(Qt.AlignCenter)

next_question()
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

btn_OK.clicked.connect(click_OK)

window.resize(400, 300)
window.show()
app.exec()