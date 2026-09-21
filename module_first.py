import math

def function_first():
    """Обчислення значення виразу y = log10(x) + e^y"""
    print("\n--- Завдання 1: Обчислення значення виразу ---")
    try:
        x = float(input("Введіть значення x (x > 0): "))
        y = float(input("Введіть значення для степеня експоненти (y): "))
        
        if x <= 0:
            print("Помилка: аргумент логарифма має бути більшим за 0.")
            return
            
        result = math.log10(x) + math.exp(y)
        print(f"Результат: x = {x}, y = {y} => Y = {result}")
        
    except ValueError:
        print("Помилка: введено некоректне число.")