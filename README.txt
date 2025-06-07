Позволяет преобразовать считанную прошивку с помощью  Silicon Laboratories Flash Utility в Intel Hex
В скрипте указаны начальный и конечный адрес по которому необходимо сформировать Ihex.

использование:
-Запустить Silicon Laboratories Flash Utility и подключиться к МК с помощью Silicon Labs USB Debugger
-Выбрать Get Memmory
-В меню Select Memmory выбрать Code
-Указать Starting addr и Ending addr
-выбрать дерикторию и вбить имя файла (пример firmware.bin)
-Программа должна сформировать файл с hex данными в asci в следующем формате:
0F
28
30
60
ff
12
21
и т.д
-запустить скрипт, пример python convert.python
Скрипт сформирует файл с подобным содержимым:
:10000000HEXHEXHEXHEXHEXHEXHEXHEXHEXHEXHEFF
:10001000HEXHEXHEXHEXHEXHEXHEXHEXHEXHEXHEFF
---
:10FFF000HEXHEXHEXHEXHEXHEXHEXHEXHEXHEXHEFF
:00000001FF

С помощью этого метода можно сделать дамп прошивки и если залить обратно на то же устройство, то теоретически оно будет работать также
