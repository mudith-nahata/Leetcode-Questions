#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3
from typing import List
class Solution:
    def solve(self,M: int, K: int, bloomDay: List[int]) -> int:
        if len(bloomDay)<M*K:
            return -1
            
        low=0
        high=max(bloomDay)
        res=-1
            
        while low<=high:
            mid=low+(high-low)//2
            sum=0
            m=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mid:
                    sum+=1
                else:
                    sum=0
                        
                if sum==K:
                    m +=1
                    sum=0
                        
            if m>=M:
                res=mid
                high=mid - 1
            else:
                low=mid + 1
                
        return res
                    
                    
                    
                    
            
            
                    
                    
                    
                    
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        M, K = list(map(int, input().split()))
        bloomDay = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(M, K, bloomDay)
        print(res)
# } Driver Code Ends