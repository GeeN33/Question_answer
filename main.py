import json
import random

class Question:
    """
     класс Question имитация вопроса
    """
    def __init__(self, question:str, complexity:str, answer:str):
        self.question = question
        self.complexity = complexity
        self.answer = answer
        self.balls = 0

    def get_points(self) -> int:

        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        self.balls = int(self.complexity) * 10
        return self.balls

    def is_correct(self, answer:str) -> bool:
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        if answer == self.answer:
            self.answer_f = True
            return self.answer_f

        else:
            self.answer_f = False
            return self.answer_f

    def build_question(self) -> str:
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.question} \nСложность: {self.complexity}/5'


    def build_positive_feedback(self) -> str:
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        return f'Ответ верный, получено {self.get_points()} баллов'


    def build_negative_feedback(self) -> str:
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f'Ответ неверный, верный ответ {self.answer}'

def load_question() -> list:
    """
    Загружает список вопросы из файла
    :return:
    """
    questions = []
    with open("questions.json", "r") as read_file:
        for quest in json.load(read_file):
            questions.append(Question(quest['q'], quest['d'], quest['a']))

    return questions

def main():
    questions = load_question()

    random.shuffle(questions)

    print('Игра начинается!')
    for question in questions:
        print(question.build_question())
        if question.is_correct(input()):
            print(question.build_positive_feedback())
            print('--------------------------------------')
        else:
            print(question.build_negative_feedback())
            print('--------------------------------------')

    ball_sum = 0
    answer_count = 0
    for question in questions:
        ball_sum += question.balls
        if question.answer_f:
            answer_count += 1

    print('Вот и всё!')
    print(f'Отвечено {answer_count} вопроса из {len(questions)}')
    print(f'Набрано баллов: {ball_sum}')


main()