from math import *
from random import randint

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def side_len(a,b):
    return float(toFixed(sqrt((b.x-a.x)**2+(b.y-a.y)**2+(b.z-a.z)**2), accuracy))

def isCrossed(a,b,c,d):
    # Первый отрезок
    x1_1 = a.x
    y1_1 = a.y
    x1_2 = b.x
    y1_2 = b.y
    # Второй отрезок
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
            return (True)
        else:
            return (False)

class Figure():
    def __init__(self):
        self.second_demension = second_demension
        self.third_demension = third_demension
        self.polar_system = polar_system
        self.cylindrical_system = cylindrical_system
        self.centr = Point(0,0,0,0,0)
        self.corners = []
        self.radius = 0
        if self.second_demension:
            self.system = "Плоская декартова система координат"
        elif self.third_demension:
            self.system = "Объемная декартова система координат"
        elif self.polar_system:
            self.system = "Полярная система координат"
        elif cylindrical_system:
            self.system = "Цилиндрическая система координат"
    def perimetr(self):
        pass
    def ploshad(self):
        pass
    def ShowClass(self):
        return("Фигура")
    def vyvod(self):
        if self.second_demension:
            if self.ShowClass() == "Треугольник":
                for j in range(3):
                    print(f"{j + 1}-я точка: ({self.corners[j].x}, {self.corners[j].y})")
            elif self.ShowClass() == "Четырехугольник":
                for j in range(4):
                    print(f"{j + 1}-я точка: {self.corners[j].x, self.corners[j].y}")
            elif self.ShowClass() == "Круг":
                print(f"Центр: ({self.centr.x}, {self.centr.y})")
                print(f"Радиус: {self.radius}")
            print(f"Периметр: {self.perimetr()}")
            print(f"Площадь: {self.ploshad()}")

        elif self.third_demension:
            if self.ShowClass() == "Треугольник":
                for j in range(3):
                    print(f"{j + 1}-я точка: ({self.corners[j].x}, {self.corners[j].y}, {self.corners[j].z})")
            elif self.ShowClass() == "Четырехугольник":
                for j in range(4):
                    print(f"{j + 1}-я точка: {self.corners[j].x, self.corners[j].y, self.corners[j].z}")
            elif self.ShowClass() == "Круг":
                print(f"Центр: ({self.centr.x}, {self.centr.y}, {self.centr.z})")
                print(f"Радиус: {self.radius}")
            print(f"Периметр: {self.perimetr()}")
            print(f"Площадь: {self.ploshad()}")

        elif self.polar_system:
            if self.ShowClass() == "Треугольник":
                for j in range(3):
                    print(f"{j + 1}-я точка: {self.corners[j].ro, self.corners[j].alfa}")
            elif self.ShowClass() == "Четырехугольник":
                for j in range(4):
                    print(f"{j + 1}-я точка: {self.corners[j].ro, self.corners[j].alfa}")
            elif self.ShowClass() == "Круг":
                print(f"Центр: {self.centr.ro, self.centr.alfa}")
                print(f"Радиус: {self.radius}")
            print(f"Периметр: {self.perimetr()}")
            print(f"Площадь: {self.ploshad()}")

        elif self.cylindrical_system:
            if self.ShowClass() == "Треугольник":
                for j in range(3):
                    print(f"{j + 1}-я точка: {self.corners[j].ro, self.corners[j].alfa, self.corners[j].z}")
            elif self.ShowClass() == "Четырехугольник":
                for j in range(4):
                    print(f"{j + 1}-я точка: {self.corners[j].ro, self.corners[j].alfa, self.corners[j].z}")
            elif self.ShowClass() == "Круг":
                print(f"Центр: ({self.centr.ro, self.centr.alfa, self.centr.z})")
                print(f"Радиус: {self.radius}")
            print(f"Периметр: {self.perimetr()}")
            print(f"Площадь: {self.ploshad()}")

    def vyvod_file(self, file):
        if self.second_demension:
            if self.ShowClass() == "Треугольник":
                for j in range(3):
                    file.write(f"{j + 1}-я точка: ({self.corners[j].x}, {self.corners[j].y})\n")
            elif self.ShowClass() == "Четырехугольник":
                for j in range(4):
                    file.write(f"{j + 1}-я точка: {self.corners[j].x, self.corners[j].y}\n")
            elif self.ShowClass() == "Круг":
                file.write(f"Центр: ({self.centr.x}, {self.centr.y})\n")
                file.write(f"Радиус: {self.radius}\n")
            file.write(f"Периметр: {self.perimetr()}\n")
            file.write(f"Площадь: {self.ploshad()}\n\n")

        elif self.third_demension:
            if self.ShowClass() == "Треугольник":
                for j in range(3):
                    file.write(f"{j + 1}-я точка: ({self.corners[j].x}, {self.corners[j].y}, {self.corners[j].z})\n")
            elif self.ShowClass() == "Четырехугольник":
                for j in range(4):
                    file.write(f"{j + 1}-я точка: {self.corners[j].x, self.corners[j].y, self.corners[j].z}\n")
            elif self.ShowClass() == "Круг":
                file.write(f"Центр: ({self.centr.x}, {self.centr.y}, {self.centr.z})\n")
                file.write(f"Радиус: {self.radius}\n")
            file.write(f"Периметр: {self.perimetr()}\n")
            file.write(f"Площадь: {self.ploshad()}\n")

        elif self.polar_system:
            if self.ShowClass() == "Треугольник":
                for j in range(3):
                    file.write(f"{j + 1}-я точка: {self.corners[j].ro, self.corners[j].alfa}\n")
            elif self.ShowClass() == "Четырехугольник":
                for j in range(4):
                    file.write(f"{j + 1}-я точка: {self.corners[j].ro, self.corners[j].alfa}\n")
            elif self.ShowClass() == "Круг":
                file.write(f"Центр: {self.centr.ro, self.centr.alfa}\n")
                file.write(f"Радиус: {self.radius}\n")
            file.write(f"Периметр: {self.perimetr()}\n")
            file.write(f"Площадь: {self.ploshad()}\n")

        elif self.cylindrical_system:
            if self.ShowClass() == "Треугольник":
                for j in range(3):
                    file.write(f"{j + 1}-я точка: {self.corners[j].ro, self.corners[j].alfa, self.corners[j].z}\n")
            elif self.ShowClass() == "Четырехугольник":
                for j in range(4):
                    file.write(f"{j + 1}-я точка: {self.corners[j].ro, self.corners[j].alfa, self.corners[j].z}\n")
            elif self.ShowClass() == "Круг":
                file.write(f"Центр: ({self.centr.ro, self.centr.alfa, self.centr.z})\n")
                file.write(f"Радиус: {self.radius}\n")
            file.write(f"Периметр: {self.perimetr()}\n")
            file.write(f"Площадь: {self.ploshad()}\n")

