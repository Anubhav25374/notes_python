import math
def circle_stats(r):
    area = math.pi * r ** 2
    circum = 2 * math.pi *r
    return area, circum

radius = float(input("Enter Radius: "))
a, c = circle_stats(radius)

a = round(a, 2)
c = round(c, 2)
print("Area of circle: ", a)
print("Circumferanc of circle: ", c)