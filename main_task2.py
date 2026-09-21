import sys
import io

import module_first
import module_second

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def main():
    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Обчислити значення виразу (Функція 1)")
        print("2. Знайти суму парних і добуток непарних чисел у діапазоні від 0 до 20 (Функція 2)")
        print("0. Вихід")
        
        choice = input("Оберіть номер завдання: ").strip()
        
        if choice == "1":
            module_first.function_first()
        elif choice == "2":
            module_second.function_second()
        elif choice == "0":
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, введіть 1, 2 або 0.")

if __name__ == "__main__":
    main()