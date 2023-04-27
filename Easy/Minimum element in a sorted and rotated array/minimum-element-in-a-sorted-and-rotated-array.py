#User function Template for python3

class Solution:
    def findMin(self, nums, n):
        #complete the function here
        if n==1:
            return arr[0]
        if arr[0]<arr[n-1]:
            return arr[0]
        start=0
        end=n-1
        while start<end:
            mid=(start+end)//2
            if arr[start]<arr[mid]:
                start=mid
            else:
                end=mid
        return arr[start+1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends