class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        rev=0
        while x>0:
            dig=x%10
            rev=(rev*10)+dig
            x=int(x/10)
        if rev==y and y>0:
            return True
        elif y==0:
            return True
        else:
            return False
        
