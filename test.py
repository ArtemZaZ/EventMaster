#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from RTCEventMaster import *


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


EvMaster = EventMaster(freq=20)            # Создаем мастера событий и запускаем его


evBlockFirst = EventBlock()         # Создаем блок события
evBlockSecond = EventBlock()
evBlockThird = EventBlock()
evBlockFourth = EventBlock()

evBlockFirst.setfun(firstfun)       # Привязываем ф-ию к событию
evBlockSecond.setfun(secondfun)
evBlockThird.setfun(thirdfun)
evBlockFourth.setfun(fourthfun)


EvMaster.append(evBlockFirst)    # Добавляем блок события в EM
EvMaster.append(evBlockSecond)
EvMaster.append(evBlockThird)
EvMaster.append(evBlockFourth)

EvMaster.start()

evBlockFirst.push()                 # Вызываем событие
evBlockSecond.push()
evBlockThird.push("Ye")
time.sleep(1)
evBlockFourth.push("a", 3, 1, 6)

time.sleep(3)

EvMaster.exit()