#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from eventmaster import *
import time


def firstfun():
    i = 0
    while i < 10:
        print("first" + str(i))
        i = i + 1


def secondfun():
    i = 0
    while i < 10:
        print("second" + str(i))
        i = i + 1


def thirdfun(a):
    print(a)


def fourthfun(a, b, c, d):
    print(a, b)
    print(d, c)


EvMaster = EventMaster()            # Создаем мастера событий и запускаем его
EvMaster.start()

evFirst = Event()         # Создаем блок события
evSecond = Event()
evThird = Event()
evFourth = Event()

evFirst.connect(firstfun)       # Привязываем ф-ию к событию
evSecond.connect(secondfun)
evThird.connect(thirdfun)
evFourth.connect(fourthfun)


EvMaster.append(evFirst)    # Добавляем блок события в EM
EvMaster.append(evSecond)
EvMaster.append(evThird)
EvMaster.append(evFourth)

evFirst.push()                 # Вызываем событие
evSecond.push()
evThird.push("Ye")
time.sleep(1)
evFourth.push("a", 3, 1, 6)

time.sleep(3)

EvMaster.exit()

