class Solution:
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if(M>N):
            return(-1)
        s=0
        sum=0
        for i in range(N):
            sum+=arr[i]
        e=sum
        ans=-1
        mid=(s+e)>>1
        while(s<=e):
            if(ispossible(arr,N,M,mid)):
                ans=mid
                e=mid-1
            else:
                s=mid+1
            mid=s+(e-s)//2
        return ans
        
def ispossible(arr,N,M,mid):
    studentcount=1
    pagesum=0
    for i in range(N):
        if(pagesum+arr[i]<=mid):
            pagesum+=arr[i]
        else:
            studentcount+=1
            if(studentcount>M or arr[i]>mid):
                return False
            pagesum=arr[i]
    return True
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends