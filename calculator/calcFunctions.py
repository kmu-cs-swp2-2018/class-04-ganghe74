from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        if n > 100000:
            raise Exception
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000 or n<=0:
        return 'Error!'
    
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(numStr):
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]
    numStrBackup = numStr
    result = 0
    for value, letters in romans:
        count = 0
        while numStr[:len(letters)] == letters:
            numStr = numStr[len(letters):]
            result += value
            count += 1

    if decToRoman(result) != numStrBackup:
        return 'Error!'
    return result

if __name__ == '__main__':
    print("romanToDec Test")
    s = input()
    print(romanToDec(s))

    for i in range(1,4000):
        if romanToDec(decToRoman(i)) != i:
            print('error at :', i)