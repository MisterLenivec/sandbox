#Nребуется написать программу, на вход которой подаётся тип фигуры и соответствующие параметры,
# которая бы выводила получившуюся площадь.
#Формат ввода:
#треугольник
#a
#b
#c
#где a, b и c — длины сторон треугольника
#прямоугольник
#a
#b
#где a и b — длины сторон прямоугольника
#круг
#r
#где r — радиус окружности

f = input("")

if (f == "прямоугольник"):
  a = float(input())
  b = float(input())
  print(a * b)
elif (f == "круг"):
  r = float(input())
  print((r*r) * 3.14)
elif (f == "треугольник"):
  a = int(input())
  b = int(input())
  c = int(input())
  p = (a + b + c) / 2
  s = (p *(p - a)*(p - b)*(p - c)) ** 0.5
  print(s)