class Solution(object):
    result = []
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.scan(0, s, [])
        return self.result

    def scan(self, section, s, ip):
        if section == 4:
            if s == '':
                self.result.append('.'.join(ip))
                return
            else:
                return
        if (len(s) >= 1) and self.isIpSection(s[:1]):
            self.scan(section+1, s[1:], ip + [s[:1]])
        if (len(s) >= 2) and self.isIpSection(s[:2]):
            self.scan(section+1, s[2:], ip + [s[:2]])
        if (len(s) >= 3) and self.isIpSection(s[:3]):
            self.scan(section+1, s[3:], ip + [s[:3]])


    def isIpSection(self, s):
        if (len(s) > 1) and (s[0] == '0'):
            return False
        section = int(s)
        if (0 <= section) and (section <= 255):
            return True
        return False

        

# ========================================================
solution = Solution()
s = "010010"
print solution.restoreIpAddresses(s)
