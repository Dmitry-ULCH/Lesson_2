def hello_user():
    question = "Как дела?"
    try:
        print(question)
        while True:
            answer = input()
            if answer.lower() == "хорошо":
                break
            else:
                print(question)
    except KeyboardInterrupt:
        print("Пока!")
 
if __name__ == "__main__":
    hello_user()