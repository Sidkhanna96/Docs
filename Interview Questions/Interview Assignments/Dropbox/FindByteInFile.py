"""
Given a pattern of bytes, return true if the pattern is a subarray of the file content.
"""


class FindByteInFile:
    def findPatternConsist(self, fileByte, patternByte):
        start = 0
        pI = 0

        for i, f in enumerate(fileByte):
            if f == patternByte[pI]:
                pI += 1
            else:
                start = i
                pI = 0

            if pI > len(patternByte) and (i - start + 1) == len(patternByte):
                return True

        return False
