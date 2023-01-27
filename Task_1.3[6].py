# 1.3[6]. Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no
# (*) Усложнение. Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор

billet = int(input('Введите шестизначный номер билета:\n'))
n = billet // 1000
m = billet % 1000
sumN = (n//100) + (n % 100 // 10) + (n % 10)
sumM = (m//100) + (m % 100 // 10) + (m % 10)
print('yes' if sumN == sumM else 'no')