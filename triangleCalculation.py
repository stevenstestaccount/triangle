import math

def classifyTriangle(num1, num2, num3):
    angle, rightTriangle = calcRightTriangle(num1, num2, num3)
    triangleType = ""
    if num1 == num2 and num2 == num3 and angle == "Equilateral":
        triangleType = "Equilateral"
    elif num1 != num2 and num2 != num3 and angle == "Scalene":
        triangleType = "Scalene"
    elif num1 == num2 or num2 == num3 or num3 == num1 and angle == "Isosceles":
        triangleType = "Isosceles"

    print("Triangle is a(n) {0} {1}".format(triangleType, rightTriangle))


def calcRightTriangle(num1, num2, num3):

    angle1 = round(math.degrees(math.acos((num1 * num1 + num2 * num2 - num3 * num3)/(2.0 * num2 * num3))), 0)
    angle2 = round(math.degrees(math.acos((num1 * num1 + num2 * num2 - num3 * num3)/(2.0 * num1 * num2))), 0)
    angle3 = round(math.degrees(math.acos((num1 * num1 + num2 * num2 - num3 * num3)/(2.0 * num1 * num3))), 0)

    rightAngle = ""
    angleType = ""

    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        rightAngle = "Right Triangle"

    if angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        angleType = "Isosceles"
    elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3:
        angleType = "Scalene"
    elif angle1 == 60 and angle2 == 60 and angle3 == 60:
        angleType = "Equilateral"

    print("RightAngle: {0}, Angle1: {1}, Angle2: {2}, Angle3: {3}".format(rightAngle, angle1, angle2, angle3))

    return angleType, rightAngle

if __name__ == "__main__":
    num1 = input("Enter side 1 of triangle: ")
    num2 = input("Enter side 2 of triangle: ")
    num3 = input("Enter side 3 of triangle: ")

    classifyTriangle(num1, num2, num3)