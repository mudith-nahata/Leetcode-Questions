#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,a,n):
	    maxi=-999
	    prod=1
	    for i in range(0,n):
	        prod*=a[i]
	        maxi=max(prod,maxi)
	        if a[i]==0:
	            prod=1
	    prod=1
	    for i in range(n-1,-1,-1):
	        prod*=a[i]
	        maxi=max(maxi,prod)
	        if a[i]==0:
	            prod=1
	    return maxi
	        
	    
		    

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends