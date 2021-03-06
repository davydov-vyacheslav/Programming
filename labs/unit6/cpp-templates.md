# Шаблонні функції та класи

## Структура директорії для лабораторної роботи

```
└── lab-cpp-05
    ├── Doxyfile
    ├── Makefile
    ├── README.md
    ├── doc
    │   └── lab-cpp-05.md
    ├── test
    │   └── test.cpp
    └── src
        ├── list.hpp
        └── main.cpp
```

## Загальне завдання. (Задача не пов’язана з попередніми роботами). 

- Зробити шаблоний клас-список (на базі динамічного масиву), що має шаблоноване поле масиву (для будь-якого існуючого типу даних)
- Створити наступні методи:
   - вивод вмісту масиву на екран;
   - визначити індекс переданого елемента в заданому масиві;
   - відсортувати елементи масиву;
   - визначити значення мінімального елемента масиву;
   - додати елемент до кінця масиву;
   - видалити елемент з масиву за індексом.

## Додаткові обов'язкові умови виконання робот.

- програма має мати документацію, що оформлена за допомогою утиліти doxygen;
- робота повинна бути оформлена згідно "Вимогам до структурної побудови звіту";
- продемонструвати відсутність витоків пам’яті за допомогою утиліти *valgrind*;
- продемонструвати роботу розроблених методів за допомогою модульних тестів;
- у звіті навести ступень покриття коду модульними тестами. 50% - є мінімально допустимим відсотком покриття коду тестами;
- продемонструвати роботу розроблених методів за допомогою модульних тестів;
- не використовувати конструкцію "using namespace std;", замість цього слід робити "using" кожного необхідного класу, наприклад: using std::string,  using std::cout;
- у проекті не повинні використовуватися бібліотеки введення / виведення мови C, а також не повинні використовуватися рядки типу `char*`.

<!-- no tests? -->

## Контрольні запитання
1. Для чого потрібні шаблони?
2. Як описати шаблонну функцію?
3. Як використовувати шаблонну функцію?
4. Чим відрізняються шаблонні функції від звичайних функцій?
5. Які дії виконує компілятор при виклику шаблонної функції?
6. Що треба зробити, щоб як аргумент шаблонної функції можна було вказувати змінну класу?
7. Які використовуються ключові слова для оголошення типу шаблонного аргументу?
8. Для чого потрібні шаблонні класи?
9. Як декларувати шаблонні класи?
10. Що таке статичний поліморфізм?
11. Що таке спеціалізація?
12. Чи є шаблонними методи у шаблонному класі?
