import math


def equationroots(a, b, c):
    det = b * b - 4 * a * c
    sqrt_det = math.sqrt(abs(det))

    if det > 0:
        print(" real and different roots ")
        print((-b + sqrt_det) / (2 * a))
        print((-b - sqrt_det) / (2 * a))

    elif det == 0:
        print(" real and same roots")
        print(-b / (2 * a))

    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", ((sqrt_det) / (2 * a)))
        print(- b / (2 * a), " - i", ((sqrt_det) / (2 * a)))


a = int(input("Enter coefficient a!\n"))
b = int(input("Enter coefficient b!\n"))
c = int(input("Enter coefficient c!\n"))

if a == 0:
    print("Input correct quadratic equation")

else:
    equationroots(a, b, c)
