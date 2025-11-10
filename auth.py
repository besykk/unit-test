def login(user, password):

    correct_user = "home"
    correct_password = "qwerty1234"

    if user == correct_user and password == correct_password:
        return "Успешно"
    else:
        return "Ошибка"

