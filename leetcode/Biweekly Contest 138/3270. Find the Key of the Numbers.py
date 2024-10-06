class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1=str(num1)
        num2=str(num2)
        num3=str(num3)
        a,b=len(num1),len(num2)
        c=len(num3)
        if a<4:
            num1 = num1.zfill(4)
        if b<4:
            num2 = num2.zfill(4)
        if c<4:
            num3 = num3.zfill(4)
        final=""
  
        for i in range(4):
            final+=str(min(int(num1[i]),int(num2[i]),int(num3[i])))
            
        return int(final)
