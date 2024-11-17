import numpy as np

temperature = [20.1, 20.1, 20.2, 20.4]
print("Початковий список температур:", temperature)
t1 = temperature * 5
print(f"При множенні на 5 маємо: {t1}")

def homework(message):
    print("\n>>>>>", message, "\n")

homework("Чому маємо такий результат?")

t1 = [x * 5 for x in temperature]
print(f"Тепер отримаємо: {t1}")

homework("Чому тепер множення успішне?")

t2 = np.array(temperature)
print("Масив з використанням методів NumPy:", t2)

t3 = t2 * 5
print("При множенні на 5 отримуємо:", t3)


# -----------------------------

