#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        low=0
        high=n-1
        while(low <= high):
            mid=low + ((high - low)// 2)
            prev=(mid - 1 + n) % n
            next = (mid + 1) % n
            if(arr[mid]<=arr[prev]
               and arr[mid]<=arr[next]):
                return mid
            elif (arr[mid]<=arr[high]):
                high=mid- 1
            elif (arr[mid]>=arr[low]):
                low=mid+1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends