class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        ans=-1
        for i in range(N):
            if A[i]<=X:
                ans=i
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends