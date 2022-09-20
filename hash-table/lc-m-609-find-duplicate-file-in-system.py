from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)

        for path in paths:
            files = path.split(" ")
            root = files[0]
            for file in files[1:]:
                file_name, content = file.split("(")
                content = content[:-1]
                file_path = f"{root}/{file_name}"
                contents[content].append(file_path)

        return [contents[content] for content in contents if len(contents[content]) >= 2]


solution = Solution()
assert solution.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]) == [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']]
assert solution.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]) == [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt']]
