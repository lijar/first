# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
       self.val = x
       self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        temp=head
        while l1 and l2:
            val=l1.val+l2.val
            if val >= 10:
                val = val%10
                if l1.next and l2.next:
                    l1.next.val +=1     
                elif l1.next:
                    l1.next=ListNode(1)
                else:
                    l2.next=ListNode(1)
            node= ListNode(val)
            temp.next=node
            temp=node
            l1=l1.next
            l2=l2.next
            
        if l1:
            temp.next=l1    
        if l2:
            temp.next=l2
            
        return head.next
        
solution = Solution()
node1=ListNode(8)
node2=ListNode(1)
node3=ListNode(6)
node1.next=node2
node2.next=node3


nodex=ListNode(1)



reNode= solution.addTwoNumbers(node1,nodex)

while reNode != None:
    print reNode.val
    reNode=reNode.next
