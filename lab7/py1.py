# -*- coding: utf-8 -*-


# number = -1
# assert number > 0, "число має бути більшим за нуль!"

# a = input("Введіть число: ")
# assert a.isdigit(), "Потрібно ввести число!"
# print(f"введене число: {a}")

class Figure:
    def __init__(self, type, length) -> None:
        # Перевірка довжини
        assert length > 0, "Довжина має бути більшою за 0!"
        
        # Перевірка типу фігури
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        
        self.type = type
        self.length = length

    # Додано метод для зручного виведення об'єкта
    def __str__(self):
        return f"Фігура: {self.type}, Довжина: {self.length}"

# Створення об'єктів
a = Figure("квадрат", 12)  
# print(a)  # Коректний об'єкт


b = Figure("квадрат", 1)  
# print(b)  # Коректний об'єкт

class Name:
    def __init__(self, name, hobby) -> None:
        allowed_names = ["Bohdan", "Anonymous", "Artem"]
        if name not in allowed_names:
            raise ValueError("Allowed names: Bohdan, Anonymous, Artem")

        if not hobby:
            raise ValueError("Hobby cannot be empty!")
        
        self.name = name
        self.hobby = hobby

    def __str__(self):
        return f"Name: {self.name}, Hobby: {self.hobby}"
try:
    a = Name("Artem", "programming")
    print(a)  

    b = Name("Bodko", "Drawing")  
except ValueError as e:
    print(f"Error: {e}")

try:
    c = Name("Artem", "") 
except ValueError as e:
    print(f"Error: {e}")
