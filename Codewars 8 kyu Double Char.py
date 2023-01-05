# 8 kyu Double Char
'''
DESCRIPTION:
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!
'''
def double_char(s):
    double = ''
    for letter in s:
        double = double + letter*2
    return double  