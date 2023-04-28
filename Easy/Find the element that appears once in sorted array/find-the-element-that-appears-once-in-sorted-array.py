#User function Template for python3

class Solution:
    def findOnce(self,a : list, n : int):
        # Complete this function
        low=0
        high=n-1
        if len(a)==1:
            return a[0]
        if a[low]!=a[low+1]:
            return a[low]
        if a[high]!=a[high-1]:
            return a[high]
        while low<=high:
            mid=low+(high-low)//2
            if a[mid]!=a[mid-1] and a[mid]!=a[mid+1]:
                return a[mid]
            elif(a[mid]==a[mid+1] and mid%2==0) or (a[mid]==a[mid-1] and mid%2!=0):
                low=mid+1
            else:
                high=mid-1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# } Driver Code Ends