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
