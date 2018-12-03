romans = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
    (1, "I")
]

def decToRoman(num):
    answer = ""
    for value, letters in romans:
        while num >= value:
            answer += letters
            num -= value
    return answer

def solution(numstr):
    numstrBackup = numstr
    answer = 0
    for value, letters in romans:
        while numstr[:len(letters)] == letters:
            numstr = numstr[len(letters):]
            answer += value
    if decToRoman(answer) != numstrBackup:
        return -1
    return answer
