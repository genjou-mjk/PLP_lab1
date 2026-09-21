def function_second():
    """Знайти суму парних і добуток непарних цілих чисел у діапазоні від 0 до 20"""
    print("\n--- Завдання 2: Сума парних та добуток непарних чисел (0-20) ---")
    total_sum = 0
    odd_product = 1
    
    for i in range(0, 21):
        if i % 2 == 0:
            total_sum += i
        else:
            odd_product *= i
            
    print(f"Сума парних чисел у діапазоні від 0 до 20: {total_sum}")
    print(f"Добуток непарних чисел у діапазоні від 0 до 20: {odd_product}")