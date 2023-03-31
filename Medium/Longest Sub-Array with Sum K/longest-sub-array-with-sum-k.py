#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, a, n, k) :
        mx=0
        s=0
        di=dict()
        for j in range(n):
            s+=a[j]
            
            if s not in di:
                di[s]=j
            if s==k:
                mx=max(mx,j+1)
            elif s-k in di:
                mx=max(mx,j-di[s-k])
        #print(s,s-k)
        # print(di)
        return mx
                
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends