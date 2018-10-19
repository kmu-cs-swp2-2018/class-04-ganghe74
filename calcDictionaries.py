import calcFunctions
consDictionary = {
    'pi' : '3.141592',
    '빛의 이동 속도 (m/s)' : '3E+8',
    '소리의 이동 속도 (m/s)' : '340',
    '태양과의 평균 거리 (km)' : '1.5E+8',
}

funcDictionary = {
    'factorial (!)' : calcFunctions.factorial,
    '-> binary' : calcFunctions.decToBin,
    'binary -> dec' : calcFunctions.binToDec,
    '-> roman' : calcFunctions.decToRoman,
}