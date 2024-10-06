class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        arr=nums
        
        def check(i):
            return nums[i+k-1] - nums[i] == k-1


        mysum=sum(arr[:k-1])
        out=(k*(k-1))//2  

        for i in range(n-k+1):
            if i+k-1<n:
                mysum+=arr[i+k-1]
            else:
                mysum=0
            if check(i) and mysum==out+k*arr[i]:
                res.append(arr[i+k-1])
            else:
                res.append(-1)
            mysum-=arr[i]
        return res

        
