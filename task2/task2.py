import sys


#load file in cmd args
if __name__ == '__main__':
    try:
        namespace1 = sys.argv[1]
        namespace2 = sys.argv[2]
        my_file1 = open(f"{namespace1}")
        circle_list = [tuple(float(j) for j in i.split()) for i in my_file1]
        my_file2 = open(f"{namespace2}")
        dots_list = [tuple(float(j) for j in i.split()) for i in my_file2]
    except IndexError:
        print("Opps. Open cmd: >python task2.py input1.txt input2.txt")
        exit()

#Описание класа окружности
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def dist(self, points):
        return (((self.x - points.x)**2 + (self.y - points.y)**2)**0.5)
class Circle:
    def __init__(self,center, radius):
        self.center = center
        self.radius = radius
    def do_intersect(self, cercles, num_cercles):
        D = self.center.dist(cercles.center)
        if (D > self.radius + cercles.radius):
            return f'{num_cercles} - точка снаружи'
        elif  round(D) == round((self.radius + cercles.radius)):
            return f'{num_cercles} - точка лежит на окружности'
        elif D < round((self.radius + cercles.radius)):
            return f'{num_cercles} - точка внутри'

dota_1 = Point(circle_list[0][0], circle_list[0][1])
dota_cir_1 = Circle(dota_1, circle_list[1][-1])
for i in range(0, 100):
    try:
        dota_0 = Point(dots_list[i][0], dots_list[i][-1])
        dota_cir_0 = Circle(dota_0, radius = 0)
        print(dota_cir_1.do_intersect(dota_cir_0, i))
    except IndexError:
        break