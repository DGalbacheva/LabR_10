#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = set("аоуэыяеюёи")

    s = input("Введите строку: "). lower()

    count = 0
    for i in s:
        if i in a:
            count += 1

    print(f"Количество гласных: {count}")