#User function Template for python3
class Solution:
	def matSearch(self,mat, N, M, X):
		# Complete this function
		for i in range(N):
		    low=0
		    high=M-1
		    while low<=high:
		        mid=low+(high-low)//2
		        if mat[i][mid]==X:
		            return 1
		        elif mat[i][mid]<X:
		            low=mid+1
		        else:
		            high=mid-1
	    return 0
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends