class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False

        s = self.removeEmptySpace(s)

        beforeE, afterE, isE = self.splitE(s)

        if isE:
            if not self.isInteger(afterE):
                return False
        return self.isInteger(beforeE) or self.isDecimal(beforeE)

    def removeEmptySpace(self, s):
        """
        :type s: str
        :rtype str
        """
        # remove all the empty space at start and end
        start = 0
        while s[start] == " ":
            start += 1
            if start >= len(s):
                break
        
        end = len(s) - 1
        while s[end] == " ":
            end -= 1
            if end <= 0:
                break
        
        if end >= start:
            return s[start:end+1]
        else:
            return ""

    def splitE(self, s):
        """
        :type s: str
        :rtype (str, str, bool)
        """
        idx = 0
        for c in s:
            if c == "e" or c == "E":
                break
            idx += 1
        if idx != len(s):
            return s[:idx], s[idx+1:], True
        else:
            return s[:idx], "", False

    def isDecimal(self, s):
        """
        :type s: str
        :rtype bool
        """
        if len(s) == 0:
            return False

        if s[0] in ["+", "-"]:
            s=s[1:]
            if len(s) == 0:
                return False
        
        isDot = False
        LastIsDigit = False
        for i, c in enumerate(s):
            if self.isDigit(c):
                LastIsDigit = True
            elif c == ".":
                if isDot:
                    return False
                if (not LastIsDigit) and (i+1 >= len(s)):
                    return False
                isDot = True
            else:
                return False
        return isDot

    def isInteger(self, s):
        """
        :type s: str
        :rtype bool
        """
        if len(s) == 0:
            return False

        if s[0] in ["+", "-"]:
            s=s[1:]
            if len(s) == 0:
                return False

        for i, c in enumerate(s):
            if not self.isDigit(c):
                return False
        return True

    def isDigit(self, c):
        """
        :type c: str, len(c) = 1
        :rtype: bool
        """
        assert len(c) == 1, \
            "input of isDigit should be char."
        return c in [
            "0", "1", "2", "3", "4", 
            "5", "6", "7", "8", "9"
        ]