class Point():
    def __init__(self, xp, yp, zp, ro, alfa):
        self.x,self.y, self.z = xp, yp, zp
        self.ro = ro
        self.alfa = alfa
    def change(self, xnew, ynew, znew):
        self.x, self.y, self.z = xnew, ynew, znew
        pass
    def vyvod(self):
        print("("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")")
        pass

class Triangle(Figure):
    def __init__(self, a, b, c):
        Figure.__init__(self)
        self.sides=[side_len(a, b),
                    side_len(c, b),
                    side_len(c, a)]
        self.corners=[a, b, c]
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
        Figure.__init__(self)
        self.corners=sorted([a,b,c,d],key=lambda x: x.x)
        if isCrossed(self.corners[0],self.corners[1],self.corners[2],self.corners[3]):
            self.corners[2],self.corners[1]=self.corners[1],self.corners[2]
        elif isCrossed(self.corners[0],self.corners[3],self.corners[1],self.corners[2]):
            self.corners[2], self.corners[3] = self.corners[3], self.corners[2]
        self.sides=[side_len(a, b),
                    side_len(c, b),
                    side_len(c, d),
                    side_len(a, d)]
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
        Figure.__init__(self)
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

def CreateRandomPoint():
    if third_demension:
        return Point(randint(-100, 100), randint(-100, 100), randint(-100, 100), randint(-100, 100), randint(-100, 100))
    else:
        return Point(randint(-100, 100), randint(-100, 100), 0, randint(-100, 100), randint(-100, 100))

