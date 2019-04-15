class Solution(object):
    def hasSubstring(self, sentence, pattern):
        patternArray = self.getPatternArray(pattern)
        i = 0
        j = 0
        sentenceLength = len(sentence)
        patternLength = len(pattern)
        while i < sentenceLength:
            while True:
                if sentence[i] != pattern[j]:
                    j = patternArray[j]
                    i += 1
                    break
                if j == patternLength - 1:
                    return True
                i += 1
                j += 1
        return False

    def getPatternArray(self, pattern):
        result = [0]
        i = 0
        j = 1
        while j < len(pattern):
            if pattern[j] == pattern[i]:
                result.append(i+1)
                i += 1
            else:
                i = 0
                result.append(0)
            j += 1
        return result

# ========================================================
solution = Solution()

print solution.hasSubstring('hhhwudadnjsandjkasabcdasdwhuwqhduihsajnncjnjncnsjakdnjaksndkjsandjknsajdnsakjdnjksanjknsajxjkcnjknxjcknzxncjkncnjknjndkjasndkjnaskjdnkjadnawjkdjkwadjkskn', 'du')
