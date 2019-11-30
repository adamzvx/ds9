# BUILD IN FUNCTION AND MODUL
from math import factorial
from datetime import datetime

numbers =[1,2,3,4,5]
number  =12345

print(abs(-number))
print(abs(number))
print('apakah ',number ,' tipe data list ? ' ,isinstance(number,list))
print('apakah ',numbers ,' tipe data list ? ' ,isinstance(numbers,list))
print('angka terkecil...',min(numbers))
print('angka terbesar...',max(numbers))

bahasa=['py','go','js','cpp']
print('posisi bahasa go pada index...',bahasa.index('go'))

#build in string
#capitilize, replace

print(factorial(6))
print(datetime.now())
