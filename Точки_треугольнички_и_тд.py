from math import *
from random import randint

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

class Point():
    def __init__(self, xp,yp):
        self.x,self.y=xp,yp
    def change(self, xnew, ynew):
        self.x, self.y=xnew, ynew
        pass
    def vyvod(self):
        print("("+str(self.x)+", "+str(self.y)+")")
        pass

class Triangle():
    def __init__(self, a, b, c):
        self.side1=float(toFixed(sqrt((b.x-a.x)**2+(b.y-a.y)**2), accuracy))
        self.side2=float(toFixed(sqrt((c.x-b.x)**2+(c.y-b.y)**2), accuracy))
        self.side3=float(toFixed(sqrt((a.x-c.x)**2+(a.y-c.y)**2), accuracy))
        self.corner1=a
        self.corner2=b
        self.corner3=c
    def perimetr(self):
        return(float(toFixed(self.side1+self.side2+self.side3, accuracy)))
    def ploshad(self):
        p=self.perimetr()/2
        return(float(toFixed(sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3)),accuracy)))

def CreatePoint(A):
    x,y=map(float, input("Введите координаты новой точки: ").split())
    A.append(Point(x,y))
    print("Точка создана")
    return(A[-1])

def CreateTriangle(A, a_point, b_point, c_point):
    A.append(Triangle(a_point, b_point, c_point))
    print("Треугольник создан")
    return(A[-1])

def CreateRandomPoint(A):
    A.append(Point(randint(-100, 100), randint(-100, 100)))
    print("Точка создана")
    return (A[-1])

def CreateRandomTriangle(A):
    A.append(Triangle(Point(randint(-100, 100), randint(-100, 100)), Point(randint(-100, 100), randint(-100, 100)), Point(randint(-100, 100), randint(-100, 100))))
    print("Треугольник создан")
    return (A[-1])

points=[]
triangles=[]
accuracy=2

if __name__ == '__main__':
    k=1
    while k:
        k = int(input("\nВыберите действие:\n"
                      "Для создания новой точки-введите 1\n"
                      "Для вывода координат точек-введите 2\n"
                      "Для изменения координат точки-введите 3\n"
                      "Для создания нового треугольника-введите 4\n"
                      "Для вывода списка треугольников-введите 5\n"
                      "Для подсчета периметра треугольника-введите 6\n"
                      "Для подсчета площади треугольника-введите 7\n"
                      "Для демонстрации работы программы-введите 8\n"
                      "Для изменения точности измерения-введите 9\n"
                      "Для выхода-введите 0\n"))

        if k==1:
            key=int(input("\nДля создания точки по заданным координатам-введите 1\n"
                          "Для создания случайной точки-введите 2\n"))
            if key-1:
                CreateRandomPoint(points)
            else:
                CreatePoint(points)

        elif k==2:
            for i in range(len(points)):
                print(str(i+1)+"-я точка: ", end="")
                points[i].vyvod()

        elif k==3:
            number=int(input("\nВведите номер точки, которую хотите изменить: "))-1
            xnew,ynew=map(float, input("Введите новые координаты: ").split())
            points[number].change(xnew, ynew)
            print("Изменения внесены")

        elif k==4:
            key = int(input("\nДля создания треугольника по заданным координатам-введите 1\n"
                            "Для создания случайного треугольника-введите 2\n"))
            if key - 1:
                CreateRandomTriangle(triangles)
            else:
                x1,y1=map(float, input("Введите координаты первой точки: ").split())
                x2,y2=map(float, input("Введите координаты второй точки: ").split())
                x3,y3=map(float, input("Введите координаты третьей точки: ").split())
                CreateTriangle(triangles, Point(x1,y1), Point(x2,y2), Point(x3,y3))

        elif k==5:
            for i in range(len(triangles)):
                print(str(i+1)+"-й треугольник:")
                print("Стороны: ", end="")
                print(triangles[i].side1, triangles[i].side2, triangles[i].side3)
                print("Координаты углов: ")
                triangles[i].corner1.vyvod()
                triangles[i].corner2.vyvod()
                triangles[i].corner3.vyvod()
                print()

        elif k==6:
            number=int(input("Введите номер треугольника, периметр которого хотите узнать: ")) - 1
            print("Периметр выбранного треугольника равен:", triangles[number].perimetr())

        elif k==7:
            number=int(input("Введите номер треугольника, площадь которого хотите узнать: ")) - 1
            print("Площадь выбранного треугольника равна:", triangles[number].ploshad())

        elif k==8:
            for i in range(2):
                CreateRandomTriangle(triangles)
            print()
            for i in range(2):
                print("Треугольник", str(i+1)+'-ый:')
                print("Стороны:")
                print(triangles[len(triangles)-1-i].side1)
                print(triangles[len(triangles)-1-i].side2)
                print(triangles[len(triangles)-1-i].side3)
                print()
                print("Координаты вершин:")
                triangles[len(triangles)-1-i].corner1.vyvod()
                triangles[len(triangles)-1-i].corner2.vyvod()
                triangles[len(triangles)-1-i].corner3.vyvod()
                print()
                print("Периметр:")
                print(triangles[len(triangles)-1-i].perimetr())
                print("Площадь:")
                print(triangles[len(triangles)-1-i].ploshad())
                print()
            for i in range(2):
                CreateRandomPoint(points)
            for i in range(2):
                print(str(i + 1) + "-я точка: ", end="")
                points[len(points)-1-i].vyvod()

        elif k==9:
            print("Знаки после запятой:", accuracy)
            accuracy=int(input("Введите новую точность: "))
