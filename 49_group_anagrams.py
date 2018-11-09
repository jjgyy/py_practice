# encoding=utf-8

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        考虑用字典将不按字母表顺序排列的字母组合，转换成按照字母表排列的计数字典
        """
        result_dic = {}
        for str in strs:
            s_str = ''.join(sorted(str))
            if s_str in result_dic:
                result_dic[s_str].append(str)
            else:
                result_dic[s_str] = [str]

        result = []
        for key in result_dic:
            result.append(result_dic[key])

        print result

# =================================================================================

solution = Solution()
strs = ["cab","pug","pei","nay","ron","rae","ems","ida","mes"]
solution.groupAnagrams(strs)