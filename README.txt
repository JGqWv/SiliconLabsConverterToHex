Can parse readed firmware by silicon labs USB debug adapter using software silicon labs flash utility.

Using:
-start Silicon Laboratories Flash Utility and connect to the MCU (EFM8, EFMBB2 or any other compatible MCU) using Silicon Labs USB Debugger
-select Get Memmory
-in menu Select Memmory select "Code"
-type Starting addr and Ending addr
-selected output derictory and type name of generated file (example C:\Users\user\Documents\extracted\firmware.bin)
-the program should create file with data in ASCII:
0F
28
30
60
ff
12
21
and ect.
-start script. Example: python convert.python
script will create a file with output in intel hex format:
:10000000HEXHEXHEXHEXHEXHEXHEXHEXHEXHEXHEFF
:10001000HEXHEXHEXHEXHEXHEXHEXHEXHEXHEXHEFF
---
:10FFF000HEXHEXHEXHEXHEXHEXHEXHEXHEXHEXHEFF
:00000001FF

In script you can udjust starting address and ending address.
With this method you can create a full damp of firmware.
