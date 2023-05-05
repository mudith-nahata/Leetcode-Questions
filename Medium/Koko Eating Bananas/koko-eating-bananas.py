#User function Template for python3
import math
class Solution:
    def Solve(self, N, piles, H):
        # Code here
        low=1
        high=max(piles)
        res=0
        while low<=high:
            mid=low+(high-low)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/mid)
            if hours<=H:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        piles = list(map(int, input().split()))
        H = int(input())
        ob = Solution()
        print(ob.Solve(N, piles, H))
# } Driver Code Ends