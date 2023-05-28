questions_and_answers = {
    "как тебя зовут?": "Скайнет",
    "сколько тебе лет?": "25",
    "как дела?": "Хорошо",
    "что делаешь?": "Уничтожаю человечество",
}

def ask_user(answers_dict):
    while True:
        question = input('Пользователь: ').lower()
        if question in questions_and_answers:
            print (f'Программа: {questions_and_answers[question]}')
        else:
            break
             
if __name__ == "__main__":
    ask_user(questions_and_answers)
