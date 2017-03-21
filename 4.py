class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''O(m+n)'''
        nums=[]
        i,j=0,0
        while i<len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i+=1;
            else:
                nums.append(nums2[j])
                j+=1;
        while i<len(nums1):
            nums.append(nums1[i])
            i+=1
        while j<len(nums2):
            nums.append(nums2[j]) 
            j+=1
        index=len(nums)
        print nums
        if index%2==0:
            return ((nums[index/2-1])+(nums[index/2]))/2.0
        else:
            return nums[index/2]
class Solution2:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l=len(A)+len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2-1)+self.findKth(A,B,l//2))/2.0
            
    '''Olog(m+n)'''        
    def findKth(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            #Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)    
solution=Solution()
print solution.findMedianSortedArrays([1,2],[3,4])