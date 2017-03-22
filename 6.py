class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        span=len(s)/2/(numRows-1)+1
        if numRows==1:
            return s
        result=[]
        for i in range(numRows):
            if i ==0 or  i == numRows-1:
                result +=s[i::2*(numRows-1)]
            else:
                for j in range(span):
                    if i+2*j*(numRows-1) < len(s):
                        result +=s[i+2*j*(numRows-1)]
                    if i+2*j*(numRows-1)+2*(numRows-i-1) <len(s):
                        result +=s[i+2*j*(numRows-1)+2*(numRows-i-1)]
        return "".join(result)    
solution=Solution()   
print solution.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers",3)

class Solution1(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        result=[]
        for i in range(numRows):
            line=list(s[i::2*(numRows-1)]) 
            add=[]
            if i != 0 and i != numRows-1:
                add=s[i+2*(numRows-i-1)::2*(numRows-1)]
            for j in range(len(add)):
                line[j]=line[j]+add[j]   
            result += line
        return "".join(result)
solution=Solution1()   
print solution.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers",3)                    