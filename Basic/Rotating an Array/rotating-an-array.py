#User function Template for python3

class Solution:
    def leftRotate(self, arr, n, k):
        if k>n:
            k=k%n
        temp=[]*k
        for i in range(0,k):
            temp.append(arr[i])
            
        for i in range(k,n):
            arr[i-k]=arr[i]
        for i in range(0,k):
            arr[n-k+i]=temp[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends