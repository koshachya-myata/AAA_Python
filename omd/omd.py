"""Print to std-out story of a duck. User input in std-in."""

# Bulat Gizatullin <gizat.blt@gmail.com>

import random

RAIN_PROBABILITY = 0.2


def get_weather() -> str:
    """Randomly choose what the weather will be like today.

    Returns:
        str: weather (rainy/sunny)
    """
    if random.random() < RAIN_PROBABILITY:
        return 'rainy'
    return 'sunny'


def undefined_action(step: int):
    """Duck is confused. Need if something went wrong during the story.

    Args:
        step (int): number of Duck story step
    """
    if step == 2:
        print('Погода кажется неопределенной 😳 ')
        print('Уточка 🦆 в растерянности добралась до бара')


def ask_user(options=None):
    """Ask a user to choose option.

    Args:
        options (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    if options is None:
        options = options = {'да': True, 'нет': False}
    option = ''
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return options[option]


def step4_food():
    """Print fourth stage of the duck story, when she take a food."""
    print(
        'Уточка 🦆 заказала себе еду 🍖, поела. '
        'Затем отлично провела время в баре с друзьями 🍻 '
        'и в хорошем настроении вернулась домой.'
    )


def step4_no_food():
    """Print fourth stage of the duck story, when she didn't take a food."""
    print(
        'Уточка 🦆 решила не брать себе еду. '
        'и сразу начала 🍻. '
        'Не успев заметить, она захмелилась. '
        'В итоге, ее друзьям пришлось провожать ее домой.'
    )


def step3():
    """Start third step of the duck story. The duck reached the bar."""
    print(
        'Сев за стол в баре, уточка 🦆 поняла, '
        'что немного проголодалась. '
        'Стоит ли ей поесть перед выпивкой?'
    )
    opt_value = ask_user()
    if opt_value:
        return step4_food()
    step4_no_food()


def step2_umbrella(weather='rainy'):
    """Start second step of the duck story, when duck take umbrella."""
    if weather == 'rainy':
        print(
            'Уточка 🦆 не ошиблась с выбором 💪. '
            'Полил дождь 😱.'
        )
        print(
            'Воодушевленная своим верным решением 🧠, '
            'уточка 🦆 добралась до бара'
        )
    elif weather == 'sunny':
        print(
            'Уточка 🦆 ошиблась! '
            'Тучки уже разошлись 😶‍🌫️. '
            'Дождя нет! 🤯 '
            'Теперь ей придется 😨 везде таскать с собой зонт ☂️ 😭.'
        )
        print('С зонтом на перевс, уточка 🦆 добралась до бара.')
    else:
        undefined_action(2)
    step3()


def step2_no_umbrella(weather='sunny'):
    """Start second step of the duck story, when duck take umbrella.

    Args:
        weather (str, optional): today weather (sunny/rainy).
                                 Defaults to 'sunny'.
    """
    if weather == 'sunny':
        print(
            'А тучек, будто и не было! ☀ '
            'Знала ведь уточка, что сегодня обойдется без дождя 😎. '
            'Интуиция 🧠 в который раз ее не подводит.'
        )
        print(
            'В хорошем настроении, на легке, '
            'уточка 🦆 добралась до бара.'
        )
    elif weather == 'rainy':
        print(
            'Ооо неет, пошел дождь 🌧. '
            'Почему же уточка не взяла зонт 😭'
        )
    else:
        undefined_action(2)
    step3()


def step1():
    """First step of the duck story."""
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option_value = ask_user()
    weather = get_weather()
    if option_value:
        return step2_umbrella(weather)
    return step2_no_umbrella(weather)


if __name__ == '__main__':
    step1()
