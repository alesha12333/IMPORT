from datetime import datetime

def calculate_salary():
    """Функция расчета заработной платы"""
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] Выполняется расчет заработной платы...")
    print("[OK] Зарплата успешно рассчитана!")
    return 50000  # Возвращаем для примера
