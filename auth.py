def login(user, password):

    correct_user = "home"
    correct_password = "qwerty1234"

    if user == correct_user and password == correct_password:
        return "Успешно"
    else:
        return "Ошибка"


if __name__ == "__main__":
    print("=== Вход в систему ===")

    user = input("Введите логин: ")
    password = input("Введите пароль: ")

    result = login(user, password)

    print("\nResult:", result)
