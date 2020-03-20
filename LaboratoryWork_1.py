import math

def say_hello(name):
    print("Hello! My name", name)

say_hello("Vika")

# Вычисление факториала
def Factorial():
    num = int(input("Введите число для нахождения факториала: "))
    i = 1
    factorial = 1
    while i<=num:
        factorial *= i
        i += 1
    print("Факториал числа", num, "равен", factorial)

Factorial()

print("\nЦикл for:")
for i in range(0, 10):
    print(i**2, end="\t")

# Вычисление площадей
print("\nВычисление площадей:")
figure = int(input("Укажите код фигуры для вычисления площади (квадрат -1, круг - 2): "))
if figure == 1:
    rib = int(input("\nВведите значение стороны квадрата: "))
    S = rib**2
    print("Площадь квадрата равна ", S)
elif figure == 2:
    R = int(input("\nВведите значение радиуса круга: "))
    S = math.pi * R**2
    print("Площадь круга равна ", S)
else:
    S = 0
    print("Неизвестная фигура")

print("Работа по нахождению площади завершена\n")

Name = "Angelina"
Surname = 'Jolie'
Age = "44 years old"
sp = " "
place_of_birth = "Los Angeles, California, USA"
Fullinfo = Name + " " + Surname + "," + Age + ". Place of birth: " + place_of_birth
print(Name, Surname, ",", Age)
print("Полная информация", Fullinfo)
L = len(Name)
print("Длина имени Angelina:",  L)
S = Fullinfo[0:8]
print("Срез: ", S)

# ключ:значение
dictCountries = {"Абхазия": "Сухум", "Азербайджан": "Баку", "Беларусь": "Минск", "Болгария": "София", "Великобритания": "Лондон",
                 "Германия": "Берлин", "Грузия": "Тбилиси", "Италия": "Рим", "Россия": "Москва", "Украина": "Киев"}
country = str(input("\nВведите название страны: "))
if country in dictCountries:
    FullStr = "Страна-столица: " + country + " - "
    print(FullStr, dictCountries[country], end="\n\n")
else:
    print("Элемент не найден\n")

dictCountries["Китай"] = "Пекин"
for key, value in dictCountries.items():
    print(key, " - ", value)
print("__________________\n")
actresses = ("Анджелина Джоли", "Нина Добрев", "Фиби Тонкин", "Шарлиз Терон", "Одри Хепберн")
print(actresses[0])
print(actresses[1])
print(actresses[2:5])