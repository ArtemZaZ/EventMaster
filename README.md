# RTCEventMaster
Модуль позволяющий работать с событиями
# Import 
Чтобы импортировать данный модуль необходимо в файле программы ввести
```
from RTCEventMaster import *
```
# EventBlock
Класс события со встроенной ф-ией(с пустыми параметрами), которая вызывается при вызове привязанного к ней события
```
ev = EventBlock()
```
### Методы
Установка ф-ии события
```
ev.setfun(f)
```
Вызвать событие
```
ev.push()
```
# EventMaster 
Класс, собирающий события со встроенными ф-иями EventBlock в список событий.
При вызове события из списка событий заполняется очередь событий, функции, привязанные к этим событиям,
выполняются в порядке очереди в разных потоках.
```
EM = EventMaster()
```
### Методы
Запуск Мастера событий 
```
EM.start()
```
Добавление нового события с привязанной ф-ией
```
EM.append(ev)
```
Прекращение работы Мастера событий
```
EM.exit()
```
