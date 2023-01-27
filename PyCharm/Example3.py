#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = set(".,:;' !?@#()")

    l1 = set(input("Введите первую строку: ").lower())
    l2 = set(input("Введите вторую строку: ").lower())

    p = l1.intersection(l2)
    pn = p.difference(a)

    print(f"Общие символы: {pn}")
