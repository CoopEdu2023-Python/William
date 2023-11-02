def convertToTitle(self, columnNumber: int) -> str:
    if not columnNumber:
        return ""
    remainder = (columnNumber - 1) % 26
    columnNumber = (columnNumber - 1) // 26
    return self.convertToTitle(columnNumber) + chr(65 + remainder)
