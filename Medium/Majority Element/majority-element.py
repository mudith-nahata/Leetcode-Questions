class Solution:
    def majorityElement(self, a, n):
        #Your code here
        c=0
        res=0
        for i in range(n):
            if c==0:
                res=a[i]
            if a[i]==res:
                c+=1
            else:
                c-=1
        c=0
        for i in a:
            if i == res:
                c+=1
        if c>n//2:
            return res
        else:
            return -1
        

                    
                
            
                
                
            
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends