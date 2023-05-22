class Solution:
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if M>N:
            return -1
        s=0
        for i in range(N):
            s+=A[i]
        high=s
        low=0
        res=-1
        while low<=high:
            mid=low+(high-low)//2
            if is_possible(A,N,M,mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
            mid=low+(high-low)//2
        return res
def is_possible(A,N,M,mid):
    alloc_student=1
    pages=0
    for i in range(N):
        if A[i]+pages<=mid:
            pages+=A[i]
        else:
            alloc_student+=1
            if alloc_student>M or A[i]>mid:
                return False
            pages=A[i]
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