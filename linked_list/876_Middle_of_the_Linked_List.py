class Solution:
    def middleNode(self,head):
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        n=count//2

        temp=head
        for i in range(n):
            temp=temp.next
        return temp
