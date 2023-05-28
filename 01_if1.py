user_age = int(input("Введите возраст: "))

def get_occupation(age):
    if age <= 0:
        return "Поздравляем, Вы ещё не родились!"
    elif age < 3:
        return "Можете пешком ходить под стол"
    elif age < 7:
        return "Собирайтесь быстрее в садик!"
    elif age < 18:
        return "Вставайте! Пора в школу!"
    elif age < 25:
        return "Сессия сама не закроется!"
    elif age < 65:
        return "Кто хочет поработать?"
    else:
        return "Наконец-то можно и отдохнуть!"
    
def main():
    user_occupation = get_occupation(user_age)
    print(user_occupation)

if __name__ == "__main__":
    main()