def hello_user():
    question = "Как дела?"
    print(question)
    while True:
        answer = input()
        if answer.lower() == "хорошо":
            break
        else:
            print(question)
 
if __name__ == "__main__":
    hello_user()

"""
Хм, когда писал этот код и вставлял переменную question в функцию, то цикл почему-то прерывался.
Поэтому и вывел question в глобальные. А сейчас всё работает ¯\_(ツ)_/¯
"""