"""Формирование списка свободных окон по 30 минут."""
from datetime import datetime, timedelta

workday_start = datetime.strptime('09:00', '%H:%M')
workday_end = datetime.strptime('21:00', '%H:%M')

busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

busy_intervals = [
    (datetime.strptime(interval['start'], '%H:%M'), datetime.strptime(interval['stop'], '%H:%M'))
    for interval in busy
]


def free_windows_list_datetime(intervals_list: list) -> list:
    """Функция получения списка свободных окон в объектах datetime.

    Args:
        intervals_list (list): Список занятых интервалов.

    Returns:
        list: Список свободных окон.
    """
    list_free_windows = []
    current_time = workday_start

    for start, stop in sorted(intervals_list):
        if (current_time + timedelta(minutes=30)) < start:
            list_free_windows.append((current_time, start))
        current_time = stop

    if current_time < workday_end:
        list_free_windows.append((current_time, workday_end))
    return list_free_windows


def free_windows_thirty_minutes_list_datetime(intervals_list: list) -> list:
    """Функция получения списка свободных окон по 30 минут в объектах datetime.

    Args:
        intervals_list (list): Список занятых интервалов.

    Returns:
        list: Список свободных окон по 30 минут в объектах datetime.
    """
    free_windows_thirty_min = []

    def split_window(start, stop, step):
        while start + step <= stop:
            yield (start, start + step)
            start += step
    for start, stop in free_windows_list_datetime(intervals_list):
        free_windows_thirty_min.extend(split_window(start, stop, timedelta(minutes=30)))

    return free_windows_thirty_min


def list_free_windows_thirty_minutes(intervals_list: list) -> list:
    """Функция получения списка словарей со свободными оконами по 30 минут.

    Args:
        intervals_list (list): Список занятых интервалов.

    Returns:
        list: Список словарей со свободными оконами по 30 минут.
    """
    return [{'start': start.strftime('%H:%M'), 'stop': stop.strftime('%H:%M')} for start, stop in free_windows_thirty_minutes_list_datetime(intervals_list)]


list_free_windows_thirty_minutes(busy_intervals)
