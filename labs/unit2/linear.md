# Розробка лінійних програм

## Структура директорії для лабораторної роботи

```
		.
		└── lab03
		    ├── Makefile
		    ├── README.md
		    ├── doc
		    │   └── lab03.txt
		    └── src
		        └── main.c
```

## Передмова

Починаючи з цієї лабораторної роботи ви повинні використовувати `Makefile`. Для спрощення вам життя, ви можете використовувати наданий у перший роботі приклад. Але треба виконати його модифікацію:

- так як ви працюєте лише з файлом `main.c` (до лабораторної роботи, що стосується покажчиків), вам потрібно видалити використання файлів `lib.c`, `lib.h`. Використовуючи наданий раніше Makefile це можливо зробити, закоментувавши строку 02 (де декларується змінна LAB_OPTS).

**Загальна рекомендація**. Не соромтесь фіксувати зміни часто. Якщо Ваша робота над лабораторною роботою займає більше одного дня, заради ваших нервів, наприкінці дня зробіть коміт на завантажте зміни до видаленого репозиторія. Таким чином, якщо у вас щось станеться з віртуальною машиною - ви будете мати мінімум незбережених даних (а заново виконати інсталяцію пакетів лабораторної роботи - займає менш ніж годину без вашої присутності)


## Індивідуальні завдання.

Виконати одне завдання з пулу завдань на свій розсуд згідно її складності (що впливає на максимальну оцінку, що може бути отримана за лабораторну роботу). **Зверніть увагу**. Викладач має право надати вам додаткове завдання для виконання.

1.	Обчислити об’єм циліндра *V* з радіусом його основи *r* і висотою *h*.
2.	Визначити відстань, яка пройдена фізичним тілом за час *t*, якщо тіло рухається з постійним прискоренням *a* і має в початковий момент часу швидкість *v0*.
3.	За заданим радіусом *r* визначити довжину окружності *l*, площу кола *S* та об’єм кулі *V*. 

4.	Відомо, що 1 дюйм дорівнює 2.54 см. Задане значення дюймів перевести в сантиметри та навпаки, для заданого значення сантиметрів визначити його еквівалент у дюймах.
5.	Визначити площу та периметр квадрата із стороною *a*.
6.	Кут задано у радіанах. Перевести радіанну міру у градуси.
7.	Температура задана у градусах за Цельсієм. Перевести температуру у градуси за Фаренгейтом і навпаки – температуру у градусах за Фаренгейтом – у температуру у градусах за Цельсієм.
8.	Знайти периметр і площу рівнобедреного трикутника за умови, що задані координати його вершин. Враховуємо, що основа трикутника паралельна осі *OX*.
9.	Дана довжина ребра куба. Знайти об’єм куба і площу його бічної поверхні.
10.	Знайти значення *n*-го елементу арифметичної прогресії, при заданих значеннях початкового значення та кроку прогресії

12.	(`*`) Дано трьох-значне число. Обчислити значення другої цифри в числі. 
Наприклад, $x = 456$  ->  $y = 5$.
13.	(`*`) Дано десяткове ціле 4-розрядне число. Визначити суму цифр заданого числа.
14.	(`*`) Визначити квадрат відстані у просторі між двома точками *M1* і *M2* із їх заданими координатами $(x1, y1, z1)$ і $(x2, y2, z2)$.
15.	(`*`) Дана сума грошей у гривнях. Перевести гривні в долари, євро, російські рублі.  Курси валют (долар, євро, російський рубль) задати в вигляді констант.

16.	(`**`) За заданим опором трьох резисторів *r1*, *r2*, *r3*, які з’єднані паралельно, визначити загальний опір.
17.	(`**`) Визначити число, яке отримане виписуванням у зворотному порядку цифр заданого тризначного числа в десятковій системі числення.
18.	(`**`) Дано дійсне число *a*. Не використовуючи тимчасові змінні та користуючись тільки операціями зсуву, отримати значення: $a * 16$, $a * 1024$ – за одну операцію.
19.	(`**`) Дано 4-розрядне число у системі числення *p* (наприклад, 8). Визначити його еквівалент у десятковій системі числення. На вході система числення повинна бути у діапазоні [2..10].
20.	(`**`) Визначити, у скільки разів перша цифра 3х-значного числа більша, ніж остання. Результат "обрізати" до другого знака після коми. Для поточного завдання "обрізання" включає до себе перевірку того, що отримане число відрізняється від очікуваного не більше, ніж на 0.00001. Наприклад, $x=123$ ->  $y = 1/3 = 0.333333 = 0.330000$.
21.	(`**`) Підрахувати суму чисел у заданому діапазоні. Наприклад, при вхідних даних *50* та *52* повинно бути $50 + 51 + 52 = 153$.
22.	Прямокутник заданий координатами своїх вершин (*x1*, *y1*, *x2*, *y2*, *x3*, *y3*, *x4*, *y4*). Знайти периметр *P* і площу *S* прямокутника. Враховуємо, що сторони прямокутника паралельні осям координат.


