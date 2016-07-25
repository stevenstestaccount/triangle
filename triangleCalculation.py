import math

def classifyTriangle(num1, num2, num3):
    
    if verifyTriangle(num1, num2, num3) == 0:
        print("This is not a valid triangle")    
        return "Invalid"
    else:
        angle, rightTriangle = calcRightTriangle(num1, num2, num3)
        triangleType = ""
        if num1 == num2 and num2 == num3 and angle == "Equilateral":
            triangleType = "Equilateral"
        elif num1 != num2 and num2 != num3 and angle == "Scalene":
            triangleType = "Scalene"
        elif num1 == num2 or num2 == num3 or num3 == num1 and angle == "Isosceles":
            triangleType = "Isosceles"
    
        print("Triangle is a(n) {0} {1}".format(triangleType, rightTriangle))
        
        return "{0} {1}".format(triangleType, rightTriangle).strip()


def angle (a, b, c):
    return round(math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b))), 0)
    
def verifyTriangle(a, b, c):
        
     # Triangle Inequality Theorem
    side1 = a + b
    side2 = b + c
    side3 = a + c

    isTriangle = 0

    if side1 > c and side2 > a and side3 > b:
        isTriangle = 1

    return isTriangle


def calcRightTriangle(a, b, c):
   
    angle1 = angle(a,b,c)
    angle2 = angle(b,c,a)
    angle3 = angle(c,a,b)

    rightAngle = ""
    angleType = ""

    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        rightAngle = "Right Triangle"

    if angle1 == 60 and angle2 == 60 and angle3 == 60:
        angleType = "Equilateral"    
    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        angleType = "Isosceles"
    elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3:
        angleType = "Scalene"

    print("RightAngle: {0}, Angle1: {1}, Angle2: {2}, Angle3: {3}".format(rightAngle, angle1, angle2, angle3))

    return angleType, rightAngle

if __name__ == "__main__":
    
    valid1 = False
    valid2 = False
    valid3 = False
    
    while valid1 == False:
        num1 = raw_input("Enter side 1 of triangle: ")       
        if num1.isdigit() == True:
            valid1 = True
            num1 = float(num1)
        else:
            print("...Please enter a valid number")
    
    while valid2 == False:
        num2 = raw_input("Enter side 2 of triangle: ")       
        if num2.isdigit() == True:
            valid2 = True
            num2 = float (num2)
        else:
            print("...Please enter a valid number") 
            
    while valid3 == False:
        num3 = raw_input("Enter side 3 of triangle: ")       
        if num3.isdigit() == True:
            valid3 = True
            num3 = float(num3)
        else:
            print("...Please enter a valid number")


    classifyTriangle(num1, num2, num3)
   
        
print ("All Done!")
