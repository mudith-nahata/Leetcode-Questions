#User function Template for python3
#Complete this function
class Solution:
    def floorSqrt(self, x):
        low=1
        high=x
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                high=mid-1
            else:
                ans=mid
                low=mid+1
        return ans
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends