from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[int], list2: Optional[int]) -> Optional[int]:
        res = []

        while list1 or list2:
            if list1 and list2:
                if list1[0] > list2[0]:
                    res.append(list2.pop(0))
                else:
                    res.append(list1.pop(0))
            elif list1:
                res.append(list1.pop(0))
            else:
                res.append(list2.pop(0))
        return res

s = Solution()
print(s.mergeTwoLists([1,2,3,4],[1,1,1,2]))