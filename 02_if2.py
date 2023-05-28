def str_mark(first, second):
    if type(first) != str or type(second) != str:
        return 0
    elif first == second:
        return 1
    elif len(first) > len(second) and second != "learn":
        return 2
    elif first != second and second == "learn":
        return 3

def main():
    values = [
        (1, "string"),
        (2.6, 0),
        ("string", "string"),
        ("string", "String"),
        ("string", "word"),
        ("word", "string"),
        ("string", "learn"),
        ("string", "Learn"),
        ("word", "learn"),
        ("learn", "learn"),
        (0, "learn"),
        (True, False),
        (True, "True"),
        (0, False),
    ]
    for value in values:
        print(str_mark(value[0], value[1]))

if __name__ == "__main__":
    main()
