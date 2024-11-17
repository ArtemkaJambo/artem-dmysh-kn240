def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Помилка! Ділення на нуль."
    return x / y

def calculator():
    print("Вибери операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    
    while True:
        choice = input("Введи номер операції (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Введи перше число: "))
                num2 = float(input("Введи друге число: "))
            except ValueError:
                print("Помилка! Потрібно ввести число.")
                continue

            if choice == '1':
                print(f"Результат: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Неправильний вибір операції.")

        # Запит на повторення
        next_calculation = input("Бажаєш виконати ще одну операцію? (так/ні): ")
        if next_calculation.lower() != "так":
            break

calculator()
