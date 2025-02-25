# Фрактальное пламя

## Описание
В проекте нужно реализовать алгоритм генерации изображения фрактального пламени, основанного на идее Chaos Game. Требуется реализовать однопоточную и многопоточную версию программы.

## Функциональные требования
1. Реализация цветного алгоритма генерации фрактального пламени.

2. Возможность запуска как в однопоточном, так и в многопоточном режиме.

3. Настройка параметров генерации: размер изображения, количество итераций, набор трансформационных функций и т.д.

4. Хотя бы 4 трансформации из оригинальной статьи.

## Нефункциональные требования
1. Программа должна легко конфигурироваться.

2. Многопоточная реализация должна работать быстрее однопоточной.

3. Опубликованы сравнительные результаты времени работы

    - Конфигурация системы

    - Время работы

    - Количество используемых потоков

## Описание входных и выходных данных
### Входные данные
1. Размеры изображения (ширина и высота).

2. Количество итераций для генерации фрактала.

3. Список трансформационных функций и их параметры.

### Выходные данные
1. Изображение фрактального пламени.

## Инструкции по реализации
1. Изучите теоретическую часть алгоритма для генерации фрактального пламени.
2. Реализуйте базовую однопоточную версию алгоритма с заданными параметрами.
3. Переведите однопоточную версию в многопоточную.
4. Добавьте конфигурацию для изменения числа потоков и других параметров генерации.

## Тестирование
1. Проверьте корректность работы алгоритма на различных наборах параметров.
    - В конце текста задания приведены примеры результатов, полученные студентами прошлых лет.
2. Проверьте корректность и напишите тесты для ваших трансформаций.
3. Выполните сравнение производительности однопоточной и многопоточной версий, измерив время выполнения.
4. Убедитесь, что реализация многопоточной обработки действительно ускоряет процесс генерации изображения.

## Ограничения и советы
1. Совет: убедитесь, что начальная реализация программы работает корректно, прежде чем переходить к многопоточности.
2. Совет: используйте профилировщик или отладочные замеры скорости для поиска узких мест.

## Дополнительные материалы
1. Описание фрактального пламени:
    - https://en.wikipedia.org/wiki/Fractal_flame
    - https://habr.com/ru/articles/251537
2. Оригинальная статья (+ каталог вариаций): https://flam3.com/flame_draves.pdf
3. Что такое Chaos Game:
    - https://en.wikipedia.org/wiki/Chaos_game
    - https://beltoforion.de/en/recreational_mathematics/chaos_game.php
4. Описание СИФ с нуля: https://proproprogs.ru/fractals
5. Онлайн демо: https://tariqksoliman.github.io/Fractal-Inferno
