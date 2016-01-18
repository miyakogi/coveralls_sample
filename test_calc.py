#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from calc import calculator


def test_add():
    assert calculator('+', 1, 3) == 4

def test_sub():
    assert calculator('-', 3, 1) == 2

def test_div():
    assert calculator('/', 36, 6) == 6