def CreateTriangle(A, a_point, b_point, c_point):
    A.append(Triangle(a_point, b_point, c_point))
    print("Треугольник создан")
    return(A[-1])

def CreateRandomTriangle(A):
    A.append(Triangle(CreateRandomPoint(),CreateRandomPoint(),CreateRandomPoint()))
    print("Треугольник создан")
    return (A[-1])

def CreateQuadrangle(A,a_point, b_point, c_point, d_point):
    A.append(Quadrangle(a_point, b_point, c_point, d_point))
    print("Прямоугольник создан")
    return (A[-1])

def CreateRandomQuadrangle(A):
    a_point = CreateRandomPoint()
    b_point = CreateRandomPoint()
    c_point = CreateRandomPoint()
    d_point = CreateRandomPoint()
    A.append(Quadrangle(a_point, b_point, c_point, d_point))
    print("Четырехугольник создан")
    return (A[-1])

def CreateCircle(A, centr, R):
    A.append(Circle(centr,R))
    print("Круг создан")
    return(A[-1])

def CreateRandomCircle(A):
    A.append(Circle(CreateRandomPoint(), randint(0,100)))
    print("Круг создан")
    return(A[-1])

def CreatePoint(): #Важнейшая
    if second_demension:
        x, y = map(float, input("x y = ").split())
        return Point(x, y, 0, 0, 0)
    elif third_demension:
        x, y, z = map(float, input("x y z = ").split())
        return Point(x, y, z, 0, 0)
    elif polar_system:
        p, a = map(float, input("p a = ").split())
        return Point(p*cos(a), p*sin(a), 0, p, a)
    elif cylindrical_system:
        p, a, z = map(float, input("p a z = ").split())
        return Point(p*cos(a), p*sin(a), z, p, a)

def CreatePoint_file(lines, line):
    if second_demension:
        x, y = map(float, lines[line].split())
        return Point(x, y, 0, 0, 0)
    elif third_demension:
        x, y, z = map(float, lines[line].split())
        return Point(x, y, z, 0, 0)
    elif polar_system:
        p, a = map(float, lines[line].split())
        return Point(p*cos(a), p*sin(a), 0, p, a)
    elif cylindrical_system:
        p, a, z = map(float, lines[line].split())
        return Point(p*cos(a), p*sin(a), z, p, a)

def add_from_file(A, in_lines, curren_line):
    global second_demension, third_demension, polar_system, cylindrical_system
    while curren_line < len(in_lines):
        if in_lines[curren_line] == "Triangle":
            curren_line+=1
            system = in_lines[curren_line]
            curren_line+=1

            if system == "SD":
                second_demension = True
                third_demension = False
                polar_system = False
                cylindrical_system = False

            elif system == "TD":
                second_demension = False
                third_demension = True
                polar_system = False
                cylindrical_system = False

            elif system == "PS":
                second_demension = False
                third_demension = False
                polar_system = True
                cylindrical_system = False

            elif system == "CS":
                second_demension = False
                third_demension = False
                polar_system = False
                cylindrical_system = True

            points = []

            for i in range(3):
                points.append(CreatePoint_file(in_lines, curren_line))
                curren_line += 1
            CreateTriangle(A, points[0], points[1], points[2])
            curren_line += 1
            
        elif in_lines[curren_line] == "Quadrangle":
            curren_line += 1
            system = in_lines[curren_line]
            curren_line += 1

            if system == "SD":
                second_demension = True
                third_demension = False
                polar_system = False
                cylindrical_system = False

            elif system == "TD":
                second_demension = False
                third_demension = True
                polar_system = False
                cylindrical_system = False

            elif system == "PS":
                second_demension = False
                third_demension = False
                polar_system = True
                cylindrical_system = False

            elif system == "CS":
                second_demension = False
                third_demension = False
                polar_system = False
                cylindrical_system = True

            points = []

            for i in range(4):
                points.append(CreatePoint_file(in_lines, curren_line))
                curren_line += 1
            CreateQuadrangle(A, points[0], points[1], points[2], points[3])
            curren_line += 1

        elif in_lines[curren_line] == "Circle":
            curren_line += 1
            system = in_lines[curren_line]
            curren_line += 1

            if system == "SD":
                second_demension = True
                third_demension = False
                polar_system = False
                cylindrical_system = False

            elif system == "TD":
                second_demension = False
                third_demension = True
                polar_system = False
                cylindrical_system = False

            elif system == "PS":
                second_demension = False
                third_demension = False
                polar_system = True
                cylindrical_system = False

            elif system == "CS":
                second_demension = False
                third_demension = False
                polar_system = False
                cylindrical_system = True

            center = CreatePoint_file(in_lines, curren_line)
            curren_line += 1
            radius = float(in_lines[curren_line])
            curren_line+=1
            CreateCircle(A, center, radius)
            curren_line += 1

figures=[]

accuracy = 2

second_demension = True
third_demension = False
polar_system = False
cylindrical_system = False
current_system = "Плоская декартова система координат"

file_in = False
file_out = False

