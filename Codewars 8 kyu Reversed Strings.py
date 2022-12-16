# 8 kyu Reversed Strings
'''
DESCRIPTION:
Complete the solution so that it reverses the string passed into it.
'world'  =>  'dlrow'
'word'   =>  'drow'
'''
def solution(string):
    words = string.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence