def romanToInt(self, s: str) -> int:
    dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dict2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    r = 0
    for i in dict2.keys():
        for j in range(s.count(i)):
            s = s.replace(i, '')
            r += dict2[i]
    for i in dict1.keys():
        for j in range(s.count(i)):
            s = s.replace(i, '')
            r += dict1[i]
    return r

