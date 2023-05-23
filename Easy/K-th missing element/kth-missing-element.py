#User function Template for python3


def KthMissingElement (arr,  n, K) : 
    #Complete the function
    cnt=0
    nums=arr[0]
    n=len(arr)
    j=0
    while j<n:
        if nums==arr[j]:
            nums+=1
            j+=1
        else:
            cnt+=1
            if cnt==K:
                return nums
            nums+=1
    return -1
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n, K = map(int ,input().split())
    arr = list(map(int,input().strip().split()))
    res = KthMissingElement(arr, n, K)
    print(res)



# } Driver Code Ends