#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
    i,j,count,zero=0,0,0,0
    while j<n:
        if arr[j]==0:
            zero+=1
        while zero>m:
            if arr[i]==0:
                zero-=1
            i+=1
        count=max(count,j-i+1)
        j+=1
    return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends