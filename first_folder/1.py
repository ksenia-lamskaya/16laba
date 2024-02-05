#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import func_first as func_first

if __name__ == "__main__":
    num = [int(a) for a in input("Вводите числа: ").split()]
    test_max = func_first.fun1()
    result = test_max(num)
    print("Результат выполнения программы: ", result)