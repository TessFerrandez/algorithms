'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        skip = set(['..', '.', ''])

        for dir in path.split('/'):
            if dir == '..' and stack:
                stack.pop()
            elif dir not in skip:
                stack.append(dir)

        stack = reversed(stack)
        res = ''
        for dir in stack:
            res = f"/{dir}{res}"

        return '/' if res == '' else res


solution = Solution()
assert solution.simplifyPath('/home//foo/') == '/home/foo'
assert solution.simplifyPath('/a/./b/../../c/') == '/c'
assert solution.simplifyPath('/home/') == '/home'
assert solution.simplifyPath('/../') == '/'
