#-*- coding: utf-8
pers_001 = {'name': {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'},
    'address': ['г. Майкоп, ул. Коновалова д.34/1, кв.53'],
    'phone': {'home_phone': '67-87-92', 'mobile_phone': '8-929-232-84-96', 'mobile_phone_2': 'Нет'}
    }
pers_002 = {'name': {'last_name': 'Егоров', 'first_name': 'Егор', 'middle_name': 'Егорович'},
    'address': ['г. Сочи, переулок Ромашковый д.65, кв.17'],
    'phone': {'home_phone': '241-65-18', 'mobile_phone': '8-925-278-96-87', 'mobile_phone_2': '8-928-658-82-77'}
    }
pers_003 = {'name': {'last_name': 'Семенов', 'first_name': 'Семен', 'middle_name': 'Семенович'},
    'address': ['г. Екатеринбург, ул. Победы д.56, кв.25'],
    'phone': {'home_phone': 'Нет', 'mobile_phone': '8-921-247-66-77', 'mobile_phone_2': 'Нет'}
    }

call_crew = [pers_001, pers_002, pers_003]
call = str.capitalize(input('Введите Имя или Фамилию '))
found = False
for personal in call_crew:
    if call in personal['name']['first_name'] or call in personal['name']['last_name']:
        print('ФИО:', personal['name']['last_name'], personal['name']['first_name'], personal['name']['middle_name'])
        print('Адрес:', personal['address'][0])
        print('Телефон:', '\nДомашний.', personal['phone']['home_phone'], '\nМобильный.',
        personal['phone']['mobile_phone'],
        '\nДополнительный.', personal['phone']['mobile_phone_2'])
        found = True

if not found:
    print("Такого имени в базе данных нету. ")



def fibonacci(x):
    if x < 2: return 1
    return (fibonacci(x-2) + fibonacci(x-1))

def factorial(x):
    if x < 2: return 1
    return (x * factorial(x-1))

def main():
    funcs = [fibonacci, factorial]
    n = 10
    for i in range(len(funcs)):
        print (funcs[i](n))

main()