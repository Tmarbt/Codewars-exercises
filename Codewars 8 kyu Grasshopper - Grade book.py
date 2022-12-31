# 8 kyu Grasshopper - Grade book
'''
DESCRIPTION:
Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
'''
def get_grade(s1, s2, s3):
    x = (s1 + s2 + s3) / 3
    if x <= 100 and x >= 90:
        return "A"
    elif x <= 90 and x >= 80:
        return "B"
    elif x <= 80 and x >= 70:
        return "C"
    elif x <= 70 and x >= 60:
        return "D"
    else: 
        return "F"