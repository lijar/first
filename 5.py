class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen=1
        palindrome=''

        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                for m in range(i+1,len(s)):
                    if s[m]==s[i]:
                        pass
                    else:
                        m-=1
                        break    
                if m-i+1 > maxlen:
                    maxlen=m-i+1
                    palindrome = s[i:m+1]
            if s[i] == s[i+1]:
                for m in range(1,i+2):
                    if  i+m < len(s) and s[i-m+1] == s[i+m] :
                        pass
                    else :
                        m-=1
                        break
                
                if 2*m >= maxlen:
                    maxlen = 2*m
                    palindrome = s[i-m+1:i+m+1] 
            if i>=1 and s[i-1] == s[i+1]:
                for m in range(1,i+1):
                    if  i+m < len(s) and s[i-m] == s[i+m] :
                        pass
                    else :
                        m-=1
                        break
                
                if 2*m+1 >= maxlen:
                    maxlen = 2*m+1
                    palindrome = s[i-m:i+m+1]
        if maxlen ==1:
            return s[0] 
        else:           
            return palindrome
solution=Solution()   
print solution.longestPalindrome("abc")
