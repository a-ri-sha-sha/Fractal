from render import render
from genetetor import ImageUtils, ImageFormat
from typing import List
from transformation import add_transformation

def setting_game():
    print('Введи размеры изображения')
    width, height = map(int, input().split())
    while (width < 0 or height < 0):
        print('Ширина и высота должны быть больше 0!')
        print('Введи размеры изображения')
        width, height = map(int, input().split())

    print('Введи количество итераций для генерации фрактала')
    it = int(input())
    while (it < 0):
        print('Количество итераций должно быть больше 0!')
        print('Введи количество иттераций для генерации фрактала')
        it = int(input())
    
    transformations = []
    print('Введи виды трансформаци, которые хочешь использовать для генерации изображения')
    print('Напиши "Синусоидальное", "Сферическое", "Полярное", "Сердце", "Диск"')
    print('Если хочешь закончить, напиши "-"')
    transform = input().lower()
    while transform != '-':
        add_transformation(transform, transformations)
        transform = input().lower()

    print('Подождите, изображение генерируется')
    image = render(100000, 5, it, width, height, transformations)
    ImageUtils.save(image, "fractal.png", ImageFormat.PNG)
    print('Изображение успешно сохранено в файле fractal.png')


def start():
    while (True):
        print('Привет! Давай сгенирируем фрактальное пламя.')

        setting_game()

        print('Сыграем еще? Напиши "да" или "нет".')
        play_again_word = "да"
        not_play_again_word = "нет"
        user_word = input().lower()

        while user_word not in (play_again_word, not_play_again_word):
            print('Упс! Я вас не понимаю.')
            print('Сыграем еще? Напиши "да" или "нет".')
            user_word = input().lower()

        if user_word == not_play_again_word:
            break

if __name__ == "__main__":
    start()
