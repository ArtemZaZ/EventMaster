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


EvMaster = EventMaster(freq=1)            # Создаем мастера событий и запускаем его


evBlockFirst = EventBlock()         # Создаем блок события
evBlockSecond = EventBlock()

evBlockFirst.setfun(firstfun)       # Привязываем ф-ию к событию
evBlockSecond.setfun(secondfun)

EvMaster.append(evBlockFirst)    # Добавляем блок события в EM
EvMaster.append(evBlockSecond)

EvMaster.start()

evBlockFirst.push()                 # Вызываем событие
evBlockSecond.push()

time.sleep(5)

EvMaster.exit()