if __name__ == '__main__':
    k=1
    while k:
        k = int(input("\nВыберите действие:\n"
                      "Для создания треугольника - введите 1\n"
                      "Для создания четырехугольника - введите 2\n"
                      "Для создания круга - введите 3\n"
                      "Для вывода списка фигур - введите 4\n"
                      "Для сортировки массива по периметру - введите 5\n"
                      "Для сортировки массива по площади - введите 6\n"
                      "Для работы с файлами - введите 7\n"
                      "Для изменения системы координат - введите 8\n"
                      "Для изменения точности измерения - введите 9\n"
                      "Для выхода - введите 0\n\n"))

        if k==1:
            key = int(input("\nДля создания треугольника по заданным координатам-введите 1\n"
                            "Для создания случайного треугольника-введите 2\n"))
            if key - 1:
                CreateRandomTriangle(figures)
            else:
                print("Введите координаты первой точки: ")
                a=CreatePoint()
                print("Введите координаты второй точки: ")
                b=CreatePoint()
                print("Введите координаты третьей точки: ")
                c=CreatePoint()
                CreateTriangle(figures, a, b, c)

        elif k==2:
            key = int(input("\nДля создания четырехугольника по заданным координатам-введите 1\n"
                            "Для создания случайного четырехугольника-введите 2\n"))
            if key - 1:
                CreateRandomQuadrangle(figures)
            else:
                print("Введите координаты первой точки: ")
                a = CreatePoint()
                print("Введите координаты второй точки: ")
                b = CreatePoint()
                print("Введите координаты третьей точки: ")
                c = CreatePoint()
                print("Введите координаты четвертой точки: ")
                d = CreatePoint()
                CreateQuadrangle(figures, a,b,c,d)

        elif k==3:
            key = int(input("\nДля создания круга по заданным координатам-введите 1\n"
                            "Для создания случайного круга-введите 2\n"))
            if key - 1:
                CreateRandomCircle(figures)
            else:
                print("Введите координаты центра: ")
                center=CreatePoint()
                R=float(input("Введите радиус: "))
                CreateCircle(figures, center, R)

        elif k==4:
            if not file_out:
                for i in range(len(figures)):
                    print(f"\n{i+1}-я фигура:\n{figures[i].ShowClass()}\nСистема координат: {figures[i].system}")
                    figures[i].vyvod()
                if not len(figures):
                    print("Нет фигур :(")
            else:
                otp = open("output.txt", "w", encoding="UTF-8")
                for i in range(len(figures)):
                    otp.write(f"{i+1}-я фигура:\n{figures[i].ShowClass()}\nСистема координат: {figures[i].system}\n")
                    figures[i].vyvod_file(otp)
                if not len(figures):
                    otp.write("Нет фигур :(\n")
                print("Список фигур выведен в файл")
                otp.close()

        elif k==5:
            key = int(input("\nЧтобы отсортировать по убыванию-введите 1\n"
                            "Чтобы отсортировать по возрастанию-введите 2\n")) - 1
            if not key:
                figures = sorted(figures, key=lambda x: x.perimetr(), reverse=True)
            else:
                figures = sorted(figures, key=lambda x: x.perimetr())
            print("Фигуры отсортированы")

        elif k==6:
            key = int(input("\nЧтобы отсортировать по убыванию-введите 1\n"
                            "Чтобы отсортировать по возрастанию-введите 2\n")) - 1
            if not key:
                figures = sorted(figures, key=lambda x: x.ploshad(), reverse=True)
            else:
                figures = sorted(figures, key=lambda x: x.ploshad())
            print("Фигуры отсортированы")

        elif k==7:
            key = int(input("Для вывода справки - введите 0\n"
                            "Для включения/выключения вывода в файл - введите 1\n"
                            "Для ввода из файла - введите 2\n"))
            if key == 0:
                print("При включении работы с файлами, по умолчанию используются следующие файлы\n"
                      "Ввод производится из файла input.txt\n"
                      "Вывод производится в output.txt\n"
                      "Ввод необходимо проводить в следуюем формате:\n"
                      "Наименование типа фигуры (Triangle, Quadrangle, Circle)\n"
                      "Название системы координат (SD, TD, PS, CS)\n"
                      "В следующих n строках вводятся координаты точек в выбранной системе координат\n"
                      "(Для треугольника n=3. Для четырехугольника n=4. Для круга n=1)\n"
                      "В случае создания круга в следующей строчке вводится радиус, иначе ничего\n")

            elif key == 1:
                file_out = not file_out
                if file_out:
                    print("Включен вывод в файл\n")
                else:
                    print("Выключен вывод в файл\n")

            elif key == 2:
                inp = open("input.txt", "r")
                inp_lines = inp.read().split("\n")
                current_line = 0
                add_from_file(figures, inp_lines, current_line)
                print("Фигуры из файла считаны\n")

        elif k==8:
            print(f"Текущая система координат: {current_system}")
            print("Выберите новую:")
            if not second_demension:
                print("Для выбора плоской декартовой системы координат - введите 1")
            if not third_demension:
                print("Для выбора объемной декартовой системы координат - введите 2")
            if not polar_system:
                print("Для выбора полярной системы координат - введите 3")
            if not cylindrical_system:
                print("Для выбора цилиндрической системы координат - введите 4")
            key = int(input())
            if key == 1:
                second_demension = True
                third_demension = False
                polar_system = False
                cylindrical_system = False
                current_system = "Плоская декартова система координат"
                print(f"Выбрана {current_system}\n")
            elif key == 2:
                second_demension = False
                third_demension = True
                polar_system = False
                cylindrical_system = False
                current_system = "Объемная декартова система координат"
                print(f"Выбрана {current_system}\n")
            elif key == 3:
                second_demension = False
                third_demension = False
                polar_system = True
                cylindrical_system = False
                current_system = "Полярная система координат"
                print(f"Выбрана {current_system}\n")
            elif key == 4:
                second_demension = False
                third_demension = False
                polar_system = False
                cylindrical_system = True
                current_system = "Цилиндрическая система координат"
                print(f"Выбрана {current_system}\n")

        elif k==9:
            print("Знаки после запятой:", accuracy)
            accuracy=int(input("Введите новую точность: "))
