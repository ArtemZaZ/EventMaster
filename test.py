from RTCEventMaster import *


def firstfun():
    i = 0
    while i < 10:
        print("first" + i)
        i = i + 1


def secondfun():
    i = 0
    while i < 10:
        print("second" + i)
        i = i + 1


EvMaster = EventMaster()            # Создаем мастера событий и запускаем его
EvMaster.start()

evBlockFirst = EventBlock()         # Создаем блок события
evBlockSecond = EventBlock()

evBlockFirst.setfun(firstfun)       # Привязываем ф-ию к событию
evBlockSecond.setfun(secondfun)

EventMaster.append(evBlockFirst)    # Добавляем блок события в EM
EventMaster.append(evBlockSecond)

evBlockFirst.push()                 # Вызываем событие
evBlockSecond.push()

