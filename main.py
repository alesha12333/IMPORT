from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    """Основная функция программы"""
    current_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    
    print("=" * 60)
    print("ПРОГРАММА «БУХГАЛТЕРИЯ»")
    print(f"Дата и время запуска: {current_date}")
    print("=" * 60)
    
    # Вызов функций
    get_employees()
    calculate_salary()
    
    print("=" * 60)
    print("Программа завершила работу")

if __name__ == '__main__':
    main()
