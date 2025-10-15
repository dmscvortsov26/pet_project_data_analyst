#print,(печать)
# input, (ввод данных с клавиатуры)
# sep,end, (сеп = между симовали, енд = конец)
# int,str, ( инт натуральное число  1, 2 != 0.1 и тд, стр = строчное значение а, б, с и тд) 
# if, else, elif ( оператор условий, если, если не , то, если не то и не то, получается = )
# операторы для сложных условий 
# and, or, not (и, или , не )
# float,( действительные числа 1.0 2.0 3.5 и тд)
# min, max, ( мин и максисум)
# abs ( модуль -(-) или -(+))
# len, считает количество символов например в input()
# in ( оператор В)
# math ( модуль мини  мат библиотеки )
# for "название" in rage("количество выполнений"): ( общепринятые значения для названия условия  I, J, K, L, M, N)
# while
# break, continue ***
# ревью кода
# вложенные циклы ****
# оператор chr(символ) то же самое что и орд, только наооброт 65 = A
# оператор ord(ордер) есть таблица символов Unicode. в ней A = 65 (И у него есть двоичн код) орд определяет число 65 в А
# функция def() - определять 
# glonal "переменная" в глобальн внутри фунции def ( есть глобальн и локальная )
# return возращает значение 
# round ( округление )
# Модуль random
# включает в себя:
# randint() принимает два обязательных аргумента a и b и возвращает случайное целое число из отрезка
# randrange() принимает такие же аргументы, что и функция range()
# random() возвращает случайное число с плавающей точкой в диапазоне от 0.0 до 1.0 (исключая 1.0).
# uniform() тоже возвращает случайное число с плавающей точкой, но при этом она позволяет задавать диапазон для отбора значений.
# shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.
# choice() принимает список (строку) в качестве обязательного аргумента и возвращает один случайный элемент из переданного списка (строки).
# sample() принимает два обязательных аргумента: список (строку) и количество случайных элементов, а возвращает список случайных элементов в указанном количестве.
# map()

# format() and {} - (заполнитель) формат кратко говоря int + str {} - запоминает где выбранн условие нужно заполнить, условно
# birth_year = 1992
# text = 'My name is Timur, I was born in {}'.format(birth_year)
# print(text)
# f-строка , по сути более читабельн и оптимиз вариант format()


# АЛГОРИТМЫ++__++_++_+__++_+_+_ ПРИ СОРТИРОВКЕ

# списки ----------- СПИСКИ 
# n = [1, 2, 3, 4, 5]
# list = (1, 2, 3, 4, 5) одно и то же
# при работе со списками:
# методы списка
# .append() - добавлять. Добавляет список по заданому условию( например через иф ) в скобочке (i напр)
#разница между append and extend - первый добавляет строку целиком, а второй по символу (p,y,t,h,o,n)
# .extend() - расширять , по сути складывает списки ( расширил список, добавик к нему другой)
# del "название строки"[номер индекса] оператор del удаляет по заданному условию, также работает со срезами
# split() разбивает строку на слова и возвращает список, содержащий все слова
# у split() есть ДОП в виде ip ( место разделения) (ip = название строки или переменной, оно может быть любое)
# join()собирает строку из элементов списка, делает наооброт split()
# у join, как и у split(), есть походий метод с ip, перед .join указать символ крепления строки(=+- и тд *** * 81 и тд)
# строковый метод split() служит для преобразования строки в список, а метод join() — для преобразования списка в строку.
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers) символ * - распаковывет элементы в списке
# insert() заменяет ( по типу реплейса )
# index() == index() в медоте строк ( находит индекс в списке ) можно использовать с in
# remove() удаляет значение в отличии от del = удаляет индекс 
# но remove удаляет первое вхождение, при необх можно через цикл и принадлежности in
# pop() удаляет и возращает в строку (отдельно от списка) (условие = a, из abc = a)
# count() == count() в методе строк 
# .reverse() - переворот. Переворачивает список = аналогично [::-1]
# clear() удаляет все элементы из списка

# Например, для создания списка целых чисел от 0 до 9 мы вынуждены писать такой код:
# numbers = []
# for i in range(10):
#     numbers.append(i)
# numbers = [i for i in range(10)]
# две строки (1- кол во строк 2 строки)
# n = int(input())
# lines = [input() for _ in range(n)]
# интерпритация
# lines = [input() for _ in range(int(input()))]

# copy() копирует (создает) копию списка, аналогично с
# names = ['Gvido', 'Roman', 'Timur']
# names_copy1 = list(names)   
# names_copy2 = names[:]



# срезы (slikes)
# конвертация строк 
# методы строк --=-==-=-==-=-=-=-=-=-=-=--= 
# capitalize – писать прописными буквами, закрепить
# swapcase – обменять регистр. swap – гл. обмениваться, case – случай, регистр, падеж, дело, расследование
# title – заголовок, титул
# set() - применяемая к строке, создает множество из неповторяющихся элементов строки set('aabbccdd') = (a, b, c, d).
# lower – нижний
# upper – верхний
# count - подсчет 
# start|end\swith узнает начинается или заканчивается строка в строке
# find\rfind находит ё индекс вхождения ( условно первую а в строке , можно использовать как опер in) false = -1
# index\rindex работает по принципу финд и рфинд, но в случае false = выдает ошибку 
# strip\lstrip\rstrip удаляет пробелы в начале и конце / в начале / в конце ( также могут убирать условно символы = +абс+ = убирают + = абс)
# replace заменяет по условию ( условно а на б ( то есть олд на нев))
# isalnum = is alpha numeric  - это буквенно цифровой?/ или только буквы или цифры ( без =-+_ и тд)
# isalpha  = is alpha  - это буквенный?
# isdigit    = is digit    - это цифра, число?
# islower  = is lower - это нижний?
# isupper = is upper -  это верхний?
# isspace = is space - это пробел (промежуток)?

# Допольнительно для for: 
# Например, чтобы начать отчёт с 1го: for i in range(1, 5):     
# print(i) Вывод: 0 1 2 3 4
# , можно указать шаг: for i in range(1, 8, 2):     
# print(i) Вывод: 1 3 5 7 
# А также шаг в обратном порядке" -2" и начать не с 1, а с 20: for i in range(20, 8, -2): 
# print (i) Вывод: 20 18 16 ... 10

print ("hello world")
print('Я учусь программировать на Python!', end="\n\n\n\n\n\n")
print("I'm", 'the', "BAD", 'guy') 
print('I"m the BAD guy')  
print('*', '**', '***', '****','*****', '******','*******', sep="\n")
print('*', "*2", sep="\n") 
print ("как тебя зовут?")
a = input() 
print("здравствуй", a)
print ("сколько тебе лет?")
b = input()
print("замечательно!", "число", b , "явялется фундаментальным")

#кроме чисел а и б, можно давать названия, пример:
print ("выберите число:", "12", "24", "34", "44", "55", sep="\n")
name = input()
print ("если ваше число", name, "вы победили")

print(a)

print ("ваш город проживания?")
city = input()
print (city, "это большой, и замечательный город")

Name = "Тимма"
print("Привет", Name , a)


name1 = 'Тимур'
name2 = name1
name1 = 'Гвидо'

print(name1)
print(name2)

# наименование 2,будет имееть значение наименования 1, после этого наименование 1 в третей строке будет имееть другое значение
# каждая последущяя команда наименование name1, будет присваивать ему значение

print("составь уравнение") 
print("a2 + x2 = y")
print ("a2")
a2 = input()
print("x2")
x2 = input()
y = a2+x2
print(y)

# уравнение не вышло, число а2 и х2 не суммировались, а просто вывелись последовательно , т.е 4+6=46, 561+541=561541
# если записать уже готовые числа, т.е а= 10 и б=20, то х будет 30
# для этого используется функция int, т.е

num1 = int(input())
num2 = int(input())
a = num1+num2
print(a)




print('Как тебя зовут?')
name = input()

# можно преобразовать в 

name = input('Как тебя зовут?')

print("Ты тоже Аянами Рей")
print("Кто ты?")
name = input()
print("Ты тоже", name)
print("Кто ты?")
print("Аянами Рей")
print("Ты тоже Аянами Рей?")

# sep - разделитель и end - окончание, идет по дефолту в print, но если добавить , как функцию, меняет значени \n (перенос строки)

minus = '-'
print('a', 'b', 'c', end=minus)
print('second line')


print('a', '\n', 'b', '\n', 'c', sep='*', end='#')

print('Mercury', 'Venus', sep='*', end='!')
print('Mars', 'Jupiter', sep='**', end='?')


# множественное присваивание в 1 строке
f,i,o = "Dima", "Sot", "Maksimovich"
print("имя", f , "фамилия", i , "отчество" , o)

# использование инт и стр 

a = int(input())
b=a+1
c=b+1

print(a)
print(b)
print(c)

# 2 задача с инт 

a=int(input())
b=int(input())
c=int(input())
print(a+b+c)


# 3 задача 

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print((a + b + c + d) * 3) 

#  ее интерпритация 

print((int(input())+int(input())+int(input())+int(input())) * 3)

number = int(input())
print("Следующее за числом", number, "число:", number + 1)
print("Для числа", number, "предыдущее число:", number -1)

# задача 3

a = int(input())
b = int(input())

с= a+b
d= a-b
f= a*b

print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)


# задача 4 

a1 = int(input())
d = int(input())
n = int(input())
an = a1 + d * (n-1)

print(an)


#  задача 5

x = int(input())
print(x, x*2, x*3, x*4, x*5, sep="---")

# # Доп функции 
#    **	Возведение в степень ( по сути символ возведения)
#     %	Остаток от деления ( обратный процесс делению без остатка, 10 % 3 = 1 - остаток)
#    //	Целочисленное деление ( без десятичных, условно 10 // 3 = 3)

# Обратите внимание: при 0 < n < m результатом деления n % m является число n, а результатом деления n // m является число 0.
# Приведённый ниже код:
# print(5 % 9)
# print(3 % 13)
# print(5 // 9)
# print(3 // 13)
# выводит:
# 5
# 3
# 0
# 0

#  прогрессия арифметическая и геометрическая
 

b1 = int(input())
q = int(input())    
n = int(input())

bn = b1 * 1 * (q ** (n-1))  

print(bn)


# задача 6

number = int(input())

km = number // 100

print(km)


#  задача 7

d = int( input())
o = int( input())

print(o // d)
print(o % d)

#  задача 8

n = int(input())
print((n+1) // 2)

# интерпритация 

p = int(input())
print(p - p//2)


#  задача 9 

time = int(input())

a = time // 60
b = time % 60

print(time, "мин - это", a, "час", b, "минут.")


# задача 10+ 

a=int(input())  #вводимое значение
b=(a+3)//4      # поскольку мест в купе 4, доьавляем еще три от обнуления при целочисленном делении, и собственно делим нацело на 4
print (b)



# Алгоритм получения цифр 
# n-значного числа
# Несложно понять, по какому алгоритму можно найти каждую цифру 
# n-значного числа num:

# num%10-последняя цифра.

# (num%100)//10=средняя цифра (в трёхзначном числе).

# num//100=первая цифра.


# задача 11

a = int(input())

a1 = a // 100
a2 = (a % 100) // 10
a3 = a % 10

sum = a1 + a2 + a3
print("Сумма цифр", sum)

proizvedenie = a1 * a2 * a3
print("Произведение цифр", proizvedenie)


#  задача с вычислением номера обьекта 
# вычислется по формуле х + ( число для деления до единицы) \ на второе известное число


#  ЗАДАЧА 12+

a = int(input())    

a1 = a // 1000
a2 = (a % 1000) // 100
a3 =(a % 100) // 10
a4 = a % 10

print("Цифра в позиции тысяч равна", a1)
print("Цифра в позиции сотен равна", a2)
print("Цифра в позиции десятков равна", a3)
print("Цифра в позиции единиц равна", a4)

# интерпритация ( самый простой вариант )

n = int(input())

d1 = (n // 10 ** 3) % 10
d2 = (n // 10 ** 2) % 10
d3 = (n // 10 ** 1) % 10
d4 = (n // 10 ** 0) % 10

print("Цифра в позиции тысяч равна", d1)
print("Цифра в позиции сотен равна", d2)
print("Цифра в позиции десятков равна", d3)
print("Цифра в позиции единиц равна", d4)


# 1 экзамен 
print("*", "*", sep="***************")
print("*", "*", sep="               ")
print("*", "*", sep="               ")
print("*", "*", sep="***************")

# интерпритация 

# put your python code here
print("*" * 17)
print('*' + ' ' * 15 + '*')
print('*' + ' ' * 15 + '*')
print("*" * 17)

#  2 Экзамен 

a = int(input())    
b = int(input())    
print("Квадрат суммы", a, "и", b, "равен", (a+b)**2)
print("Сумма квадратов", a, "и", b, "равен", a**2 + b**2)


# put your python code herea = int(input())    
a = int(input())    
b = int(input())    

K2 = (a + b ) ** 2
S2 = a ** 2 + b ** 2

print("Квадрат суммы", a, "и", b, "равен", K2)
print("Сумма квадратов", a, "и", b, "равен", S2)


# 3 экзамен

# 1 решение задачи 
a1 = int(input())    
b1 = int(input())

a = a1 ** 29
b = b1 ** 27

print (a + b)

#  2 решение задачи 

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a ** b + c ** d)


# Условия для If: если,их всего 6 ===>  (х > 7, если < 7, если х ><=(два условия, больше или меньше) 7, и х = или не неравен 7)
#  помимо if, используется else() and elif( нужна для более сложных структур, упращает читаемость кода)

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('числа равны')
else:
    print('числа не равны')

    #  обязательно условия == (сравнение значения равный они или нет)
    #  условие = , что бы обновить значение переменной, условно а = 50 , а = 100, использовалось значение 50, но по окончанию условия 100)
    #  есть также значение !=, что означает неравеннство, условно a != б, б != с, не факт что а и с будут неравнны 

    # Отношение порядка по курсам математики
    # 1, если а == б , б == с, то а == с (если бы использовалость значение =, число бы меняли значение, сравнение ==)
    # 2, если а > б, б > с, то а > с
    # 3, если а || б, б || с, то а || с
    # 4, если а делится на б, б делится на с, то а делится на с 



num = int(input())

last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')

#  2.1 задача

    word = input()

if word == 'Python':
    print('ДА')
else:
    print('НЕТ')
    

    #  задача 2.2.

    num1, num2, num3 = int(input()), int(input()), int(input())

counter = 0  # переменная счётчик, то есть нам неизвестно число четных значений, поэтому создаем условие 0, можно написать любое
if num1 % 2 == 0:  # то есть идет сравнение, число делится на 2( значит четное, можно делить на 4, но на 2 оно не делится)
    # делится на 2 и == на 0, что бы в решение не было остатка, условно 1,3,5 и других значений
    counter = counter + 1  # увеличиваем счётчик на 1, из нашей первой строчки где коунтер = 0, мы к этому значению добавляем +1, если оно истино
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1

print(counter)


# для if, в конце строчки обязательно двоеточие ::::::::

cod = input()
cod2 = input()

if  cod == cod2:
    print("Пароль принят")
if cod != cod2:
    print("Пароль не принят")


    # Задача 2.3

    a = int(input())

a1 = a // 1000
a2 = (a % 1000) // 100
a3 = (a % 100) // 10
a4 = a % 10

b = a1 + a4
c = a2 - a3

if b == c:
    print("Да")
if b != c:
    print("Нет")

    # задача 2.4

age = int(input())

if age < 18:
    print("Запрещенно")
if age >= 18:
    print("Разрешенно")


    #  Задача 2.5

    a, b, c = int(input()), int(input()), int(input())

n = c - b
d = b - a   

if n == d:
    print("Да")

if n != d:
    print("Нет")

    #  Задача 2.6 

    age = int(input())

if age <= 13:
    print("детство")
if 14 <= age <= 24:
    print("молодость")
if 25 <= age <=59:
    print("зрелость")
if age >= 60:
    print("старость")

    # Задача 2.7

    a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:     # сравниваем два числа, если а больше б, то оно берет значение б,если меньше , то остается 
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)

#  Задача 2.8

a = int(input())
b = int(input())
c = int(input())

if a < 0:
    a = 0
if b < 0:
    b = 0
if c < 0:
    c = 0
print(a+b+c)

# Задача 2.9 
#  УСЛОВИЯ AND ВЫПОЛНЯЮТСЯ КОГДА ВСЕ ТРЕБОВАНИЯ СООТВЕСВТУЮТ ПОСТАВЛЕНОЙ ЗАДАЧИ ( ЕСЛИ ОДНО ИЗ НЕСКОЛЬКИХ ОТРИЦАТЕЛЬНОЕ, ОН -)
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

#  Задача 3.
# Оператор or, требуется выполнение одного, поставленного условия (даются условно 3 варианта по условия or, одно из них должно +)

city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

# Задача 3.1
# В операторе if, можно использовать два условия 
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

    #  Задача 3.2

num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')

    # Задача 3.3
    
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')

    # Задача 3.2

    a = int(input())

if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5

p = (a + b) * (a + b)
print(p)
#  ответом будет 100, а не 58 потому что перед выводом  данных (принт) мы запрашиваем еще раз условие р - оно будет конечным


#  Задача 3.4
x = int(input())

if x > -1 and x < 17:
    print("Выполняется")    
else:
    print("Невыполняется")

#  Задача 3.5

x = int(input())

if x > -3 and x < 7:
    print("Не принадлежит") 
else: 
    print("Принадлежит")

    # Задача 3.6

    x = int(input())

if x > -30 and x <= -2 or x > 7 and x <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")

    #  Задача 3.7

    x = int(input())

if (x >= 1000 and x <= 9999) and (x % 7 == 0 or x % 17 == 0):
    print("YES")
else:
    print("NO")

    # Задача 3.8

    a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    print("YES")
else: 
    print("NO")

    # Задача 3.9

    x = int(input())

if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
        print("YES")
else:
    print("NO")

    # Задача 4. С ШАХМАТАМИ 
    a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d:
    print("YES")
else:
    print("NO")


    # Задача 5 ШАХМАТЫ С КОНЕМ

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (((c == a + 2) and (b == d + 1) or
   (c == a + 2) and (b == d - 1) or
   (c == a - 2) and (b == d + 1) or
   (c == a - 2) and (b == d - 1) or
   (c == a + 1) and (b == d + 2) or
   (c == a + 1) and (b == d - 2) or
   (c == a - 1) and (b == d + 2) or
   (c == a - 1) and (b == d - 2))):
   print("Да")
else:
    print("Нет")

# if (c == a + 2) or (c == a - 2):
#     print(a+2) 
#     if (d == b + 2) or (d == b -2):
#         print(b + 2)
#     else:
#         print("Нет")
# else:
#     print("Нет")


#   Задача - определенние плоскости координаты в векторе

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')


#  Задача - определенние бала по 100 балльной системе

#   1 КОД
x = int(input())                  

if x >= 90:
    print("5")
elif x >= 80:
    print("4")
elif x >= 70:
    print("3")
elif x >= 60:
    print("2")
else:
    print("1")

    # 2 КОД

grade = int(input())
    
if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70: 
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)


#  if elif and else читаются лучше , нежели продолжительный код if + else , тем не менее , else в 1 коде необязательный , как допустим
#  if - 1 условие
#  elif, это способ Python сказать, что “если предыдущие условные были неверными, тогда попробуйте это условное”.
#  else, способ закончить код, условно если предыдущие были ложные

traffic_light_signal = input('Введите сигнал светофора: ')

if traffic_light_signal == 'красный':
    print('Стой!')
elif traffic_light_signal == 'желтый':
    print('Приготовься...')
elif traffic_light_signal == 'зеленый':
    print('Иди!')

#  для себя запомнил это так: (if)Если ты неправ, (elif)значит я прав, (else)иначе мы оба дураки

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:


# 1 способ. Использование вложенного условного оператора.

a = int(input())
b = int(input())
c = int(input()) 

if a == b and b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
# 2 решение задачи 

if not ((a != b) or (b != c) or (a != c)):
    print(3)
else:
    print(0)

#  ИНТЕРПРИТАЦИЯ - НЕБОЛЬШАЯ ВЕРСИЯ

a, b, c = int(input()), int(input()), int(input())

if a == b and b == c:
        print(3)
else:
        print(2)

    # Задача 

a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    print(b)
elif b < a < c:
    print(a)
else:
    print(c)


    #  Задача находит из 3 чисел среднее 

    a = int(input())
b = int(input())
c = int(input())

if a > b and a < c or a < b and a > c:
    print(a)
elif b > a and b < c or b < a and b > c:
    print(b)
elif c > a and c < b or c < a and c > b:
    print(c)


#  Задача считает сколько дней в месяце

month = int(input())

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(31)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
elif month == 2:    
    print(28)

# # 1, 3, 5, 7, 8, 10, 12 месяцы - 31 день
# 4, 6, 9, 11 - 30
# 2 - 28

# ИНТЕРПРТАЦИЯ x = int(input())
if x == 2:
    print(28)
elif (x < 8 and x % 2 == 0) or (x > 7 and x % 2 != 0):
    print(30)
else:
    print(31)


#   Задача на распределение веса 

x = int(input())

if x < 60:
    print("Легкий вес")
elif x >= 60 and x < 64:
    print("Первый полусредний вес")
elif x >= 64 and x < 69:
    print("Полусредний вес")
else:
    print("Мешок")

    #  Мини - КАЛЬКУЛЯТОР 

    a = int(input())
b = int(input())
c = input()

if (a == 0 and b == 0) or (b == 0 and c == ("/")):
    print("На ноль делить нельзя!")
elif c == ("+"):
    print(a + b)
elif c == ("-"):
    print(a - b)
elif c == ("/"):
    print(a / b)
elif c == ("*"):
    print(a * b)
else:
    print("Неверная операция")

    #  комбинация цветов 

    a = input()
b = input()


# можно добавить а ( условно - красный ) а = и ( то и б - красный)
if (a == "красный" and b == "желтый") or (a == "желтый" and b == "красный"):
    print("оранжевый")

elif (a == "красный" and b == "красный"):
    print("красный")

elif (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
    print("фиолетовый")

elif (a == "желтый" and b == "желтый"):
    print("желтый")

elif (a == "синий" and b == "желтый") or (a == "желтый" and b == "синий"):
    print("зеленый")

elif (a == "синий" and b == "синий"):
    print("синий")

else: 
    print("ошибка цвета")

    #  Расчет из 36 на 0, четное и нечетное число по цветам
    x = int(input())

if x == 0:
    print("зеленый")
elif (0 < x <= 10 and x % 2 == 0) or (11 <= x <= 18 and x % 2 != 0) or (19 <= x <= 28 and x % 2 == 0) or (29 <= x <= 36 and x % 2 != 0):
    print("черный")
elif (0 < x <= 10 and x % 2 != 0) or (11 <= x <= 18 and x % 2 == 0) or (19 <= x <= 28 and x % 2 != 0) or(29 <= x <= 36 and x % 2 == 0):
    print("красный")
else:
    print("ошибка ввода")


#  ЗАДАНИЕ ПОВЫШЕННОЙ СЛОЖНОСТИ


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# Находим начало пересечения (аналог max(a1, a2))
if a1 >= a2:
    start = a1
else:
    start = a2

# Находим конец пересечения (аналог min(b1, b2))
if b1 <= b2:
    end = b1
else:
    end = b2

# Проверяем, существует ли пересечение
if start <= end:
    if start == end:
        print(start)  # Пересечение — одна точка
    else:
        print(start, end)  # Интервал
else:
    print("пустое множество")  # Нет пересечения

#  ЗАДАЧА ПО ШАХМАТАМ ( ЧТО БЫ КООРДИТАНА 1 И 2 СОВПАДАЛИ ЦВЕТОМ)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

xy = x1 + y1
xy2 = x2 + y2

if ((xy + xy2) % 2 == 0):
    print("YES")
if ((xy + xy2) % 2 != 0):
    print("NO")

    # ЗАДАЧА НА ЭКЗ

    x = int(input())

if (x % 2 != 0) or (x >= 6 and x <=20 and x % 2 == 0): 
    print("YES")
elif (x > 20 and x % 2 == 0) or (x >=2 and x <= 5 and x % 2 == 0):
    print("NO")
else:
    print("NO")

#  ЗАДАЧА ШАХМАТЫ - СЛОН

x, y = int(input()), int(input())
x2, y2 = int(input()), int(input())

if abs(x - x2) == abs(y - y2):
    print("YES")
else:
    print("NO")

    # Задача для Ферзя

a = int(input())
b = int(input())
x = int(input())
y = int(input())

if abs(a - x) == abs(b - y) or (a == x or b == y):
    print("YES")
else:
    print("NO")

    # оператор float

a = float(input())
b = float(input())
s = (1/2) * (a * b)

print(s)

#  Задача с float

x = float(input())

if x != 0:
    print(1 / x)
    
else:print("Обратного числа не существует")

#  Задача с float

n = float(input())

if n == 1 or n == 2:
    print(n * 10.5)
elif n > 2:
    print((10.5 * 2) + (n - 2) * 4)

    # Задача float

x = float(input()) * 10

y = int(x % 10)

print(y)  

# max (максимальное число из условия)
# min (минимальноеч число из условия)
# float и int могут иметь сравнение == , а с str нет !=
# модуль abs = например abs(-10) == 10. для него имеет место равенство:
# abs|a| = а eсли  a>0 
# abs|a| = а если  a=0 
# abs|a| = а если  a<0 

a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())

x = min(a, b ,c, d, f)
y = max(a, b, c, d, f)
print("Наименьшее число =", x)
print("Наибольшее число =", y)


# Задача 12
a = int(input())
b = int(input())
c = int(input())

f = max(a, b, c)
y = min(a, b, c)
x = (a + b + c) - (f + y)
if a == b == c:
    print(a, b, c, sep="\n")
else:
 print(f, x, y, sep="\n")

#  Задача 21

x = int(input())

x1 = x // 100
x2 = (x % 100) // 10
x3 = x % 10

a = max(x1, x2, x3)
b = min(x1, x2, x3)
f = (x1 + x2 + x3) - (a + b )

if f == a - b:
    print("Число интересное")
else:
    print("Число неинтересное")

    # Задача 1.23
a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())

b = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
print(b)


#  Задача 1.25

a = int(input())
b = int(input())
a2 = int(input())
b2 = int(input())

x = abs(a - a2) + abs(b - b2)
print(x)



#  Задача на соединение строк ( конкатенация строк )

name = input()
family = input()

print("Hello", name, family + "!", "You have just delved into Python")

# Задача 32

a = '''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."'''
print(a)

#  2 вариант 

s1 = '"Python is a great language!", said Fred. "I don'
s2 = "'"
s3 = 't ever remember having this much fun before."'

res = s1 + s2 + s3
print(res)

#  Задача 3.1

x = str(input())

x1 = len(x)
print("Футбольная команда", x, "имеет длину", x1, "символов")
\
# Не сложная, но заеб хаха

a = input()
b = input()
c = input()

a2 = len(a)
b2 = len(b)
c2 = len(c)

if min(a2, b2, c2) == a2 and max(a2, b2, c2) == b2:
    print(a, b, sep = "\n")
elif min(a2, b2, c2) == a2 and max(a2, b2, c2) == c2:
    print(a, c, sep = "\n")
elif min(a2, b2, c2) == b2 and max(a2, b2, c2) == a2:
    print(b, a, sep = "\n")
elif min(a2, b2, c2) == b2 and max(a2, b2, c2) == c2:
    print(b, c, sep = "\n")
elif min(a2, b2, c2) == c2 and max(a2, b2, c2) == a2:
    print(c, a, sep = "\n" )
elif min(a2, b2, c2) == c2 and max(a2, b2, c2) == b2:
    print(c, b, sep = "\n" )


    # Задача из стр преобразовать в лен, узнать будет ли у них арифм прогрессия ( у чисел )

a = len(input())
b = len(input())
c = len(input())

x = max(a, b, c)
y = min(a, b, c)
f = (a + b + c) - (x + y)

if x - f == f - y:
    print("YES")
else: 
    print("NO")

    # Оператор in


    x = "12345678001242156751670"

if "9" in x:
    print("Содержит")
else:
    print("Не содержит")


    # С помощью оператора in мы можем упростить проверяющий, что значение s равно одному символов 'a', 'e', 'i', 'o', 'u':
s = "aeiou"
if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('YES')

# до вида:

if len(s) >= 5 and s in 'aeiou':
    print('YES')


    # С помощью оператора in мы можем проверять наличие сразу нескольких символов в строке.
# Приведённый ниже код:
s = 'Sigma'
print('a' in s)
print('z' in s)
# выводит:
True
False

#    Приведённый ниже код:
print('ab' in 'abc')
print('ac' in 'abc')
# выводит:
True
False

# Приведённый ниже код:
s = 'Alpha'
print('p' in s)
print('P' in s)
# выводит:
True
False

# Задача 

a = input()

if "суббота" in a or "воскресенье" in a:
    print("YES")
else:
    print("NO")


# модуль math ( мини библиотека с операторами )

# sqrt вычисление корня квадратного из двух
# ceil  округление числа вверх
# floor округление числа вниз


#  Задача 1
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

from math import sqrt
a = (x1 - x2)**2
b = (y1 - y2)**2
p = a + b
print(sqrt(p))

#  Задача 2
# pi - число Пи
r = float(input())

from math import pi
s = pi * r**2
c = 2 * pi *r
print(s)
print(c)

# Задача 3 

a = float(input())
b = float(input())
 
from math import sqrt
 
x = ( a + b ) / 2
y = a * b
f = (2 * a * b) / ( a + b)
d = (a**2 + b**2) / 2

print(x)
print(sqrt(y))
print(f)
print(sqrt(d))

# Задача 4

from math import *

i = radians(float(input()))

b = sin(i)
x = cos(i)
y = tan(i) ** 2

a = b + x + y

print(a)

# Задача 5

from math import *
a = float(input())

x = ceil(a)
y = floor(a)

a = x + y
print(a)

#  Задача 6

from math import *

a = float(input())
b = float(input())
c = float(input())

d = b**2 - (4 * a) * c
x1 = 0
x2 = 0
if d < 0:
    print("Нет корней") 

elif d == 0:
    print( - (b / (2 * a))) 
       
elif d > 0:
    x1 = ((-b - sqrt(d)) / (2 * a))
    x2 = ((-b + sqrt(d)) / (2 * a))
    print(min(x1, x2), max(x1, x2), sep = "\n")

# ЗАДАЧА НА СЛОЖНЫЕ ПРОЦЕНТЫ
    m = int(input())
p = int(input())
n = int(input()) - 1
for i in range(n+1):
    a = m * (1 + p/100)**i
    print(i+1, a)
    # ОБЬЯСНЕНИЕ ПОЧЕМУ В УРОВНЕНИЕ В КОНЦЕ СТЕПЕНЬ ** I А НЕ N, то есть условно в конце n = колво дней в целом, 
    # и оно не перечисляет каждый день, допустим n = 6, в каждом значение от 1 до 6 будет значение 6 6 6 6 6 6 ,
    # а надо 1 2 3 4 5 6
    # i, и есть значение 1 2 3 4 5 6 ( в зависимости от range(n например 6))
    # поэтому в уровнение он будет конкретным днем ( а не в целом )



# Использование фор с иф и без иф
a = int(input())
b = int(input())
for l in range(a - 1 + a % 2, b, -2):
    print(l)
    #  с ИФ
m = int(input())
n = int(input())
for m in range(m, n-1, -1):
    if m % 2 != 0:
        print(m)


# Задача 254.1
a = int(input())
b = int(input())
for l in range(a, b+1):
    if l % 17 ==0 or l % 10 == 9 or (l % 3 == 0 and l % 5 == 0):
        print(l)
    else:("")


    # Задача определяет сколько чисел больше 10 
counter = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1
    print('Было введено', counter, 'чисел, больших 10.')
# # Подсчет количества – это очень частый сценарий. Он состоит из двух шагов:
# Создание переменной счетчика, и придание ей первоначального значения: counter = 0;
# Увеличение переменной счетчика на 1
# counter = counter + 1.


#  определяет простое число или составное ( и искл = 1)
num = int(input())
flag = True  # условно если не выполнится команда иф, то число = правда ( уходит в принт )

for i in range(2, num):
    if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False # то есть , если от 2 до num - 1 оно подделится на что -то, то число неправда 
        # ( есть 3 принта, 1 , правда и елсе, как остальное )
if num == 1:
    print('Это единица, она не простая и не составная') 
elif flag == True:
    print('Число простое')
else:
    print('Число составное')


# мини игра 
point = 5 # принтом написать у вас кол-во жизней и число point)
for l in range(10):
    print("Ваше число?")
    a = int(input())
    if a % 2 == 0 and a <= 10 or a > 11:
        point = point - 1
        print(" у вас осталось", point, "жизней")
        


# ЗАДАЧКА 
n = int(input())
a = 1
b = 1
summ = 0
if n >= 1:
    print(a, end=" ")
if n >= 2:
    print(b, end=" ")
if n <= 100 and n >= 3:
    for i in range(2, n):
        summ = a + b
        print(summ, end=" ")
        a, b = b, summ

# Задача 231242
n = int(input())
c = 0
while n > 0:
    if n >= 25:
        b = n // 25
        c += b # сохранили значение поинта при делении на 25
        n -= b*25
    elif n >= 10:
        b = n // 10
        c += b # сохранение значения при делении на 10
        n -= b*10
    elif n >= 5:
        b = n // 5
        c += b # сохранение значения при делении на 5
        n -= b*5
    else:
        c += n
        n = 0
print(c)


# ЗАДАЧА НА НАХОЖДЕНИИ ЦИФРЫ В ЧИСЛЕ (ПРИМЕР 7)
num = int(input())
has_seven = False  # сигнальная метка
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10
if has_seven == True:
    print('YES')
else:
    print('NO') 

#  Задача 10.1
num = int(input())
if num >=9:
    while num >100:
        num //= 10
    num %= 10
    print(num)

    # 23125
    num = int(input())
prev_digit = 0
flag = True
while num !=0:
    digit = num % 10 
    if digit < prev_digit:
        flag = False
    prev_digit = digit
    num //= 10
if flag == True:
    print("YES")
else:
    print("NO")




#АХУЕТИЛЬЕНАЯ ЗАДАЧА 
# данный код решает задачу за 4 секунды
    from math import *
total = 0
flag = False
for a in range(1, 151):
    for b in range(a, 151):
        if a ** 5 + b ** 5 > 150**5:
            break
        for c in range(b, 151):
            if a ** 5 + b ** 5 + c ** 5 > 150**5:
                break
            for d in range(c, 151):
                total = a ** 5 + b ** 5 + c ** 5 + d ** 5
                if total > 150**5:
                    break
                e = round(total ** (1/5))
                if e <= 150 and e**5 == total:
                    print(a + b + c + d + e)
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break
if not flag:
    print("Нет решения")
# интерпритация кода 0 меньше, но больше нагрузки )
# данный код решает задачу почти 4 минуты
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                for e in range(d, 151):      
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a, b, c, d, e)
                        print(a + b + c + d + e)
                        break


# СЛожная задачка по времени
n = int(input())
mid = 1
for i in range(1, n+1):
    digit = 0
    for l in range(1, mid+1):
        if l <= i:
            digit += 1
        else:
            l > i
            digit -= 1
        print(digit, end="")
    print()
    mid +=2
    # ИНТЕРПРИАТАЦИЯ 
    n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print(j+1, end ="")
    for k in range(i-1, 0, -1):
        print(k, end="")
    print()



    # ЕБАНАЯ ЗАДАЧА -- ищет промежуток от а до б вкл, из них ищет число с макс сумм делителей этого числа, вывод числа и сумм
a, b = int(input()), int(input()) # допустим 1 и 5
counter = 0
largest = 0
if a < b: 
    for i in range(a, b+1): # от 1 до 5 включительно ( b + 1)
        total = 0
        for l in range(1, i+1): # вложенный цикл от 1 до 5
            if i % l == 0:
                total += l
        if (total > counter) or (total == counter and i > largest):
                counter = total
                largest = i       
    print(largest, counter)



# Задача на поиск простых чисел из отрезка аб
a = int(input())
b = int(input())
for i in range(a, b+1): 
    total = 0
    for x in range(1, i+1): 
        if i % x == 0:
            total += 1
    if total == 2:
        print("Простые числа", i)
    elif total == 1:
        print("Цифра", 1, "-исключение")
    else:
        total >= 3
        print("Составные числа", i)
    # i(из цикла 1) делим на x ( от 1 до 10)
    # и так 10 раз, то есть 
    # 2 делим на 1 до 10
    # 3 делим на 1 до 10
    # у простых будет делить без остатка 2 раза
    # у составных 3 и более
    # единица искл



    #  Задача на 6 условий
n = int(input())
total_ld = 0
total_3d = 0
total_x = 0
sum_ab = 0
proizv_d = 1
total_fn = 0
last_digit = n % 10
flag = False 
while n > 0:
    digit = n % 10
    if digit == 3:
        total_3d += 1 
    n = n // 10
    
    if last_digit == digit:
        total_ld += 1
    
    if digit % 2 == 0: 
        total_x += 1

    if digit > 5:
        sum_ab += digit

    if digit > 7:
        flag = True  
        proizv_d *= digit

    if digit == 5 or digit == 0: 
        total_fn += 1
print(total_3d)  
print(total_ld)  
print(total_x)
print(sum_ab)
if not flag:  
    print(1)
else: 
    print(proizv_d)
print(total_fn)


#  Задача на получение сумму цифр от числа: 1234 = 1+2+3+4
n = int(input())
last_digit = 0 
total = 0
while n > 0:
    last_digit = n % 10
    total += last_digit
    n //= 10
    print(total)
#  интерпритация , есть через стр переводить в инт
n = input() # вводим строку 1234
s = 0
for i in n:
    s += int(i)
print(s)
#  код на результат одинаковый 

# Задача на проверку, содержит ли ипут число или любой заданный символ 
n = input()
flag = True

for i in n:
    if i in "0123456789":
        flag = False
    
if not flag:
    print("Цифер нет")
else:
    print("Цифра")
#  2 вариант задачи 
s = input()
digits = '0123456789'

for c in s:
    if c in digits:
        print('Цифра')
        break
else:
    print('Цифр нет')



# Задача на нахождение символа в строке 
n = input()
a = "*"
b = "+"
total_a = 0
total_b = 0
for i in n:
    if i in a:
        total_b +=1
    if i in b:
        total_a +=1
print("Символ + встречается ", total_a, "раз")
print("Символ * встречается ", total_b, "раз")
# интерпретация 
s = input()
cnt_plus = 0
cnt_mul = 0

for el in s:
    if el == "+":
        cnt_plus += 1
    elif el == "*":
        cnt_mul += 1

print("Символ + встречается", cnt_plus, "раз")
print("Символ * встречается", cnt_mul, "раз")


#  Задач, считает количество гл и согл букв в тексте 
n = input()
a = "ауоыиэяюеАУОЫИЭЯЮЕ"
b = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
total_a = 0
total_b = 0
for i in range(len(n)-1):
    if n[i] in a:
        total_a += 1
    elif n[i] in b:
        total_b += 1
print("Количество гласных букв равно", total_a)
print("Количество согласных букв равно", total_b)

# нахохдение строки через s(slices) - в переводе, срезы
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])
# 2 интерпритация
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[40:49])

# нахождение по усл задачи
n = input()
ab = len(n)
print(len(n))
print(n*3)
print(n[0])
print(n[0:3])
print(n[-3:])
print(n[::-1])
print(n[1:ab-1]) # or [1:-1]
# 2 тип задачи 
n = input()
ab = len(n)
print(n[2]) #1 третий символ этой строки
print(n[ab-2]) #2 предпоследний символ этой строки
print(n[0:5]) #3 первые пять символов этой строки
print(n[0:ab-2]) #4 всю строку, кроме последних двух символов
print(n[0::2]) #5 все символы с чётными индексами
print(n[1::2]) #6 все символы с нечётными индексами
print(n[::-1]) #7 все символы в обратном порядке
print(n[::-2]) #8 все символы строки через один в обратном порядке, начиная с последнего
# 3 тип задачи 
n = input()
nfx = (len(n) + 1) // 2
sum = n[nfx:] + n[:nfx]    
print(sum)

#  удаляет все значения строки между заданным условие ( ферст h и ласт h)
n = input()
nh_first = n.find("h")
nh_last = n.rfind("h")
print(n[:nh_first] + n[nh_last + 1:])

# код проверяет по заданым условиям, соответсвует ли инпут = задаче
n = input()
n_l = len(n) 
total_a = n.isupper()
fn = "_"
saim = "АВЕКМНОРСТУХ"
if n_l == 9 and total_a and n[6] == fn:
    n_letter = n[0] + n[4] + n[5]
    if n[0] in saim and n[4] in saim and n[5] in saim:  
        n_digit = n[1] + n[2] + n[3] + n[7] + n[8] 
        print("YES" if n_digit.isdigit() else "NO") 
    else:
        print("NO")
elif n_l == 10 and total_a and n[6] == fn:
    n_letter = n[0] + n[4] + n[5]
    if n[0] in saim and n[4] in saim and n[5] in saim:
        n_dig = n[1] + n[2] + n[3] + n[7] + n[8] + n[9]
        print("YES" if n_dig.isdigit() else "NO")    
    else:
        print("NO")
else:
    print("NO")

# код проверяет по заданым условиям, соотвеств ли инп = задаче 
n = input()
nl = len(n)
nt = n.islower()
if n[0] == "@" and (nl >= 5 and nl <= 15) and nt:
    n_s = n[1:].isalpha()
    n_sd = n[1:].isalnum()
    if n_sd == True or n_s == True:
        print("Correct")
    else:
        print("Incorrect")
elif n[0] == "@" and (nl >= 5 and nl <= 15):
    n_d = n[1:].isdigit()
    if n_d == True:
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Incorrect")
# оптимизированный код
n = input()
if (
    n.startswith("@")
    and 5 <= len(n) <= 15
    and n[1:].isalnum()
    and n == n.lower()
    ):
    print("Correct")
else:
    print("Incorrect")

# задача, вес = 100 кг, каждый день нужно - 0.2 
day = int(input()) # день
total = 100 - (i * 0.2) # какой должен быть 
flag = "Что-то пошло не так"
f_wt = float(input()) # вес
if f_wt <= total:
    flag = "Все идет по плану"
    print(flag)
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {f_wt} кг, ЦЕЛЬ по ВЕСУ = {total} кг')
else:
    print(flag)
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {f_wt} кг, ЦЕЛЬ по ВЕСУ = {total} кг')

# к вводимой букве через имп + 1 , то есть а - б, б - в и тд
fn = input() # вводим символ
if fn == "Я":
    print("Дальше букв нет")
if fn != "Я":
    total = ord(fn) + 1
    print(chr(total))

# задача выводит слово с макс суммой его букв по юникоду
il = input()
total = 0
max_word = il
for i in il:
    total += ord(i)
    sum = total
for k in range(3):
    n = input()
    count = 0
    for l in n:
        count += ord(l)
        if count > sum:
            sum = count
            max_word = n
print(max_word)

# находит и заменяет по реплейсу в строке символы англ на русск
text = input()
total_old = 0 
total_new = 0
for i in text:
    total_old += ord(i)
print(f'Старая стоимость: {total_old*3}🐝')
text = text.replace("e", "е")
text = text.replace("y", "у")
text = text.replace("o", "о")
text = text.replace("p", "р")
text = text.replace("a", "а")
text = text.replace("x", "х")
text = text.replace("c", "с")
text = text.replace("E", "Е")
text = text.replace("T", "Т")
text = text.replace("O", "О")
text = text.replace("P", "Р")
text = text.replace("A", "А")
text = text.replace("H", "Н")
text = text.replace("X", "Х")
text = text.replace("C", "С")
text = text.replace("B", "В")
text = text.replace("M", "М")
for l in text:
    total_new += ord(l)
print(f'Новая стоимость:{total_new*3}🐝')
# интерпритация кода, без реплейса
text = input()
eng = "eyopaxcETOPAHXCBM"
rus = "еуорахсЕТОРАНХСВМ"
total_old = 0
total_new = 0
for i in text:
    total_old += ord(i)
    if i in eng:
        eng_find = eng.find(i)
        rus_find = eng_find
        rus_name = rus[rus_find]

        total_new += ord(rus_name) * 3
    else:
        total_new += ord(i) * 3
print(f'Старая стоимость: {total_old*3}🐝')
print(f'Новая стоимость:{total_new*3}🐝')

# задача - шифр Юлия Цезаря
n = int(input()) # число , которым уменьшаем значение символа юникода 
text = input() # текст
total = 0
for i in text:
    total = ord(i) # перебираем символы в цилке фор и даем значение по юникоду
    fn = total - n # значение фн = симлов по условию задачи 
    if fn >= 97:   
        fn = chr(fn)  
        print(fn, end = "")
    else:
        fn = (total - n) + 26
        fn = chr(fn) 
        print(fn, end = "")

# Задача, нахлдит число в виде шифра, и меняет их на символ 
text = input()
for i in range(64):
    unicode = ord("А") + i
    total = f'[u-{unicode}]'
    if total in text:
        text = text.replace(f'[u-{unicode}]', chr(unicode))
    print(text)
# интерпритация 
s = input()
for i in range(32):
    cur_number = ord('а') + i
    cur_writing = f'[u-{cur_number}]'
    cur_letter = chr(cur_number)
    if cur_writing in s:
        s = s.replace(cur_writing, cur_letter)
for i in range(32):
    cur_number = ord('А') + i
    cur_writing = f'[u-{cur_number}]'
    cur_letter = chr(cur_number)
    if cur_writing in s:
        s = s.replace(cur_writing, cur_letter)
print(s)

# сборник задач
n = input()
max_n = n
min_n = n
while True:
    l = input()
    if l == "КОНЕЦ":
        break

    if l < min_n:
       min_n = l 

    if l > max_n:
        max_n = l
print(f'Минимальная строка ⬇️: {min_n}') 
print(f'Максимальная строка ⬇️: {max_n}')
# ее интерпритация 
s = input()
mx_s = s
mn_s = s

while s != 'КОНЕЦ':
    mn_s = min(mn_s, s)
    mx_s = max(mx_s, s)
    
    s = input()
    
print(f'Минимальная строка ⬇️: {mn_s}')
print(f'Максимальная строка ⬆️: {mx_s}')

# сборник задач
text = input()
max_text = text
min_text = text
for i in range(3):
    new_text = input()
    if new_text > max_text:
        max_text = new_text
    if new_text < min_text:
        min_text = new_text
digit = (ord(max_text[-1]) * ord(min_text[-1])) ** 2
print(digit)
# 2
n = int(input())
digit = "0123456789"
letter = "АБВГДЕЖЗИЙКЛМНОП"
for i in range(n):
    nl = input()   
    if len(nl) == 2:
        if nl[0] in digit and nl[1] in letter:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
# 3
a = input()
b = input()
a_n = a.lower()
b_n = b.lower()
text_a = ""
text_b = ""
for i in a_n:
    if i.isalpha(): 
        text_a += i
for l in b_n:
    if l.isalpha():
        text_b += l
if text_a == text_b:
    print("YES")  
else:
    print("NO")
# 4
a, b , c = input(), input(), input()
max_n = max(a, b, c)    
min_n = min(a, b, c)
middle = ""
if a != max_n and a != min_n:
    middle = a
elif b != max_n and b != min_n:
    middle = b
elif c != max_n and c != min_n:
    middle = c
print(min_n, middle, max_n)
# 5
n = int(input())
text = input() # первая строчка

first_d = text.find(" ") 
total = text[0:first_d] # фамилия автора 
first_l = text.find("«") 
prod_l = text[first_l:] # название кнги
    
flag = True

for i in range(n - 1):
    text_n = input() #строки
    fn_digit = text_n.find(" ") 
    total_n = text_n[0:fn_digit] # фамилии авторов
    first_i = text_n.find("«") 
    prod_i = text_n[first_i:] # названия книг

    if total > total_n:
        flag = False
        break 
    elif total == total_n:
        if prod_l > prod_i:
            flag = False
            break
    total,prod_l = total_n, prod_i
if flag:
    print("YES")
else:
    print("NO")
# 6
text = input()
for i in range(len(text)):
    if i % 3 == 0:
        continue
    print(text[i], end = "")
# 7
n = input()
f_digit = n.find("h")
l_digit = n.rfind("h")

res = n[:f_digit] + n[l_digit: f_digit: -1] + n[l_digit:]
print(res)
# 8списки
n = int(input())
total = ""
for i in range(n):
    total += chr(ord("a") + i)
print(list(total))
# интерпритация 
n = int(input())
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(abc[0 : n])
# 9 cписки
n = int(input())
total = list(range(1, n, 2))
print(total)
# 10 списки + срезы
n = input()
go = list(n)
print(go[0::2])
# 11 cписки 
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
total = 0
s = []
for i in primes:
    total += 1
    if total <= 6:
        s.append(i)
print(s)
# интерпритация 
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[:6])
# 12 методы списков
open = []
for i in range(1, 27):
    open.append(chr(96 + i) * i)
