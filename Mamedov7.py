import math

a = float(input("Введите первый катет (a): "))
b = float(input("Введите второй катет (b): "))

c = math.sqrt(a**2 + b**2)  # Вычисляем гипотенузу
p = a + b + c               # Вычисляем периметр

print(f"Гипотенуза: {c:.2f}")
print(f"Периметр: {p:.2f}")
