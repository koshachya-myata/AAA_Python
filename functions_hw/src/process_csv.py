"""Functions for csv processing."""

from typing import Dict, Set


def get_command_hierarchy(data_path: str) -> Dict[str, Set[str]] | None:
    """Read a CSV file at the given data_path; construct a command hierarchy.

    This function reads the data from a CSV file at the specified 'data_path'
    and constructs a command hierarchy in the form of a dictionary
    where department names (keys) map to sets of command names (values).
    If there is no columns with department or a command then None returnted.

    @data_path (str): path to the CSV file with department and command data.

    Returns:
        Dict[str, Set[str]] | None: None or a dictionary representing the
                                    command hierarchy, where department names
                                    are keys and sets of command names
                                    are values.
    """
    hierarchy: Dict[str, Set[str]] | None = None
    with open(data_path) as f:
        cols = f.readline().split(';')
        cols[-1] = cols[-1][:-1]  # delete \n
        if 'Департамент' not in cols or 'Отдел' not in cols:
            return None
        dep_ind = cols.index('Департамент')
        com_ind = cols.index('Отдел')
        hierarchy = dict()
        for line in f:
            row = line.split(';')
            dep, com = row[dep_ind], row[com_ind]
            if dep not in hierarchy.keys():
                hierarchy[dep] = set()
            hierarchy[dep].add(com)
    return hierarchy


def get_departments_stats(data_path: str) -> Dict[str, Dict[str, int | float]]:
    """Construct departments statistics from .csv file from data_path.

    Read a CSV file at the given data_path; construct statistics about
    each department. Statistics for department consists of count of employees
    and max salary, mean salary, min salary.

    @data_path (str): path to .csv file with data.

    Returns:
        Dict[str, Dict[str, int | float]]: dict with departments statistics.
    """
    deps_stats: Dict[str, Dict[str, int | float]] = dict()
    with open(data_path) as f:
        cols = f.readline().split(';')
        cols[-1] = cols[-1][:-1]  # delete \n
        salary_ind = cols.index('Оклад')
        dep_ind = cols.index('Департамент')
        for line in f:
            row = line.split(';')
            dep, salary = row[dep_ind], int(row[salary_ind])
            if dep not in deps_stats.keys():
                deps_stats[dep] = dict()
                deps_stats[dep]['count'] = 1
                deps_stats[dep]['min_salary'] = salary
                deps_stats[dep]['max_salary'] = salary
                deps_stats[dep]['max_salary'] = salary
                deps_stats[dep]['sum_salary'] = salary
            else:
                deps_stats[dep]['count'] += 1
                deps_stats[dep]['min_salary'] = min(
                                                salary,
                                                deps_stats[dep]['min_salary']
                                                )
                deps_stats[dep]['max_salary'] = max(
                                                salary,
                                                deps_stats[dep]['max_salary']
                                                )
                deps_stats[dep]['sum_salary'] += salary
    for dep in deps_stats.keys():
        deps_stats[dep]['mean_salary'] = \
            deps_stats[dep]['sum_salary'] / deps_stats[dep]['count']
        deps_stats[dep].pop('sum_salary')
    return deps_stats


def save_deps_stats(deps_stats: Dict[str, Dict[str, int | float]],
                    save_path: str = 'data/report_deps_stats.csv') -> None:
    """Save departments statistics deps_stats to .csv file save_path.

    @deps_stats (Dict[str, Dict[str, int  |  float]]):  dict with
                                                        departments statistics.
    @save_path (str, optional): path where the .csv file will be saved.
                                Defaults to 'data/report_deps_stats.csv'.
    """
    with open(save_path, 'w+') as f:
        cols = ['Департамент', 'Число сотрудников', 'Минимальная ЗП',
                'Средняя ЗП', 'Максимальная ЗП']
        f.write(';'.join(cols) + '\n')
        for dep, stats in deps_stats.items():
            row = list(map(str, [dep, stats['count'], stats['min_salary'],
                                 stats['mean_salary'], stats['max_salary']]))
            f.write(';'.join(row) + '\n')
