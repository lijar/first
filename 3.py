class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic={}
        start=0
        res=0
        for i, ch in enumerate(s):
            if ch in dic:
                lens=i-start
                if lens > res:
                    res=lens
                start= max(start,dic[ch]+1)
                 
            dic[ch]=i
                
        return max(res, len(s)-start) 
    
solution=Solution()   
print solution.lengthOfLongestSubstring("abbcaa")

"""
    def lengthOfLongestSubstring(self, s):        
        if s != '':
            length = 1
        else:
            length =0
        sub=list(s)
        lens=len(s)
        for i in range(lens):
            count=1
            for j in range(i+1,lens):
                if s[j] not in sub[i]:
                    sub[i]=sub[i]+s[j]
                    count +=1
                    if count > length:
                        length=count
                else:
                    break
        return length
"""            
