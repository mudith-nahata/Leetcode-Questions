#User function Template for python3
from typing import List
class Solution:
    def findTwoElement( self,arr,n):
        k1,k2=0,0
        for i in range(n):
            if arr[abs(arr[i])-1]>0:
                arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
            else:
                k1=abs(arr[i])
        for i in range(0,n):
            if arr[i]>0:
                k2=i+1
        return [k1,k2]
        
            
            
                    
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends