from accounting.application.db.people import get_employees
from accounting.application.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
