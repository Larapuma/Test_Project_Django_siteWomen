from typing import Optional


class Solution:
    @staticmethod
    def deleteDuplicates(head: Optional[list[int]]) -> Optional[list[int]]:
        sort_list_without_dublicates = [0]*(head[-1]+1)
        for i in range(len(head)):
            sort_list_without_dublicates[head[i]]+=1
        res = []
        for i in range(len(sort_list_without_dublicates)):
            if sort_list_without_dublicates[i]!=0:
                res.append(i)
        return res

print(Solution.deleteDuplicates([1,1,2,3,4,4,4,5]))