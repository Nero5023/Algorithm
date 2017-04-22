class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        pathsTrack = path.split('/')
        if pathsTrack[0] == '':
            pathsTrack[0] = '/'
        for track in pathsTrack:
            if track == '':
                continue
            if track == '.':
                continue
            if track == "..":
                if len(stack) == 1 and stack[0] == '/':
                    stack = ['/']
                else:
                    stack.pop()
                continue
            stack.append(track)
        res = "/".join(stack)
        if len(res) >= 2 and res[0] == "/" and res[1] == "/":
            return res[1:]
        return res

if __name__ == '__main__':
    print Solution().simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")