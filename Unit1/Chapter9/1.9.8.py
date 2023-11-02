def plusOne(self, digits: list[int]) -> list[int]:
    return list(map(int, list(str(int(''.join(list(map(str, digits)))) + 1))))
