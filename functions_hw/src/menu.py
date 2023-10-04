"""Functions for menu."""

import os.path
from typing import Tuple, Dict, Set, Callable
from .process_csv import get_command_hierarchy, get_departments_stats
from .process_csv import save_deps_stats


def highlight_print(f: Callable) -> Callable:
    """Highlights the output of the function f with '-' and linebreaks.

    @f (Callable): function which output will be highlighted.

    Returns:
        Callable:   function with the logic of function f,
                    but highlighting its output.
    """
    def wrapper(*args, **kwargs):
        print('\n' + '-' * 15)
        result = f(*args, **kwargs)
        print('-' * 15, end='\n\n')
        return result
    return wrapper


def print_menu(default_data_path: str = 'data/Corp_Summary.csv') -> None:
    """Print menu to std-out.

    @default_data_path (str, optional): Path to default data file.
                                        Defaults to 'data/Corp_Summary.csv'.
    """
    print('Меню.\n Выберите опцию:')
    print('\t1. Вывести иерархию команд')
    print('\t2. Вывести отчет по департаментам')
    print('\t3. Сохранить отчет в .csv файл')
    print('\t4. Выход')
    print(f'\nПо умолчанию файл с данными ищется в {default_data_path}.')
    print(
        'Если нужен другой файл укажите путь до него '
        'после выбора опции в формате "(опция) (путь)"'
    )


def get_user_choice(default_data_path: str = 'data/Corp_Summary.csv') \
                                                    -> Tuple[str, str]:
    """Get user action choice from std-in.

    @default_data_path (str, optional): Path to default data file.
                                        Defaults to 'data/Corp_Summary.csv'.

    Returns:
        Tuple[str, str]: user option, path to data file
    """
    print_menu(default_data_path)
    inp = input('Выбор: ').strip().split()[:2]
    opt, data_path = inp[0], default_data_path
    if len(inp) >= 2:
        data_path = inp[1]
    return opt, data_path


@highlight_print
def print_hierarchy(hierarchy: Dict[str, Set[str]]) -> None:
    """Print command hierarchy from hierarchy dict.

    @hierarchy (Dict[str, Set[str]]): dictionary representing the command
                                      hierarchy, where department names
                                      are keys and sets of command names
                                      are values.
    """
    for dep, coms in hierarchy.items():
        print(f'{dep}:')
        for com in coms:
            print(f'\t{com}.')
        print()


@highlight_print
def print_deps_report(dep_stats: Dict[str, Dict[str, int | float]]) -> None:
    """Print departements report from dep_stats departments statistics.

    @dep_stats (Dict[str, Dict[str, int  |  float]]): dict with departments
                                                      statistics.
    """
    for dep, stats in dep_stats.items():
        print(f'{dep}:')
        print('\tКоличество сотрудников', stats['count'])
        print('\tМаксимальная ЗП', stats['max_salary'])
        print('\tСредняя ЗП', round(stats['mean_salary'], 2))
        print('\tМинимальная ЗП', stats['min_salary'])


def execute_user_choice(option: str, data_path: str) -> None:
    """Execute user choice with selected option and data path.

    @option (str): user option.
    @data_path (str): path to .csv file with data.
    """
    if option == '1':
        hierarchy = get_command_hierarchy(data_path)
        print_hierarchy(hierarchy)
    if option == '2':
        dep_stats = get_departments_stats(data_path)
        print_deps_report(dep_stats)
    if option == '3':
        dep_stats = get_departments_stats(data_path)
        head, tail = os.path.split(data_path)
        tail = 'report_' + tail
        save_pth = os.path.join(head, tail)
        save_deps_stats(dep_stats, save_pth)
        highlight_print(lambda: print('Файл отчета сохранен в', save_pth))()
