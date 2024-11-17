name = 'Artem'
surname = 'Dmysh'

print(name + ' ' + surname)

firstValue = 20
secondValue = 20
print(firstValue + secondValue)

name = 'Artem'
array = [1]
array.append(2)
print(array)
print('the length of the word: ',len(name))

letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"{i} {letters[i]}")

for i in range(1,4):
    print(i)

checkData = name == surname
print(checkData)

is_sunny = True
is_raining = False

if is_sunny:
    print("Сьогодні сонячно, виходь на вулицю!")
else:
    print("Сьогодні не сонячно, залишайся вдома.")

if is_raining:
    print("Візьми парасольку!")
else:
    print("Парасолька не потрібна.")

A = 0
try:
    print("Що буде якщо", 10/A, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")



this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це її виклик:", this_is_lambda('Artem', 'Dmysh'))