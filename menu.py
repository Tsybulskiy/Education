from task1 import solve_task1
from task2 import solve_task2
from task3 import solve_task3
from task4 import solve_task4
from task5 import solve_task5
from task6 import solve_task6
while True:
    print("Выберите номер задачи:")
    print("1. Задача 1")
    print("2. Задача 2")
    print("3. Задача 3")
    print("4. Задача 4")
    print("5. Задача 5")
    print("6. Задача 6")
    print("0. Выход")

    choice = input("Введите номер задачи (0-6): ")
    if choice == '0':
        break

    if choice == '1':
        solve_task1()
    elif choice == '2':
        solve_task2()
    elif choice == '3':
        solve_task3()
    elif choice == '4':
        solve_task4()
    elif choice == '5':
        solve_task5()
    elif choice == '6':
        solve_task6()