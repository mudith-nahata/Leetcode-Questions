#User function Template for python3
class Solution:
    def findTwoElement( self,a, n): 
        # code here
        k1=0
        k2=0
        for i in range(n):
            if a[abs(a[i])-1]>0:
                a[abs(a[i])-1]=-a[abs(a[i])-1]
            else:
                k1=abs(a[i])
        for i in range(n):
            if a[i]>0:
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