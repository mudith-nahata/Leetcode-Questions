#User function Template for python3

class Solution:
    def Search(self, n, a, k):
        low=0
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            if a[mid]==k:
                return 1
            if a[mid]==a[low]:
                low+=1
                continue
            if a[mid]==a[high]:
                high-=1
                continue
            if a[low]<=a[mid]:
                if k>=a[low] and k<a[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if k>a[mid] and k<=a[high]:
                    low=mid+1
                else:
                    high=mid-1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        ans = ob.Search(n, arr, k)
        print(ans)
        tc -= 1
# } Driver Code Ends