print(open)
# 13 методы списков 
n = int(input()) # кол-во итераций в цилке
nd = int(input()) # первое число 
open = []
for i in range(n-1):
    nf = int(input()) # второе, третье и n! число 
    sum = nd + nf
    open.append(sum)
    nd = nf
print(open)
# интерпритация кода
seq = []
for _ in range(int(input())):
    seq.append(int(input())) 
res = []
for i in range(len(seq) - 1):
    res.append(seq[i] + seq[i+1])
    
print(res)
# 14 методы строк
n = int(input())
take = []
for i in range(n):
    text = input()
    take.append(text) # список
k = int(input()) # индекс необходимой буквы
res = ""
for l in take: # цикл выполняется = кол-ву в списке
    if len(l) >= k:
        res += l[k-1]
print(res)
# вывод элементов
numbers = [1, 3, 0, 2, 4]
for i in numbers:
    print(numbers[i], end=' ')
# Код выведет: `3 2 1 0 4`  
# Пошаговое объяснение:
# 1. Список `numbers = [1, 3, 0, 2, 4]` имеет индексы от `0` до `4` и значения:  
#    - `numbers[0] = 1`  
#    - `numbers[1] = 3`  
#    - `numbers[2] = 0`  
#    - `numbers[3] = 2`  
#    - `numbers[4] = 4`  
# 2. Цикл `for i in numbers:` перебирает значения списка (не индексы!):  
#    - Первая итерация: `i = 1` → `numbers[1] = 3` → вывод `3`  
#    - Вторая итерация: `i = 3` → `numbers[3] = 2` → вывод `2`  
#    - Третья итерация: `i = 0` → `numbers[0] = 1` → вывод `1`  
#    - Четвёртая итерация: `i = 2` → `numbers[2] = 0` → вывод `0`  
#    - Пятая итерация: `i = 4` → `numbers[4] = 4` → вывод `4`  
# 3. Итог:  
#    Значения выводятся в порядке обработки: `3 2 1 0 4`.   
# задача 15
n = int(input())
take = []
for num in range(n):
    digit = int(input())
    take.append(digit)

# Находим индексы
max_idx = take.index(max(take))
min_idx = take.index(min(take))

# Удаляем сначала больший индекс
if max_idx > min_idx:
    del take[max_idx]
    del take[min_idx]
else:
    del take[min_idx]
    del take[max_idx]

print(*take, sep='\n')
# задача 16
n = int(input()) 
take = []
for i in range(n):
    text = input().strip()
    take.append(text)

fn = input().lower()
res = []

for l in take:
    if fn in l.lower():
        res.append(l) 
    else:
        print("")
        
print(*res, sep='\n') 
# задача 17 ++++
n = int(input()) # кол - во строк
take = [] # список 

for i in range(n): # цикл = кол - ву строк 
    text = input() # строки 
    take.append(text) # заносим их в список
digit = int(input()) # кол - во принимаемых слов 
res = [] # список 

for l in range(digit): # цикл = кол - ву принимаемых слов
    fn = input().lower() # принимаемые условием слова
    res.append(fn) # заносим в список

for text in take:
    new_text = text.lower() # заносим строки в нижний регист 
    flag = True

    for g in res: # берет список ( язык и питон )
        if g not in new_text: # (g = язык and g = питон [0, 1] если нет одного из слов
            flag = False # флаг становится фолс
            break # цикл заканчиваем 
    if flag: # если цикл принимает тру флаг 
        print(text) # печатает строку оригинал

# задача 18
n = int(input())
digit_z = []
digit_x = []
digit_c = []
res = []
for i in range(n):
    digit = int(input())

    if digit < 0:
        digit_z.append(digit)

    if digit == 0:
        digit_x.append(digit)

    if digit > 0:
        digit_c.append(digit)

res.extend(digit_z)
res.extend(digit_x)
res.extend(digit_c)
print(res)

# задача 19 - методы строк сплит и джоин
n = input()
s = n.split()
total = ""
for i in s:
    total += i[0]
    res = (".".join(total))
print(res, end =".")
# интерпритация с двойной индексеция
full_name = input().split()
print(full_name[0][0], full_name[1][0], full_name[2][0], sep=".", end=".")

# 20 
text = input()
total = text.split("\\")
print(*total, sep='\n')

# 21
text = input().split()
res = ""
for i in text:
    res = int(i) * "+"
    print(res)

# 22 
n = input().split(".")
for i in n:
    if int(i) > 255:
        print("НЕТ") 
        break   
else:
    print("ДА")

# 23 
text = input()
letter = input()
res = letter.join(text)
print(res)

# 24 +
n = input().split()
total = 0
for i in range(len(n)):
    for l in range(i+1, len(n)):
        if n[i] == n[l]:
            total += 1
print(total)

# 25
numbers = [8, 9, 10, 11]

del numbers[1]
numbers.insert(1, 17) # 1 задание 
 
numbers.extend([4, 5, 6]) # 2 задание

del numbers[0] # 3 задание

numbers.extend(numbers) # 4 задание

numbers.insert(3, 25) # 5 задание 

print(numbers) 
# 26
numbers = [8, 9, 10, 11]
one_numbers = numbers.copy()
two_numbers = numbers.copy()
three_numbers  = numbers.copy()
four_numbers  = numbers.copy()
five_numbers = numbers.copy()

numbers.insert(1, 17)
print(numbers) # 1 задание 

one_numbers.append(4)
one_numbers.append(5)
one_numbers.append(6)
print(one_numbers) # 2 задание 

del two_numbers[0] # or two_numbers.remove(8)
print(two_numbers) # 3 задание

three_numbers.extend(three_numbers)
print(three_numbers) # 4 задание 

four_numbers.insert(3, 25)
print(four_numbers) # 5 задание

print(five_numbers) # 6 задание

# 27 задание 
seq = []
for l in input().split():
    seq.append(int(l))
    maximum = seq.index(max(seq))
    minimum = seq.index(min(seq))
seq[maximum], seq[minimum] = seq[minimum], seq[maximum]
print(*seq)
# интерпритация 
n =[int(s) for s in input().split()]


maximum = n.index(max(n))
minimum = n.index(min(n))

n[maximum], n[minimum] = min(n), max(n)
print(*n)

# 28 задание 
n = input().lower().split()
total = 0
total += n.count("a")
total += n.count("the")
total += n.count("an")
print("Общее количество артиклей:", total)

# 29 задание 
digit_str = input()
seq = (int(digit_str[1:])) # кол - во строк
slice = 0
for i in range(seq):
    text = input()
    if "#" in text:
        slice = text.index("#")
        text = text[0:slice]   
    print(text.rstrip())

# 30 задание
n = int(input())
res = []
for x in range(n):
    text = input()
    res.append(text)
    res.sort()
print(*res, sep='\n')

# дпо
numbers = []
for i in range(1, 5):
    for j in range(2):
        numbers.append(i * j)
print(numbers)
# интерпритация
numbers = [i * j for i in range(1, 5) for j in range(2)]
print(numbers)

# дпо
# Списочное выражение	Результирующий список
[0 for i in range(10)] # РЕЗУЛЬТАТ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[i ** 2 for i in range(1, 8)] # РЕЗУЛЬТАТ [1, 4, 9, 16, 25, 36, 49]
[i * 10 for i in numbers] # РЕЗУЛЬТАТ [10, 140, 50, 90, 120]
[c * 2 for c in word] # РЕЗУЛЬТАТ ['HH', 'ee', 'll', 'll', 'oo']
[m[0] for m in word] # РЕЗУЛЬТАТ ['o', 't', 't', 'f', 'f', 's']
[i for i in numbers if i < 10] # РЕЗУЛЬТАТ [1, 5, 9]
[m[0] for m in word if len(m) == 3] # РЕЗУЛЬТАТ ['o', 't', 's']
# ПРИ word = 'Hello'numbers = [1, 14, 5, 9, 12]words = ['one', 'two', 'three', 'four', 'five', 'six']

# задача 31
print(*(el for el in input() if el.isdigit()), sep='')
# задача 32
print(*(int(el)**2 for el in input().split() if int(el) % 2 == 0 and int(el)**2 % 10 != 4))


# задача 33
a = input()
n = len(a)
res = []
for i in range(n - 1):
    min_digit = a.index(min(a))
    res.append(a.pop(min_digit))
print(res)
# интерпритация кода
n = len(a)
for i in range(n):
    mx_ind = n - 1 - i
    for j in range(n - i):
        if a[j] > a[mx_ind]:
            mx_ind = j

    a[n - 1 - i], a[mx_ind] = a[mx_ind], a[n - 1 - i]
print(a)

# ЭКККККККККККЗЗЗЗЗЗЗЗААААААААААААММММММММММММЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕН
res = []
m = [int(seq) for seq in input().split()]
l = [int(jf) for jf in input().split()]
for i in range(len(m)):
    res.append(m[i] + l[i])
print(*res)

# задача с экзамена 
total = 0
n = [int(el) for el in input().split()]
res = []
for digit in n:
    total += digit
    res.append(str(digit))
write = "+".join(res)
print(f'{write}={total}')
# интерпритация 
numbers = [int(number) for number in input().split()]
print(*numbers, sep='+', end=f'={sum(numbers)}')

# задача с экзамена 
text = [el for el in input().split()]
res = 0
for i in text:
    if len(i) > res:
        res = len(i)
print(res)
# интерпритация 
lens = [len(el) for el in input().split()]
print(max(lens))

# задача с экзамена 
text = [el[1:] + el[0] + "ки" for el in input().split()]
print(*text)

# задача с экзамена ++
n = input()
fn = []
new_text = n.replace("-","")
if not new_text.isdigit():
    print("NO")
else:
    eq = n.split("-")
    for i in eq: 
        fn.append(len(i))
    if fn == [3, 3, 4] or eq[0] == "7" and fn == [1, 3, 3, 4]:
        print("YES")
    else:
        print("NO")

# задача с функцией def
def draw_box():
    print("*" * 10)

    for i in range(12):
       print("*", "*" , sep = " " * 8)

    print("*" * 10)

draw_box() 
# интерпритация 
def draw_box():
    print("**********")
    for i in range(12):
        print('*', '*',sep = " " * 8)
    print("**********")
print()

# 2 задача 

# объявление функции
def draw_triangle():
    
    for i in range(1, 11):  
        print(i * "*")     

# основная программа
draw_triangle()  # вызов функции

# 3 задача 
def draw_f(a, b):
    for i in range(a):
        print("*" * b)

draw_f(10**2,10**2)
def draw_f(a, b):
    for i in range(a):
        print("*" * b)

draw_f(10**2,10**2)

# 4 задача 
def draw_triangle(fill, base):
    for i in range(1, (base + 2) // 2):
        print(fill * i)
    
    for l in range((base - 1) // 2, base):
        print(fill * (base - l))

fill = input()
base = int(input())

draw_triangle(fill, base)

# 5 задача 
def print_fio(name, surname, patronymic):
    full_name = (surname[0] + name[0] + patronymic[0]).upper()
    print(full_name)
name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)
#  интерпритация 
def print_fio(name, surname, patronymic):  
        print(name[0], surname[0], patronymic[0], sep='')
name, surname, patronymic = input().upper(), input().upper(), input().upper()
print_fio(surname, name,  patronymic)

# 6 задача def and return
def convert_to_miles(km):
    res = km * 0.6214
    return round(res, 4)

num = int(input())
print(convert_to_miles(num))
# 7 задача 
def get_days(month):   
    return mon[month - 1]
        

mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
num = int(input())
print(get_days(num))
# интерпритация 
def get_days(month):
   if month == "2":
    return 28
   elif month <= 7 and month % 2 != 0 or month >= 8 and month % 2 == 0:
    return 31
   else:
    return 30
   
num = int(input())
print(get_days(num))

# 8 задача 
# объявление функции
def get_factors(num):
    res = []
    for i in range(1, num+1):
        if num % i == 0:
            res.append(i)
    return res 

n = int(input())
print(get_factors(n))
# 9 задача 
def factor_number(num):
    total = 0
    for i in range(1, num+1):
        if num % i == 0:
            total += 1
    return total

n = int(input())
print(factor_number(n))
# 10 задача 
def find_all(target, symbol):
    res = []
    for el in range(len(target)):
        if target[el] == symbol:
            res.append(el) 
    return res       

s = input()
char = input()
print(find_all(s, char))
# 11 
def merge(list1, list2):
    total = list1 + list2 
    total.sort()
    return total
    

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))
# 
#   
# 
# 
# не задача а пиздец 
def merge(lst):
    lst.sort() 
    return lst

ls = []
for i in range(int(input())):
    text = [int(el) for el in input().split()]
    ls.extend(text)
    
resultat = merge(ls)
print(*resultat)
# интерпритация 
# берём из теории уже реализованную функцию быстрой сортировки
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока ни один из списков не закончился
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    
    return result

# принимаем кол-во строк
n = int(input())

# формируем из первой строки список чисел и возьмём
# этот первый список за основу для результирующего списка
res = [int(num) for num in input().split()]

# принимаем n - 1 строк (потому что первую строку мы уже приняли)
for _ in range(n - 1):
    # принимаем текущую строку и формируем из неё список чисел
    cur_list = [int(num) for num in input().split()]
    
    # объединяем результирующий список и текущий список
    # и записываем этот новый отсортированный список в качестве
    # результирующего списка
    res = quick_merge(res, cur_list)

# выводим результирующий список
print(*res)

# задача 13
# объявление функции
def is_valid_triangle(side1, side2, side3):
    sum_s = [side1, side2, side3]
    sum_s.sort()
    
    return (
        sum_s[0] + sum_s[1] > sum_s[2]
    )

a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))
# интерпритация 
def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False


a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))

# 14 задача 
def is_prime(num):
    res = []
    for el in range(1, num+1):
        if num % el == 0:
            res.append(el)
    if len(res) == 2:
        return True
    else:
        return False
# считываем данные
n = int(input())
# вызываем функцию
print(is_prime(n))

# 15 задача 
def next_deg_prime(number):
    next_num = number + 1
    while True:
        res = []
        for i in range(1, next_num+1):
            if next_num % i == 0:
                res.append(i)
        if len(res) == 2:
            return next_num
        else:
            next_num += 1

n = int(input())
print(next_deg_prime(n))
# интерпритация
def is_prime(num):
    if num == 1:
        return False  # число 1 не является простым

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # сразу возвращает False, когда находим делитель

    return True

def get_next_prime(num):
    cur_num = num + 1  # начинаем искать следующее простое число

    while not is_prime(cur_num):  # если следующее число непростое, то увеличиваем на 1
        cur_num += 1

    return cur_num
n = int(input())
print(get_next_prime(n))
# задача 16
# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    f_n = 0 # верхний регистр 
    s_n = 0 # нижний регистр
    n_total = 0 # наличие цифры
    for el in password:
        
        if el.isupper():
            f_n += 1
        if el.islower():
            s_n += 1
        if el.isdigit():
            n_total += 1
    return f_n >= 1 and s_n >= 1 and n_total >= 1

txt = input()
print(is_password_good(txt))

# задача 17
# объявление функции
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count_n = 0
    for el in range(len(word1)):
        if word1[el] == word2[el]:
            count_n += 1
    return count_n == len(word1) - 1
       
txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))

# задача 18 
# заголовок функции 
def is_palindrome(text):
# тело функции
    total = ""
    for el in text:
        if el.isalpha():
            total += el
    return total == total[::-1]
       
# основная часть функции 
text = input().lower()
# вызов функции 
print(is_palindrome(text))

# задача 19
# большой код!!!
# большой код!!!
# большой код!!!
# большой код!!!
# большой код!!!
# большой код!!!
# большой код!!!
# большой код!!!
# первая функция "a" == число палиндром
def is_palindrome(text):


    total = ""
    for el in text:
        total += el
    return total == total[::-1]

# вторая функция "b" == простое число
def is_prime(num):
    res = []
    for el in range(1, num+1):
        if num % el == 0:
            res.append(el)
    if len(res) == 2:
        return True
    else:
        return False
    
# объявление функции
def is_valid_password(password):
    new_text = password.split(":")
    if len(new_text) != 3:
        return False
    a = new_text[0]
    b = int(new_text[1])
    c = int(new_text[2])
    return is_palindrome(a) and is_prime(b) and c % 2 == 0
        
# считываем данные
psw = input()
# вызываем функцию
print(is_valid_password(psw))

# задача 20
# объявление функции
def is_correct_bracket(text):
    one_count = 0
    for el in txt:
        if one_count < 0:
            return False
        if el == "(":
            one_count += 1
        if el == ")":
            one_count -= 1
    if one_count == 0:
        return True
    else:
        return False
     

# считываем данные
txt = input()
# вызываем функцию
print(is_correct_bracket(txt))

# задача 21
# объявление функции
def convert_to_python_case(text):
    res = ""
    res += (text[0].lower())

    for el in text[:1]:
        if el.isupper():
            res += ("_" + el.lower())
        else:
            res += (el)
    return res

# считываем данные
txt = input()
# вызываем функцию
print(convert_to_python_case(txt))

# задача 22
# объявление функции
def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())
# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

# задача 23 
# объявление функции
from math import *
def get_circle(radius):
    c = radius * (2 * pi)
    s = pi * (radius ** 2)
    return c, s


# считываем данные
r = float(input())
# вызываем функцию
length, square = get_circle(r)
print(length, square)

# задача 24 
from math import *
# объявление функции
def solve(a, b, c):
    d = b**2 - (4 * a) * c
    x1_new = (-b - sqrt(d)) / (2 * a)
    x2_new = (-b + sqrt(d)) / (2 * a)
    return x1_new, x2_new


# считываем данные
a, b, c = int(input()), int(input()), int(input())
# вызываем функцию
x1, x2 = solve(a, b, c)
print(min(x1, x2), max(x1,x2))

# задача 25
from math import *
# объявление функции
def compute_binom(n, k):
    resultat = factorial(n) // (factorial(k) * (factorial(n - k)))
    return (resultat)


# считываем данные
n = int(input())
k = int(input())
# вызываем функцию
print(compute_binom(n, k))

# задача 26
# объявление функции
def is_pangram(text):
    total = 0
    res = ['a', 'b', 'c', 'd', 'e', 'f', 
           'g', 'h', 'i', 'j', 'k', 'l', 
           'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for el in text:
        if el in res:
            res.remove(el)
            total += 1
    if total == 26:
        return True
    else:
        return False
    

# считываем данные
text = input().lower()
# вызываем функцию
print(is_pangram(text))

# задача 27
# объявление функции
def is_magic(date):
    new_date = date.split(".")
    f_n = int(new_date[0]) * int(new_date[1])
    f_s = int(new_date[2]) % 100
    if f_n == f_s:
        return True
    else:
        return False


# считываем данные
date = input()
# вызываем функцию
print(is_magic(date))

# задача 28
# объявление функции
def get_month(language, number):
    lng_en = ['january', 'february', 'march', 'april', 
          'may', 'june', 'july', 'august', 
          'september', 'october', 'november', 'december']
    lng_ru = ['январь', 'февраль', 'март', 'апрель',
           'май', 'июнь', 'июль', 'август', 
           'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    if language == "ru":
        return lng_ru[number - 1]
    else:
        return lng_en[number - 1]

# считываем данные
lan = input()
num = int(input())
# вызываем функцию
print(get_month(lan, num))

# задача 29 
from math import *

def number_digit(num):
    return ceil(log2(num)) if num > 1 else 1

n = int(input())
print(number_digit(n+1))

# задача 30
def na_easy(num, num2):
    summ = num + num2
    raz = num - num2
    proz = num * num2
    chast = num / num2
    delen = num // num2
    ost = num % num2
    koren = (num**10 + num2**10) ** 0.5
    return summ, raz, proz, chast, delen, ost, koren


one_n = int(input())
two_n = int(input())
print(*na_easy(one_n, two_n), sep='\n')

# задача 1
def total_sale(write):
    digit = len(write)
    total = (digit * 60) / 100
    one = int(total)
    two = (digit * 60) % 100
    return (f'{one} р. {two} коп.')


text = input()
print(total_sale(text))
# задача 2
def digit_word(n):
    return len(n)


text = input().split()
print(digit_word(text))

# задача 3 
# обьявляем функцию
def zodiac(n):
    # тело функции
    sl = ['Обезьяна', 'Петух', 'Собака', 
          'Свинья', 'Крыса', 'Бык', 
          'Тигр', 'Заяц', 'Дракон', 
          'Змея', 'Лошадь', 'Овца']
    
    return sl[n % 12]


# считываем данные
fn = int(input())
# выводим результат
print(zodiac(fn))

# задача 4
# обьявляем функцию
def revers_digit(tol):
# тело функции
    if len(tol) == 5:
        return int(tol[::-1])
    else:
        one = tol[:1]
        two = tol[1:]
        return one + two[::-1]
    

# считываем данные
esq = input()
# выводим результат
print(revers_digit(esq))

# задание 5
def form_stroka(ewq):
    return (f'{ewq: ,}')


text = int(input())
print(form_stroka(text))

# задание 6
n = int(input())
k = int(input())     
res = 0        
for el in range(1, n+1):
    res = ( res + k) % el 

print(res + 1)

# задание 7 
def coordinata(x , y, seq):
    if x > 0 and y > 0:
        seq[0] += 1
    elif x < 0 and y > 0:
        seq[1] += 1
    elif x < 0 and y < 0:
        seq[2] += 1
    elif x > 0 and y < 0:
        seq[3] += 1

seq = [0, 0, 0, 0]   


for i in range(int(input())):
     x, y = map(int, input().split())
     coordinata(x, y, seq)

print(f'Первая четверть: {seq[0]}')
print(f'Вторая четверть: {seq[1]}')
print(f'Третья четверть: {seq[2]}')
print(f'Четвертая четверть: {seq[3]}')

# задача 8
def bg_pred(total):
    count = 0
    for el in range (1, len(total)):
        if total[el] > total[el - 1]:
            count += 1
    return count

digit = list(map(int, input().split()))
print(bg_pred(digit))

# задача 9

def back_forw(text):

    for i in range(0, len(text) - 1, 2):
        text[i], text[i+1] = text[i+1],  text[i]
    return text


tx = input().split()
print(*back_forw(tx))
# интерпритация 
def element(text):
    n = []
    for el in text:
        if el not in n:
            n.extend(el)
    return n


seq = input().split()
print(len(element(seq)))

# задача 10 
def proizvedenie_digit(my_seq, my_target):
    n = len(seq)
    for i in range(n):
        for l in range(n):
            if i != l and my_seq[i] * my_seq[l] == my_target:
                return ("ДА") 
    return ("НЕТ") 


seq = []
n_count = int(input())
for el in range(n_count): 
    text = int(input())
    seq.append(text)

target = int(input())
print(proizvedenie_digit(seq, target))

# задача 11

def fight(one_t, two_r):
    k = "камень"
    b = "бумага"
    n = "ножницы"
    if one_t == two_r:
        return("ничья")
    if one_t == k and two_r == n or one_t == b and two_r == k or one_t == n and two_r == b:
        return("Тимур")
    else:
        return("Руслан")


timur = input()
ruslan = input()
print(fight(timur, ruslan))
# интерпритация
moves = ["камень", "ножницы", "бумага"]
outcomes = ["ничья", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

difference = moves.index(timur_move) - moves.index(ruslan_move)
result = outcomes[difference]

print(result)

# задача 12
def fight(timur, ruslan):
    moves = ["камень", "ножницы", "бумага", "ящерица", "спок"]
   
    if timur == ruslan:
        return "ничья"
    
    rules = {
        "камень": ["ножницы", "ящерица"],    
        "ножницы": ["бумага", "ящерица"],     
        "бумага": ["камень", "спок"],         
        "ящерица": ["бумага", "спок"],        
        "спок": ["камень", "ножницы"]         
    }
    
    if ruslan in rules[timur]:
        return "Тимур"
    else:
        return "Руслан"

timur = input()
ruslan = input()
print(fight(timur, ruslan))

# задача 13
for i in range(1, int(input()) + 1):
    s = input()
    
    a = s.find('a', 0)
    n = s.find('n', a)
    t = s.find('t', n)
    o = s.find('o', t)
    n = s.find('n', o)
    
    if o != -1 and n != -1:
        print(i, end=' ')

# задача 14
seq = ['а', 'б', 'в', 'г', 'д', 'е',     
     'ж', 'з', 'и', 'й', 'к', 'л', 
     'м', 'н', 'о', 'п', 'р', 'с', 
     'т', 'у', 'ф', 'х', 'ц', 'ч', 
     'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

word = input() + ' запретил букву'

for letter in seq:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '')
        word = ' '.join(word.split())

# задача 15
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for el in list1:
    counter += len(el)
    for i in el:
        total += i
res = total / counter
print(res)

# задача 16
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for elem in row:
        print(elem, end=' ')
    print()
# интерпритация кода 16 - выводит [0] каждого списка, затем [1] и [2]
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[j][i], end=' ')  # выводим my_list[j][i] вместо my_list[i][j]
    print()

# задача 17
n = int(input())

for el in range(n):
    my_list = [i for i in range(1,n+1)]
    print(my_list)

# задача 18
n = int(input())
for el in range(1,n+1):
    res = [i for i in range(1, el+1)]
    print(res)

# задача 19 
def pascal(il):
    total = []
    for i in range(0, il+1):
        for l in range(i):
            total.append(l)
    return total

n = int(input())
print(pascal(n))
# задача 20
def pascal(il):


    seq = []
    for i in range(0, il+1):
        row = []
        for l in range(i + 1):
            if l == 0 or l == i:
                row.append(1)
            else:
                row.append(seq[i-1][l-1] + seq[i-1][l])
        seq.append(row) 

    return seq 


n = int(input())
print(pascal(n))
# задача 21
def pascal(il):


    seq = []
    for i in range(0, il):
        row = []
        for l in range(i + 1):
            if l == 0 or l == i:
                row.append(1)
            else:
                row.append(seq[i-1][l-1] + seq[i-1][l])
        seq.append(row) 

    return seq 


n = int(input())
for sg in pascal(n):
    print(*sg)

# задача 22
def pack_dublle(text):
    res = [[text[0]]]
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            res[-1].append(text[i])
            
        else:
            res.append([text[i]])
    return res      

 
el = input().split()
print(pack_dublle(el))

# задача 23
def chanked(text, targ):

    res = []
    for el in range(0, len(text), targ):
        res.append(text[el:el+targ])

    return res

write = input().split()
target = int(input())
print(chanked(write, target))
# .keys() - получить ключи
# .values() получить значение
# .items() - получить ключ и значение 
# .update(словарь) - добавить словарь ( обновить - дополнить )
# .setdefault(key, or values,items[, default]) (вывести значение, а если ключа нет, дать ему обозначение в default - например число)
# clear() - удалить словарь ( такой же , как и в списке метод )

# метод del удаляет ключ и его значение, метод pop если есть переменная, удаляет ключ и присваивает ей значение 
# вернет 3 значения

# # 1 
phone_book = {}
phone_book['Стефанн'] = '8-111-222-33-44'
phone_book['Серёга'] = '8-222-333-44-55'
phone_book['Юра'] = '7-900-222-44-55'

text = input(f'Выберите один из следующих контактов {list(phone_book.keys())}: ')
if text not in phone_book:
    print("Абонент не найден")
else:
    print(f'Телефон абонента {phone_book[text]}')

print(f"Весь список контактов: {phone_book}")

# 2
product = {"name": "iPhone", "price": 1000, "in_stock": True}
print("Актуальные ключи")
for key in product:
    print(key)
print("Актуальные данные ключей")
for value in product.values():
    print(value)
for key,value in product.items():
    print(f'Ключ:{key}, Значение:{value}')
print("Новые изменения в данных телефона")
product['price'] *= 1.10
product["in_stock"] = False

print(f'Актуальный статус телефона: {product}')

# 3
text = input("Пожалуйста, введите строку: ")
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)


# словарь dict() не упорядоченная последовательность, состоит из ключа и значения
# имеет следующие методы:
# keys() - получить ключи
# get()
# .values() получить значение
# .items() - получить ключ и значение 
# .update(словарь) - добавить словарь ( обновить - дополнить )
# .setdefault(key, or values,items[, default]) (вывести значение, а если ключа нет, дать ему обозначение в default - например число)
# clear() - удалить словарь ( такой же , как и в списке метод )
# del()

# список list() - упорядоченная последовательность,

# множество set() не упорядоченная последовательность, имеет только уникальные элементы
# add() добавление одного элемента
# update() добавление нескольких элементов другой коллекции
# revome() удаление элемента по значение( может выдать ошибку )
# discard() безопасное удаление (ошибки не будет)
# random_element = my_set.pop() #  Удаление и возврат случайного элемента (из-за неупорядоченности)
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# обьединение:
# union_set = a | b или a.union(b) -> {1, 2, 3, 4, 5, 6}

# Пересечение: (элементы, которые есть и в a, и в b)
# intersection_set = a & b или a.intersection(b) -> {3, 4}    

# Разность: (элементы, которые есть в a, но нет в b)
# difference_set = a - b или a.difference(b) -> {1, 2}

# # Симметрическая разность: (элементы, которые есть только в одном из множеств)
# sym_diff_set = a ^ b # или a.symmetric_difference(b) -> {1, 2, 5, 6}

# кортеж tuple()
# поддерживает канкетанацию, повторение строки через умножение, и несколько методов:
# коунт, индекс, срезы и лен
# срезы поддерижвает так как является 
# упорядоченной последовательностью( как и список) - этим они похожи