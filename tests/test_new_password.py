import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    length = 16
    password = generate_password(length)
    assert len(password) == length

def test_passwords_are_different():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2
