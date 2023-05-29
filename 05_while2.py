def ask_user(answers_dict):
    while True:
        question = input('Пользователь: ').lower()
        if question in answers_dict:
            print (f'Программа: {answers_dict[question]}')
        else:
            break


def main():
    questions_and_answers = {
        "как тебя зовут?": "Скайнет",
        "сколько тебе лет?": "25",
        "как дела?": "Хорошо",
        "что делаешь?": "Уничтожаю человечество",
    }
    ask_user(questions_and_answers)


if __name__ == "__main__":
    main()
