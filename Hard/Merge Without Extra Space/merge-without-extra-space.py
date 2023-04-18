#User function Template for python3
import math
class Solution:
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        t=n+m
        gap=math.ceil(t/2)
        while gap>0:
            i=0
            j=gap
            while j<n+m:
                if i<n and j<n:
                    if arr1[i]>arr1[j]:
                        arr1[i],arr1[j]=arr1[j],arr1[i]
                elif j>=n and i<n:
                    if arr1[i]>arr2[j-n]:
                        arr1[i],arr2[j-n]=arr2[j-n],arr1[i]
                elif j>=n and i>=n:
                    if arr2[i-n]>arr2[j-n]:
                        arr2[i-n],arr2[j-n]=arr2[j-n],arr2[i-n]
                i=i+1
                j=j+1
            if gap==1:
                break
            else:
                gap=math.ceil(gap/2)
                

                    
                    
                
                    


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends