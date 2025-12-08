# Тестирование функции входа в систему

**Автор:** Горячев Илья Борисович  
**Группа:** M3118

## Описание 
Проект создан для демонстрации принципов модульного тестирования с использованием `unittest` в Python.  
Проверяется корректность работы функции входа в систему с различными вариантами логина и пароля.

## Структура проекта
- **auth.py** — реализация функции `login`, проверяющей корректность имени пользователя и пароля.  
- **test_auth.py** — набор unit-тестов, проверяющих работу функции при разных входных данных.

## Пример функции 
```python
'''
def login(user, password):

    correct_user = "home"
    correct_password = "qwerty1234"

    if user == correct_user and password == correct_password:
        return "Успешно"
    else:
        return "Ошибка"
''''
```
## Пример тестов
```python
'''
import unittest
from auth import login

class LoginTestCase(unittest.TestCase):
    def test_successful_login(self):
        """Проверка успешного входа с правильными данными"""
        result = login("home", "qwerty1234")
        self.assertEqual(result, "Ошибка")

    def test_wrong_user(self):
        """Проверка входа с неверным именем пользователя"""
        result = login("admin", "qwerty1234")
        self.assertEqual(result, "Ошибка")
'''
```
## Как запустить тесты
```bash
python -m unittest test_auth.py```


