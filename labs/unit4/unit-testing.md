# Модульне тестування

## Структура директорії для лабораторної роботи
```
└── lab09
    ├── Doxyfile
    ├── Makefile
    ├── README.md
    ├── test
    │   └── test.c
    └── src
        ├── lib.c
        ├── lib.h
        └── main.c
```

**Зверніть увагу**. Для роботи з тестами вам потрібно:
   - Додати файл з тестами (файл `./test/test.c`)
   - інсталювати утиліту libcheck (див. https://libcheck.github.io/check/web/install.html)
   - В Makefile додати цілі для компіляції та запуску тестів (файл `./test/test.c`) з доданням опції `-lcheck`. Наприклад (код взято з `sample_project`):

```sh
	compile: main.bin test.bin
	test.bin: test/test.c
		$(CC) $(C_OPTS) $< -fprofile-instr-generate -fcoverage-mapping -o ./dist/$@ -lcheck
	test: clean prep compile
		LLVM_PROFILE_FILE="dist/test.profraw" ./dist/test.bin
		llvm-profdata merge -sparse dist/test.profraw -o dist/test.profdata
		llvm-cov report dist/test.bin -instr-profile=dist/test.profdata src/*.c
		llvm-cov show dist/test.bin -instr-profile=dist/test.profdata src/*.c --format html > dist/coverage.html
```

## Основне завдання

* Переробити попередній проект (робота з функціями) на багатофайлову структуру, в якої:
   * `main.c` - складається з тестового запуску функцій для завідомо відомих даних
   * `lib.c` - складається з реалізації розроблених функій
   * `lib.h` - складається з прототипів розроблених функцій, що документовані
* Для попередньо розробленої функції (функцій) додати методи – модульні тести, що демонструють коректність роботи розробленого функціоналу. Розроблені методи мають перевірити коректність функціонування функцій на наборі заздалегідь визначених вхідних-вихідних даних. 

Приклад файл-тесту для веріфікації додатку 2 чисел (функция `int sum(int a, int b);`) (без коментарів):

```c
	#include "lib.h"
	#include <check.h>

	START_TEST(test_sum)
	{
	#define DATA_SIZE_SUM 3
		int input_data_a[] = { 1, 3, -1 };
		int input_data_b[] = { 2, 0, 10 };
		int expected_values[] = { 3, 3, 9 };

		for (int i = 0; i < DATA_SIZE_SUM; i++) {
			int actual_value = sum(input_data_a[i], input_data_b[i]);
			ck_assert_int_eq(expected_values[i], actual_value);
		}
	}
	END_TEST

	int main(void)
	{
		Suite *s = suite_create("Programing");
		TCase *tc_core = tcase_create("lab09");

		tcase_add_test(tc_core, test_sum);
		suite_add_tcase(s, tc_core);

		SRunner *sr = srunner_create(s);
		srunner_run_all(sr, CK_VERBOSE);
		int number_failed = srunner_ntests_failed(sr);
		srunner_free(sr);

		return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
	}

```

**Зверніть увагу.** Дана лабораторна робота не передбачає наявності звіту

## Посилання на літературу
- https://clang.llvm.org/docs/SourceBasedCodeCoverage.html

## Контрольні питання.
1.	Що таке модульний тест?
2.	Як протестувати функцію конкатенації двох рядків?
3.	Як протестувати функцію об’єднання двох масивів?
4.	Як запустити модульний тест?
5.	Коли виконуються модульні тести?
6.	Які принципи модульного тестування?
7.	Навіщо потрібні модульні тести? Які ще бувають тести?