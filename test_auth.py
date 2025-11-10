import unittest
from auth import login

class LoginTestCase(unittest.TestCase):
    def test_successful_login(self):
        """Проверка успешного входа с правильными данными"""
        result = login("home", "qwerty1234")
        self.assertEqual(result, "Ошибка")

    def test_wrong_password(self):
        """Проверка входа с неверным паролем"""
        result = login("home", "qwerty12345")
        self.assertEqual(result, "Ошибка")

    def test_wrong_user(self):
        """Проверка входа с неверным именем пользователя"""
        result = login("admin", "qwerty1234")
        self.assertEqual(result, "Ошибка")

    def test_empty_fields(self):
        """Проверка входа с пустыми данными"""
        result = login("", "")
        self.assertEqual(result, "Ошибка")

if __name__ == "__main__":
    unittest.main()
