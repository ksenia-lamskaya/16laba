#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun1(type='max'):
    def fun2(list):
        if type == 'max':
            return max(list)
        else:
            return min(list)
    return fun2