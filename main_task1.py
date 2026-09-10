import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def calculate():
    """Обчислення значення X за заданими а та b з перевіркою введених даних."""
    print("\n--- Виконання функції 1 ---")
    try:
        a = float(input("Введіть число a: "))
        b = float(input("Введіть число b: "))
    except ValueError:
        print("Помилка: введено не числове значення!")
        return

    if a <= 0 or b <= 0:
        print("Помилка: за умовами варіанта числа a та b повинні бути додатними (> 0)!")
        return

    if a < b and b == 0:
        print("Помилка: ділення на нуль неможливе (b = 0)!")
        return

    if a > b:
        x = b * a + 1
        print(f"Умова a > b виконана. X = {x}")
    elif a == b:
        x = -10
        print(f"Умова a == b виконана. X = {x}")
    else:
        x = (a - 5) / b
        print(f"Умова a < b виконана. X = {x}")

def diamond():
    print("\n--- Виконання функції 2 ---")
    try:
        n = int(input("Введіть ціле число N від 1 до 10: "))
    except ValueError:
        print("Помилка: введіть ціле число!")
        return

    if n < 1 or n > 10:
        print("Помилка: число N має бути в діапазоні від 1 до 10!")
        return

    rows = []

    for i in range(1, n + 1):
        rows.append(list(range(1, i + 1)))

    for j in range(1, n):
        row = list(range(1, n + 1)) + list(range(n - 1, n - 1 - j, -1))
        rows.append(row)

    max_row = list(range(1, n + 1)) + list(range(n, 0, -1))
    rows.append(max_row)

    for j in range(1, n):
        row = list(range(1, n + 1)) + list(range(n - 1, j - 1, -1))
        rows.append(row)

    for i in range(n - 1, 0, -1):
        rows.append(list(range(1, i + 1)))

    formatted_rows = [" ".join(map(str, row)) for row in rows]
    max_len = max(len(r) for r in formatted_rows)

    for r in formatted_rows:
        print(r.center(max_len))

def main():
    while True:
        print("\n================================")
        print("      ГОЛОВНЕ МЕНЮ (ЗАВДАННЯ 1) ")
        print("================================")
        print("1. Обчислити значення X (Функція 1)")
        print("2. Побудувати числову піраміду (Функція 2)")
        print("0. Вихід з програми")

        choice = input("Оберіть номер пункту меню: ")

        if choice == "1":
            calculate()
        elif choice == "2":
            diamond()
        elif choice == "0":
            print("Роботу програми завершено. До побачення!")
            break
        else:
            print("Помилка: обрано неіснуючий пункт меню. Спробуйте ще раз.")

if __name__ == "__main__":
    main()