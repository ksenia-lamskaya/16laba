#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def display_workers(staff):
    """
    Отобразить список работников.
    """
    # Проверить, что список работников не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )

        print(line)
        print(
       '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "№",
            "Ф.И.О.",
            "Должность",
            "Год"
            )
        )
        print(line)
    
        # Вывести данные о всех сотрудниках.
        for idx, worker in enumerate(staff, 1):
            print(
               '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                worker.get('name', ''),
                worker.get('post', ''),
                worker.get('year', 0)
                )
            )
        print(line)
       
    else:
        print("Список работников пуст.")
       