#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date

def select_workers(staff, period):
    """
    Выбрать работников с заданным стажем.
    """
    # Получить текущую дату.
    today = date.today()

    # Сформировать список работников.
    result = []
    for employee in staff:
        if today.year - employee.get('year', today.year) >= period:
            result.append(employee)
           
    # Возвратить список выбранных работников.
    return result

