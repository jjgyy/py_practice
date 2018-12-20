class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        array = path.split('/')
        array = [e for e in array if (e != '') & (e != '.')]
        s_path_array = []
        for e in array:
            if e == '..':
                if s_path_array:
                    s_path_array.pop()
            else:
                s_path_array.append(e)

        s_path = ''
        for e in s_path_array:
            s_path = s_path + '/' + e

        if s_path == '':
            s_path = '/'

        return s_path

# ========================================================
solution = Solution()
path = "/"
print solution.simplifyPath(path)
