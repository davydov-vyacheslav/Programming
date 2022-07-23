# Взаємодія з користувачем шляхом механізму введення/виведення

## Структура директорії для лабораторної роботи

```
└── lab12
    ├── Doxyfile
    ├── Makefile
    ├── README.md
    ├── assets
    │   └── input.txt
    ├── doc
    │   └── lab12.md
    ├── test
    │   └── test.c
    └── src
        ├── lib.c
        ├── lib.h
        └── main.c
```


**Зверніть увагу**. Початковий Текст зберігається у файлі `assets/input.txt` однією строкою. Програма повинна зчитати дані з стандартного потоку `stdin`. Приклад передачі контенту файлу до стандартного потоку вводу `main.bin`:
```sh
cd lab12
cat ./assets/input.txt | ./dist/main.bin
```

## Індивідуальні завдання.

Виконати завдання з пулу завдань на свій розсуд згідно її складності (що впливає на максимальну оцінку, що може бути отримана за лабораторну роботу). **Зверніть увагу**. Викладач має право надати вам додаткове завдання для виконання.

При виконанні завдань слід зазначити, щоб:

- при старті програми виводилась інформація об авторі, номері та темі лабораторної роботи;
- при запиті даних, користувач отримав повідомлення, що від нього очікують;
- початкові дані вводилися з клавіатури за допомогою функції *scanf()*;
- видача результуючих даних проводилася у консоль за допомогою функції *printf()*;
- після запиту даних треба виконати валідацію введених даних з точки зору бізнес логіки;
- на базі введених даних створити стосовні дані *речових* чисел в діапазоні`(-1000; 1000)` з мінімальним кроком 0.001;
- результат роботи виводу матриці повинен бути відформатованим стосовно наступного прикладу:

```
[   -5.25  33.25    23.00 ]
[ -454.50   0.00   123.23 ]
[  323.99 123.55  -123.00 ] 
``` 

**Завдання**:

1. Визначити суму двох матриць.
2. Визначити добуток двох матриць.
3. Визначити транспоновану матрицю.
4. (`*`) Сформувати трикутник Паскаля ітеративним та рекурсивним методом.
5. (`*`) Визначити зворотню матрицю.

## Додаткові завдання підвищеної складності:

1. (`**`) Виконати індивіджуальне завдання з взаємодією з користувачем шляхом використання функцій *write()*, *read()*

## Додаткові обов'язкові умови виконання робот

- програма має мати документацію, що оформлена за допомогою утиліти doxygen;
- звіт повинен бути оформлений згідно "Вимогам до структурної побудови звіту";
- продемонструвати відсутність витоків пам’яті за допомогою утиліти *valgrind*;
- доступ до елементів масиву здійснювати через розіменування покажчиків, а не через оператор індексування (*[ ]*);
- продемонструвати роботу розроблених методів за допомогою модульних тестів;
- у звіті навести ступень покриття коду модульними тестами. 50% - є мінімально допустимим відсотком покриття коду тестами.

## Контрольні питання.
1.	Як виводити текст на консоль?
2.	Як читати дані з клавіатури?
3.	В чому різниця форматованого виведення даних від неформатованого?
4.	У якому файлі знаходяться прототипи функцій введення/виведення?
5.	Який символ використовується для формування адреси змінної?
6.	Як можна форматувати дані при їх виведенні на екран?
7.	Які дії виконує функція читання при введенні даних з клавіатури?
8.	Які дії виконує функція виведення даних на екран?
9.	Як ввести текст, який складається з декількох слів?
10.	Як вивести текст, який складається з декількох слів?