## Додаткові обов'язкові умови виконання робот

- текст програми повинен мати коментарі до коду. Точка входу має також бути документована формулюванням завдання, а також по-пунктного його виконанням;
- структура проекту повинна бути згідно вимогам;
- звіт має містити інформацію про хід виконання завдання, а саме:
   - створення проекту та файлу з вихідним кодом;
   - визначити, де знаходиться точка входу; описати її знаходження, призначення, та чому вона повинна бути одна;
   - запуск програми; 
   - зупинка посередині виконання програми за допомогою breakpoints. Навести приклад зміни стану програми "на льоту";
- звіт не повинен мати зображення.

## Посилання на літературу
### Code convention
- https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard
- https://releases.llvm.org/download.html
- https://github.com/torvalds/linux/blob/master/.clang-format
- https://www.kernel.org/doc/html/v5.14/process/coding-style.html
- https://resources.sei.cmu.edu/downloads/secure-coding/assets/sei-cert-c-coding-standard-2016-v01.pdf


## Приклад звіту для лабораторних робот 3-7

Лабораторна робота №3. Розробка лінійних програм

Давидов Вячеслав Вадимович, гр. КІТ-24а

Завдання: визначити об'єм конуса.

Основна частина:

- опис роботи основної функції: об'єм конуса визначається за формулою: $V = 1/3 * pi * r^2 * h$, де pi - константа, h - висота конуса, r - радіус основи конуса.
- перелік вхідних даних:
   - h - висота конуса, позитивне дійсне число (float);
   - r - радіус основи конуса, позитивне дійсне число (float).
- перелік констант: 
   - pi - математична константа. Дорівнює значенню 3.14159.
- дослідження результатів роботи програми:
   - V - об'єм конуса. Так як всі оперуємі числа є дійсними, то й результуюча змінна є дійсною. Також, слід визначити, що об'єм конуса не може бути негативним. Тому, її тип - float
   - при значенні h=2.5 та r=12, об'єм конуса повинен складати: $1/3 * 3.14159 * 12 * 12 * 2.5 = 376.9908$
   - для підтвердження коректності роботи програми, зупинено відлагодник на строці з "return 0" та введемо команду "print V". Після вводу команди отримали наступне:

```
	(lldb) print V
	(float) $1 = 376.990814
```

   Як бачимо, результат майже співпав. Похибка 0.000014 є дозволеною при виконанні операцій з плаваючою крапкою. Подібність результатів говорить про те, що програма працює коректно.

Структура проекту лабораторної роботи:

```
		.
		└── lab03
		    ├── README.txt
		    ├── Makefile
		    └── src
		        └── main.c
```

Висновки: при виконанні лабораторної роботи буди набуті практичні навички створення лінійних програм на мові С, зокрема: визначати типи даних, обчислювати математичні вирази, емулювати операцію зведення до ступеню через операцію множення.


## Контрольні питання. 
1.	З яких розділів складається програма мовою С? 
2.	Який алгоритм називається лінійним?
3.	Запишіть усі можливі оператори, які дозволять значення змінної a збільшити на одиницю.
4.	Що таке "проект"?
5.	Який порядок створення нового порожнього проекту? 
6.	Як виконати збірку програми?
7.	Який порядок додавання нового файлу до проекту?
8.	Як виправити помилку у програмі?
9.	Як поставити програму на виконання?
10.	Чим консольні програми відрізняються від віконних-програм?
11.	Чим змінна відрізняється від константи?
12.	Чим відрізняється префіксний запис операції інкременту від постфіксного запису?