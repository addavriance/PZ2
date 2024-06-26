# Практические задания по Python

Этот репозиторий содержит практические задания, выполненные в рамках изучения языка Python.

## Структура проекта

- `PZ_2` - содержит задания на базовом уровне, в основном по программированию на Python.
  - `PZ-*` - Python пакеты с решениями задач.
- `assets` - вспомогательные файлы для заданий.
- `reports` - отчеты по некоторым заданиям.
- `Отчет_E.docx` - пример отчета.
- `Регулярки.docx` - дополнительные материалы.

## Описание задач

### ПЗ №2

Дано трехзначное число. В нем зачеркнули первую справа цифру и приписали ее слева. Вывести полученное число.

Решение - [pz-2.py](https://github.com/addavriance/PZ2/blob/main/PZ_2/pz-2.py)<br>
Отчет - [Отчет_pz2.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz2.pdf)

### ПЗ №3

Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара совпадающих».

Решение - [pz-3.py](https://github.com/addavriance/PZ2/blob/main/PZ_3/pz-3.py)<br>
Отчет - [Отчет_pz3.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz3.pdf)

### ПЗ №3.2

Даны две переменные целого типа: А и В. Если их значения не равны, то присвоить каждой переменной сумму этих значений, а если равны, то присвоить переменным нулевые значения. Вывести новые значения переменных А и В.

Решение - [pz-3-2.py](https://github.com/addavriance/PZ2/blob/main/PZ_3/pz-3-2.py)<br>
Отчет - [Отчет_pz3.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz3.pdf)

### ПЗ №4

Дано вещественное число Х и целое число N (> 0). Найти значение выражения ((-1) ** N) * (X ** (2 * N + 1)) / !(2 * N + 1) (N > 12 ...). Полученное число является приближенным значением функции sin в точке Х.

Решение - [pz-4.py](https://github.com/addavriance/PZ2/blob/main/PZ_4/pz-4.py)<br>
Отчет - [Отчет_pz4.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz4.pdf)

### ПЗ №4.2

Дано целое число N (> 0). Найти сумму 1^N + 2^N-1 + ... + N^N-i.

Решение - [pz-4-2.py](https://github.com/addavriance/PZ2/blob/main/PZ_4/pz-4-2.py)<br>
Отчет - [Отчет_pz4.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz4.pdf)

### ПЗ №5

Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится нуль?

Решение - [pz_5.py](https://github.com/addavriance/PZ2/blob/main/PZ_5/pz_5.py)<br>
Отчет - [Отчет_pz5.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz5.pdf)

### ПЗ №5.2

Описать функцию ShiftLeft3(A, В, С), выполняющую левый циклический сдвиг: значение А переходит в С, значение С - в В, значение В - в А (A, B, С - вещественные параметры, являющиеся одновременно входными и выходными). С помощью этой функции выполнить левый циклический сдвиг для двух данных наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).

Решение - [pz_5_2.py](https://github.com/addavriance/PZ2/blob/main/PZ_5/pz_5_2.py)<br>
Отчет - [Отчет_pz5.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz5.pdf)

### ПЗ №6

Дан список размера N и целые числа К и L (1 < К < L < N). Найти сумму элементов списка с номерами от К до L включительно.

Решение - [pz-6.py](https://github.com/addavriance/PZ2/blob/main/PZ_6/pz-6.py)<br>
Отчет - [Отчет_pz6.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz6.pdf)

### ПЗ №6.1

Дан целочисленный список размера N. Найти количество различных элементов в данном списке.

Решение - [pz-6-1.py](https://github.com/addavriance/PZ2/blob/main/PZ_6/pz-6-1.py)<br>
Отчет - [Отчет_pz6.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz6.pdf)

### ПЗ №6.2

Дан список размера N, все элементы которого, кроме последнего, упорядочены по возрастанию. Сделать список упорядоченным, переместив последний элемент на новую позицию.

Решение - [pz-6-2.py](https://github.com/addavriance/PZ2/blob/main/PZ_6/pz-6-2.py)<br>
Отчет - [Отчет_pz6.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz6.pdf)

### ПЗ №7

Дана строка. Если она представляет собой запись целого числа, то вывести 1, если вещественного (с дробной частью) - вывести 2; если строку нельзя преобразовать в число, то вывести 0. Считать, что дробная часть вещественного числа отделяется от его целой части десятичной точкой «.».

Решение - [pz-7.py](https://github.com/addavriance/PZ2/blob/main/PZ_7/pz-7.py)<br>
Отчет - [Отчет_pz7.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz7.pdf)

### ПЗ №7.1

Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или несколькими). Преобразовать каждое слово в строке, заменив в нем все предыдущие вхождения его последней буквы на символ «.» (точка). Например, слово «МИНИМУМ» надо преобразовать в «.ИНИ.УМ». Количество пробелов между словами не изменять.

Решение - [pz-7-1.py](https://github.com/addavriance/PZ2/blob/main/PZ_7/pz-7-1.py)<br>
Отчет - [Отчет_pz7.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz7.pdf)

### ПЗ №9

Организовать словарь avto, содержащий 3 ключа (марки авто) и списки из трех моделей в качестве значений. Обеспечить отображение вторых моделей по каждому авто, всех моделей словаря.

Решение - [pz-9.py](https://github.com/addavriance/PZ2/blob/main/PZ_9/pz-9.py)<br>
Отчет - [Отчет_pz9.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz9.pdf)

### ПЗ №10

На трех участках выращиваются следующие сельскохозяйственные культуры: картофель, лук, морковь, горох, капуста, редис. Определить, какие из этих культур имеются на каждом участке, имеются хотя бы на одном из участков и не имеются ни на одном участке.

Решение - [pz-10.py](https://github.com/addavriance/PZ2/blob/main/PZ_10/pz-10.py)<br>
Отчет - [Отчет_pz10.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz10.pdf)

### ПЗ №11

Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
    Исходные данные:
    Количество элементов:
    Сумма элементов:
    Элементы до n-1 умножены на элемент n:

Решение - [pz-11.py](https://github.com/addavriance/PZ2/blob/main/PZ_11/pz-11.py)<br>
Отчет - [Отчет_pz11.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz11.pdf)

### ПЗ №11.1

Из предложенного текстового файла (text18-19.txt) вывести на экран его содержимое, количество символов, принадлежащих к группе букв. Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив символы верхнего регистра на нижний.

Решение - [pz-11-1.py](https://github.com/addavriance/PZ2/blob/main/PZ_11/pz-11-1.py)<br>
Отчет - [Отчет_pz11.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz11.pdf)

### ПЗ №12

В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.

Решение - [pz-12.py](https://github.com/addavriance/PZ2/blob/main/PZ_12/pz-12.py)<br>
Отчет - [Отчет_pz12.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz12.pdf)

### ПЗ №12.1

Составить генератор (yield), который преобразует все буквенные символы в заглавные.

Решение - [pz-12.py](https://github.com/addavriance/PZ2/blob/main/PZ_12/pz-12-1.py)<br>
Отчет - [Отчет_pz12.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz12.pdf)

### ПЗ №13

В матрице найти среднее арифметическое элементов последних двух столбцов.

Решение - [pz-13.py](https://github.com/addavriance/PZ2/blob/main/PZ_13/pz-13.py)<br>
Отчет - [Отчет_pz13.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz13.pdf)

### ПЗ №13.1

Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и последних строках и столбцах матрицы Matr2 произвольного размера.

Решение - [pz-13-1.py](https://github.com/addavriance/PZ2/blob/main/PZ_13/pz-13-1.py)<br>
Отчет - [Отчет_pz13.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz13.pdf)

### ПЗ №14

Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений. Посчитать их количество.

Решение - [pz-14.py](https://github.com/addavriance/PZ2/blob/main/PZ_14/pz-14.py)<br>
Отчет - [Отчет_pz14.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz14.pdf)

### ПЗ №15

Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна содержать таблицу Перевозки со следующей структурой записи: маршрут, фамилия водителя, даты отправки и прибытия, масса груза.

Решение - [pz-15.py](https://github.com/addavriance/PZ2/blob/main/PZ_15/pz-15.py)<br>
Отчет - [Отчет_pz15.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz15.pdf)

### ПЗ №16

Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки. Добавьте методы для вычисления среднего балла и определения, является ли студент отличником.

Решение - [pz-16.py](https://github.com/addavriance/PZ2/blob/main/PZ_16/pz-16.py)<br>
Отчет - [Отчет_pz16.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz16.pdf)

### ПЗ №16.1

Создание базового класса "Животное" и его наследование для создания классов "Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать" и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства, такие как "гавкать" и "мурлыкать".

Решение - [pz-16_1.py](https://github.com/addavriance/PZ2/blob/main/PZ_16/pz-16_1.py)<br>
Отчет - [Отчет_pz16.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz16.pdf)

### ПЗ №16.2

Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно. Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.

Решение - [pz-16_2.py](https://github.com/addavriance/PZ2/blob/main/PZ_16/pz-16_2.py)<br>
Отчет - [Отчет_pz16.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz16.pdf)

### ПЗ №17

В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу (см. таблицу 1).


Решение - [pz-17.py](https://github.com/addavriance/PZ2/blob/main/PZ_17/pz-17.py)<br>
Отчет - [X]

### ПЗ №17.1

Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ № 2 - 9.

Решение - [pz-17-1.py](https://github.com/addavriance/PZ2/blob/main/PZ_17/pz-17-1.py)<br>
Отчет - [Отчет_pz17.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz17.pdf)

### ПЗ №17.2

Задание предполагает, что у студента есть проект с практическими работами (No2-13), оформленный согласно требованиям. 
<br>Все задания выполняются с использованием модуляOS:<br>
- Перейдите в каталог PZ11. 
- Выведите список всех файлов в этом каталоге. Именавложенных подкаталогов выводить не нужно.
- Перейти в корень проекта, создать папку с именем test.<br> В ней создать еще одну папку - test1. В папку test переместить два файла из П36, а в папку test1 - один файл из П37. <br>Файл из П37 переименовать в test.txt. Вывести в консоль информацию о размерефайлов в папке test.
- Перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести вконсоль. Использовать функцию basename() (os.path.basename()).
- Перейти в любую папку где есть отчет в формате .pdfи «запустите» файл впривязанной к нему программе. Использовать функцию os.startfile(). 
- удалить файл test.txt.

Решение - [pz-17-2.py](https://github.com/addavriance/PZ2/blob/main/PZ_17/pz-17-2.py)<br>
Отчет - [Отчет_pz17.pdf](https://github.com/addavriance/PZ2/blob/main/reports/Отчет_pz17.pdf)