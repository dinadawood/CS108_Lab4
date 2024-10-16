"""
Course: CISC108
Assignment: Lab 4
Author: Dina Dawood
"""

from cisc108 import assertEqual

def calculate_grade(lab_score, test_score):
    '''
    Computes grade
    Parameters:
        lab_score: (float) - sum of student's lab scores
        test_score: (float) - sum of student's test scores
    Returns:
        grade: (float) - student's course grade
    '''
# grade is the student's calculated course grade
    grade = (lab_score + test_score) / 290
    return grade

assertEqual(round(calculate_grade(83.2, 177.6),2), 0.9)
assertEqual(round(calculate_grade(69, 190.1),2), 0.89)
########################################################
# Problem 1:

assertEqual(round(calculate_grade(89, 188.5),2), 0.96)
assertEqual(round(calculate_grade(55, 145.7),2), 0.69)
assertEqual(round(calculate_grade(73.9, 178.1),2), 0.87)

# Problem 2:

lab_score = float(input("Enter Lab Score: "))
test_score = float(input("Enter Test Score: "))
course_grade = round(calculate_grade(lab_score, test_score),2)
print("Course grade is: ", course_grade)

# Problem 3:

def greeting(name):
    print("Hello, ", name)
    
# Problem 4:

def miles_to_kilometers(number):
    mile_inKilom = 1.6
    return number * mile_inKilom

assertEqual(miles_to_kilometers(10),16.0)
assertEqual(miles_to_kilometers(15),24.0)
assertEqual(miles_to_kilometers(35),56.0)
    
# Problem 5:

def multiply(a, b):
    return a*b

assertEqual(multiply(3,2),6)
assertEqual(multiply(10,-1),-10)
assertEqual(multiply(0.5,4.5),2.25)
    
# Problem 6:

def calculate_triangle_area(height, base):
    '''
    Computes the area of a triangle given its height and base lengths
    Parameters:
        height: (float) - length of the triangle's height
        base: (float) - length of the triangle's base
    Returns:
        area of the triangle: (float)
    '''
    area = (height * base)/2
    return area

assertEqual(round(calculate_triangle_area(5.0, 2.5),2),6.25)
assertEqual(round(calculate_triangle_area(1.0, 1.0),2),0.5)
assertEqual(round(calculate_triangle_area(.001, 5000.32),5),2.50016)

# Problem 7:

def pulse_rate(seconds, pulses):
    '''
    Computes the pulse rate given the seconds and pulses counted
    Parameters:
        seconds: (int) - seconds counting pulse
        pulses: (int) - pulses counted
    Returns:
        pulse rate: (float)
    '''
    minute = seconds/60
    return pulses/minute

assertEqual(round(pulse_rate(30, 22),1), 44.0)
assertEqual(round(pulse_rate(23, 54),1), 140.9)
assertEqual(round(pulse_rate(55, 78),1), 85.1)
assertEqual(round(pulse_rate(60, 89),1), 89.0)


# Problem 8:

def graduation_year(year):
    '''
    Computes the year student started and expected graduation
    Parameters:
        year: (int) - year student starts college
    Returns:
        grad year: (int)
    '''
    return year+4

assertEqual(graduation_year(2019), 2023)
assertEqual(graduation_year(2026), 2030)
assertEqual(graduation_year(2005), 2009)

# Problem 9:

def make_string_sandwich(str1, str2):
    '''
    Computes strings and sandwiches them together
    Parameters:
        str1: (str) - random string 1
        str2: (str) - random string 2
    Returns:
        sandwiched strs: (str)
    '''
    return str1+str2+str2+str1

assertEqual(make_string_sandwich("bbb", "a"), "bbbaabbb")
assertEqual(make_string_sandwich("12","3t"), "123t3t12")
assertEqual(make_string_sandwich("Z",""), "ZZ")
assertEqual(make_string_sandwich("123", "boo"), "123booboo123")
assertEqual(make_string_sandwich("99","7s"), "997s7s99")
assertEqual(make_string_sandwich("SAND","wich"), "SANDwichwichSAND")

# Problem 10:

def calculate_manhattan_distance(p1, p2, q1, q2):
    '''
    Computes the sum of horizontal & vertical components and produces the Manhattan distance
    Parameters:
        p1: (int) - random integer 1
        p2: (int) - random integer 2
        q1: (int) - random integer 1
        q2: (int) - random integer 2
    Returns:
        distance btw (p1, p2) and (q1, q2): (int)
    '''
    return (abs(p1-q1) + abs(p2-q2))

assertEqual(calculate_manhattan_distance(1,5,7,9), 10)
assertEqual(calculate_manhattan_distance(20,15,3,45), 47)
assertEqual(calculate_manhattan_distance(8,32,14,6), 32)