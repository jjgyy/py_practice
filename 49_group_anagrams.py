# encoding=utf-8

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        考虑用字典将不按字母表顺序排列的字母组合，转换成按照字母表排列的计数字典
        """
        result_dic = {}
        for str_item in strs:
            c_dic = {}
            c_record_str = ""
            for c in str_item:
                if c_dic.has_key(c):
                    c_dic[c] += 1
                else:
                    c_dic[c] = 1
            # 字典的key排序有点迷，排下序
            sorted_c_list = sorted(c_dic.items(), key=lambda x: x[0])
            for sorted_c_item in sorted_c_list:
                c_record_str += (sorted_c_item[0] + str(sorted_c_item[1]))

            if result_dic.has_key(c_record_str):
                result_dic[c_record_str].append(str_item)
            else:
                result_dic[c_record_str] = [str_item]
            print(str_item),
            print(c_record_str)

        result = []
        for key in result_dic:
            result.append(result_dic[key])

        print(result)

# =================================================================================

solution = Solution()
strs = ["cab","pug","pei","nay","ron","rae","ems","ida","mes"]
solution.groupAnagrams(strs)