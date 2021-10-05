from math import *
from random import randint

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def isCrossed(a,b,c,d):
    #Первый отрезок
    x1_1=a.x
    y1_1=a.y
    x1_2 = b.x
    y1_2 = b.y
    #Второй отрезок
    x2_1 = c.x
    y2_1 = c.y
    x2_2 = d.x
    y2_2 = d.y

    A1 = y1_1 - y1_2
    B1 = x1_2 - x1_1
    C1 = x1_1 * y1_2 - x1_2 * y1_1
    A2 = y2_1 - y2_2
    B2 = x2_2 - x2_1
    C2 = x2_1 * y2_2 - x2_2 * y2_1
    if B1 * A2 - B2 * A1 != 0:
        y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
        x = (-C1 - B1 * y) / A1
        if min(x1_1, x1_2) <= x <= max(x1_1, x1_2) and \
                min(y1_1, y1_2) <= y <= max(y1_1, y1_2):
                return(True)
        else:
            return(False)

class Figure():
    def __init__(self):
        self.plosh=self.ploshad()
        self.perim=self.perimetr()
    def perimetr(self):
        pass
    def ploshad(self):
        pass
    def ShowClass(self):
        return("Фигура")

class Point():
    def __init__(self, xp,yp):
        self.x,self.y=xp,yp
    def change(self, xnew, ynew):
        self.x, self.y=xnew, ynew
        pass
    def vyvod(self):
        print("("+str(self.x)+", "+str(self.y)+")")
        pass

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.sides=[float(toFixed(sqrt((b.x-a.x)**2+(b.y-a.y)**2), accuracy)),
                    float(toFixed(sqrt((c.x-b.x)**2+(c.y-b.y)**2), accuracy)),
                    float(toFixed(sqrt((a.x-c.x)**2+(a.y-c.y)**2), accuracy))]
        self.corners=[a,b,c]
        self.plosh = self.ploshad()
        self.perim = self.perimetr()
    def perimetr(self):
        return(float(toFixed(sum(self.sides), accuracy)))
    def ploshad(self):
        p=self.perimetr()/2
        return(float(toFixed(sqrt(p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2])),accuracy)))
    def ShowClass(self):
        return("Треугольник")

class Quadrangle(Figure):
    def __init__(self, a, b, c, d):
        self.corners=sorted([a,b,c,d],key=lambda x: x.x)
        if isCrossed(self.corners[0],self.corners[1],self.corners[2],self.corners[3]):
            self.corners[2],self.corners[1]=self.corners[1],self.corners[2]
        elif isCrossed(self.corners[0],self.corners[3],self.corners[1],self.corners[2]):
            self.corners[2], self.corners[3] = self.corners[3], self.corners[2]
        self.sides=[float(toFixed(sqrt((b.x-a.x)**2+(b.y-a.y)**2), accuracy)),
                    float(toFixed(sqrt((c.x-b.x)**2+(c.y-b.y)**2), accuracy)),
                    float(toFixed(sqrt((d.x-c.x)**2+(d.y-c.y)**2), accuracy)),
                    float(toFixed(sqrt((d.x-a.x)**2+(d.y-a.y)**2), accuracy))]
        self.plosh=self.ploshad()
        self.perim=self.perimetr()
    def perimetr(self):
        return (float(toFixed(sum(self.sides), accuracy)))
    def ploshad(self):
        return (float(toFixed(min(Triangle(self.corners[0], self.corners[1],self.corners[3]).ploshad()+Triangle(self.corners[2], self.corners[1],self.corners[3]).ploshad(), Triangle(self.corners[0], self.corners[1],self.corners[2]).ploshad()+Triangle(self.corners[2], self.corners[0],self.corners[3]).ploshad()),accuracy)))
    def ShowClass(self):
        return("Четырехугольник")

class Circle(Figure):
    def __init__(self,centr, R):
        self.centr=centr
        self.radius=R
        self.plosh=self.ploshad()
        self.perim=self.perimetr()
    def perimetr(self):
        return(float(toFixed(2*pi*self.radius,accuracy)))
    def ploshad(self):
        return(float(toFixed(pi*self.radius**2,accuracy)))
    def ShowClass(self):
        return("Круг")

def CreateTriangle(A, a_point, b_point, c_point):
    A.append(Triangle(a_point, b_point, c_point))
    print("Треугольник создан")
    return(A[-1])

def CreateRandomTriangle(A):
    A.append(Triangle(Point(randint(-100, 100), randint(-100, 100)), Point(randint(-100, 100), randint(-100, 100)), Point(randint(-100, 100), randint(-100, 100))))
    print("Треугольник создан")
    return (A[-1])

def CreateQuadrangle(A,a_point, b_point, c_point, d_point):
    A.append(Quadrangle(a_point, b_point, c_point, d_point))
    print("Прямоугольник создан")
    return (A[-1])

def CreateRandomQuadrangle(A):
    a_point=Point(randint(-100, 100), randint(-100, 100))
    b_point=Point(randint(-100, 100), randint(-100, 100))
    c_point=Point(randint(-100, 100), randint(-100, 100))
    d_point=Point(randint(-100, 100), randint(-100, 100))
    A.append(Quadrangle(a_point, b_point, c_point, d_point))
    print("Четырехугольник создан")
    return (A[-1])

def CreateCircle(A, centr, R):
    A.append(Circle(centr,R))
    print("Круг создан")
    return(A[-1])

def CreateRandomCircle(A):
    A.append(Circle(Point(randint(-100, 100), randint(-100,100)),randint(0,100)))
    print("Круг создан")
    return(A[-1])

figures=[]
accuracy=2

if __name__ == '__main__':
    k=1
    while k:
        k = int(input("\nВыберите действие:\n"
                      "Для создания треугольника-введите 1\n"
                      "Для создания четырехугольника-введите 2\n"
                      "Для создания круга-введите 3\n"
                      "Для вывода списка фигур-введите 4\n"
                      "Для вывода площади и периметра фигуры-введите 5\n"
                      "Для сортировки массива по периметру-введите 6\n"
                      "Для сортировки массива по площади-введите 7\n"
                      "Для изменения точности измерения-введите 9\n"
                      "Для выхода-введите 0\n"))

        if k==1:
            key = int(input("\nДля создания треугольника по заданным координатам-введите 1\n"
                            "Для создания случайного треугольника-введите 2\n"))
            if key - 1:
                CreateRandomTriangle(figures)
            else:
                x1,y1=map(float, input("Введите координаты первой точки: ").split())
                x2,y2=map(float, input("Введите координаты второй точки: ").split())
                x3,y3=map(float, input("Введите координаты третьей точки: ").split())
                CreateTriangle(figures, Point(x1,y1), Point(x2,y2), Point(x3,y3))

        elif k==2:
            key = int(input("\nДля создания четырехугольника по заданным координатам-введите 1\n"
                            "Для создания случайного четырехугольника-введите 2\n"))
            if key - 1:
                CreateRandomQuadrangle(figures)
            else:
                x1,y1=map(float, input("Введите координаты первой точки: ").split())
                x2,y2=map(float, input("Введите координаты второй точки: ").split())
                x3,y3=map(float, input("Введите координаты третьей точки: ").split())
                x4, y4 = map(float, input("Введите координаты четвертой точки: ").split())
                CreateQuadrangle(figures, Point(x1,y1), Point(x2,y2), Point(x3,y3), Point(x4,y4))

        elif k==3:
            key = int(input("\nДля создания круга по заданным координатам-введите 1\n"
                            "Для создания случайного круга-введите 2\n"))
            if key - 1:
                CreateRandomCircle(figures)
            else:
                x,y=map(float,input("Введите координаты центра: ").split())
                R=float(input("Введите радиус: "))
                CreateCircle(figures,Point(x,y),R)

        elif k==4:
            for i in range(len(figures)):
                print("\n"f"{i+1}-я фигура:\n    {figures[i].ShowClass()}")
                if figures[i].ShowClass()=="Треугольник":
                    for j in range(3):
                        print(f"{j+1}-я точка: ({figures[i].corners[j].x}, {figures[i].corners[j].y})")
                elif figures[i].ShowClass()=="Четырехугольник":
                    for j in range(4):
                        print(f"{j+1}-я точка: {figures[i].corners[j].x,figures[i].corners[j].y}")
                elif figures[i].ShowClass()=="Круг":
                    print(f"Центр: ({figures[i].centr.x}, {figures[i].centr.y})")
                    print(f"Радиус: {figures[i].radius}")
            if not len(figures):
                print("Нет фигур :(")

        elif k==5:
            number=int(input("Введите номер фигуры, периметр которой хотите узнать: ")) - 1
            print("Периметр выбранной фигуры равен:", figures[number].perimetr())
            print("Площадь выбранной фигуры равна:", figures[number].ploshad())

        elif k==6:
            key=int(input("\nЧтобы отсортировать по убыванию-введите 1\n"
                    "Чтобы отсортировать по возрастанию-введите 2\n"))-1
            if not key:
                figures=sorted(figures, key=lambda x: x.perimetr(), reverse=True)
            else:
                figures = sorted(figures, key=lambda x: x.perimetr())
            print("Фигуры отсортированы")

        elif k==7:
            key = int(input("\nЧтобы отсортировать по убыванию-введите 1\n"
                            "Чтобы отсортировать по возрастанию-введите 2\n")) - 1
            if not key:
                figures = sorted(figures, key=lambda x: x.ploshad(), reverse=True)
            else:
                figures = sorted(figures, key=lambda x: x.ploshad())
            print("Фигуры отсортированы")

        elif k==9:
            print("Знаки после запятой:", accuracy)
            accuracy=int(input("Введите новую точность: "))
