"""
Предметная область – магазин. Разработать класс Shop, описывающий работу магазина продуктов.
Разработать класс Products, продукт описывается следующими параметрами: уникальный идентификатор,
название продукта, стоимость, количество. Разрабо тать класс FruitProduct на базе класс Product,
фрукт характеризуется параметрами: страна изготовителя, срок годности.

"""

# Класс "Предприятие"
#------------------------------------------------------------------------------
class Enterprise:

    def __init__(self, name, employees=[]):
        self.name = name
        self.employees = employees

    def __str__(self):
        return 'Enterprise <Company name: {0}; Employee count: {1}>'.format(self.name, self.employee_count())
    # Поиск сотрудника по табельному номеру, возвращает объект типа Сотрудник или False
    def get_emp_by_id(self, emp_id):
        e = False
        i = self.employee_count()
        j = 0

        while j < i:
            if self.employees[j].get_emp_id() == emp_id:
                e = self.employees[j]
                break
            j += 1

        return e
    # Добавление сотрудника, по одному табельному номеру может быть только один сотрудник
    def add_employee(self, employee):
        if not self.get_emp_by_id(employee.get_emp_id()):
            self.employees.append(employee)
            return True
        else:
            return False
    # Удаление сотрудника по табельному номеру
    def rem_employee(self, emp_id):
        e = self.get_emp_by_id(emp_id)
        if e:
            self.employees.remove(e)
            return True
        else:
            return False
    # Количество сотрудников на предприятии
    def employee_count(self):
        return len(self.employees)
    # Список сотрудников предприятия
    def employee_list(self):
        for e in self.employees:
            print('  {}'.format(e))
    # Выводим информацию о предприятии
    def info(self):
        print(self)
        self.employee_list()
#------------------------------------------------------------------------------
# Класс "Человек"
#------------------------------------------------------------------------------
class Person:

    def __init__(self, last_name, first_name, mid_name, birth_dt, phone_num):
        self.last_name  = last_name
        self.first_name = first_name
        self.mid_name   = mid_name
        self.birth_dt   = birth_dt
        self.phone_num  = phone_num

    def __str__(self):
        return 'Person <{0} {1} {2}>'.format(self.last_name, self.first_name, self.mid_name)
#------------------------------------------------------------------------------
# Класс "Сотрудник"
#------------------------------------------------------------------------------
class Employee(Person):

    def __init__(self, last_name, first_name, mid_name, birth_dt, phone_num, emp_id, depart_id, salary):
        super().__init__(last_name, first_name, mid_name, birth_dt, phone_num)
        self.emp_id     = emp_id
        self.depart_id  = depart_id
        self.salary     = salary

    def __str__(self):
        return 'Employee <{0}: {1} {2} {3}>'.format(self.emp_id, self.first_name, self.last_name, self.mid_name)

    def get_emp_id(self):
        return self.emp_id
#------------------------------------------------------------------------------
# Тест
#------------------------------------------------------------------------------
# Создаём предприятие

print('Создаём предприятие')
enterprise = Enterprise('Alphabet')
enterprise.info()

# Создаём первого сотрудника через переменную
print('\nСоздаём первого сотрудника')
employee1 = Employee('Brin', 'Sergey', 'Michaylovich', '21.03.1973', '+18880000001', '00000001', 'top', '1')
enterprise.add_employee(employee1)
enterprise.info()

# Создаём второго сотрудника без промежуточной переменной
print('\nСоздаём второго сотрудника')
enterprise.add_employee(Employee('Black', 'John', '', '09.09.1989', '+18567834001', '03423401', 'any', '10500'))
enterprise.info()

# Создаём третьего сотрудника с уже имеющимся табельным номером
print('\nПытаемся создать третьего сотрудника с уже имеющимся табельным номером')
enterprise.add_employee(Employee('White', 'John', '', '01.09.1989', '+18567834001', '03423401', 'any', '5000'))
enterprise.info()

# Удаляем первого сотрудника подавая на вход весь экземпляр объекта Сотрудник
print('\nУдаляем первого сотрудника')
enterprise.rem_employee(employee1.get_emp_id())
enterprise.info()