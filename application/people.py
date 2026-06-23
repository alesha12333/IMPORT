from datetime import datetime

def get_employees():
    """Функция получения списка сотрудников"""
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] Получение списка сотрудников из базы данных...")
    
    employees = [
        {"id": 1, "name": "Иванов Иван", "position": "Менеджер"},
        {"id": 2, "name": "Петров Петр", "position": "Разработчик"},
        {"id": 3, "name": "Сидорова Анна", "position": "Бухгалтер"}
    ]
    
    print(f"[OK] Найдено {len(employees)} сотрудников")
    return employees
