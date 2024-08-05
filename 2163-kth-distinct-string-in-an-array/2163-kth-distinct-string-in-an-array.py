class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        dt = {}

        if len(arr) == 1:
            return arr[0]

        for i in range(len(arr)):
            if arr[i] not in dt:
                dt[arr[i]] = 1
            else:
                dt[arr[i]] +=1

        l = []
        for i in range(len(arr)):
            if dt[arr[i]] == 1:
                l.append(arr[i])

        if len(l)<k:
            return ""
        else:
            return l[k-1]



        
                 
        
        