# 8) Дан одновимірний масив числових значень, що нараховує n елементів. Виключити всі нульові елементи.

# import pandas as pd
# import sqlite3 as s3
#
# import sqlalchemy as sq
# from sqlalchemy.orm import mapper
#
# import sys as sy
# import numpy as nu
#
# from sqlalchemy import table, column, Integer, digit
# metadata = MetaData()
# syntax = table('matric', metadata,
#     column('1', Integer, primary_key = True),
#     column('2', digit),
#     column('3', digit),
#     column('4'

def search(massive):
    result = []
    for element in massive:
        if int(element) == 0:
            pass
        else: result.append(element)
    return result

def correct(massive):
    correct_massive = []
    for element in massive:
        if bool(element.isdigit()) == True:
            correct_massive.append(element)
        else:
            new_element = input("Your enter isn't correct, enter number: ")
            correct_massive.append(new_element)
    return correct_massive

n = 0
while n!=1:
    massive = input("Enter massive space separated: ").split(" ")
    massive = correct(massive)
    print(search(massive))
    n = 1