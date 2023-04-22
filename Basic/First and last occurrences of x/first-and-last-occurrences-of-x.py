#User function Template for python3


def find(arr,n,x):
    # code here
    def lh(arr,x):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        return low
    def rh(arr,x):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]<=x:
                low=mid+1
            else:
                high=mid-1
        return high
    lhs=lh(arr,x)
    rhs=rh(arr,x)
    if lhs<=rhs:
        k=lhs,rhs
        return k
    return -1,-1
    
#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends