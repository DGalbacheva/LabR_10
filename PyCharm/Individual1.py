#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a","f", "i", "n", "o"}
    b = {"f", "g", "o", "p", "z"}
    c = {"i", "j", "u", "w"}
    d = {"f", "h", "n", "t", "u", "y", "z"}

    x = (a.intersection(b)).union(c)
    print(f"x = {x}")

    # Найдем дополнения множества
    bn = u.difference(b)
    an = u.difference(a)

    y = (an.intersection(bn)).difference(c.intersection(d))
    print(f"y = {y}")