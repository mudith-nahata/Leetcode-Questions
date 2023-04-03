class Solution:
    def majorityElement(self, a, n):
        #Your code here
        d={}
        for num in a:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for num in d:
            if d[num]>len(a)//2:
                return num
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