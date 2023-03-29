from pywebio.output import toast, put_button, put_text, use_scope
from random import choice


def step() -> str:
    side = ["левая", "правая"]
    organ = ["рука", "нога"]
    color = ["красный", "синий", "зеленый", "желтый"]
    return f'{choice(side)} {choice(organ)} {choice(color)}'


def get_steps_list(data='data.txt') -> list:
    """выбираем последние 5 строк"""
    with open(data, 'r', encoding='UTF-8') as file:
        return file.readlines()[-5:]


def main():
    """рандомим шаг"""
    step_ = step()
    """записываем шаг в data.txt"""
    with open('data.txt', 'a', encoding='UTF-8') as file:
        print(step_, file=file)
    """передаем в шаблон последние 5 шагов"""
    with use_scope('scope', clear=True):
        step_list = get_steps_list()
        [put_text(step_list[i].strip()) for i in range(len(step_list))]
    """очищаем data.txt если в нем больше 100 сторк"""
    with open('data.txt', 'r', encoding='UTF-8') as file:
        if len(file.readlines()) > 100:
            open('data.txt', 'w', encoding='UTF-8').close()
    toast(step_, color='#808080')


put_button("ШАГ", onclick=main)

if __name__ == '__main__':
    main()
