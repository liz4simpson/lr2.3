#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input('Введите предложение:\n')
    s1 = s.split()
    i = 0
    s1.sort(key=len, reverse=True)
    s = ''
    for i in range(0, len(s1)):
        s += s1[i] + ' '
    print(s)
