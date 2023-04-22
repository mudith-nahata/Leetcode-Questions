#User function Template for python3
class Solution:

	def count(self,arr, n, x):
	    hashmap={}
	    for ele in arr:
	        if ele not in hashmap:
	            hashmap[ele]=1
	        else:
	            hashmap[ele]+=1
	    c=0
	    for k,v in hashmap.items():
	        if k==x:
	            c=v
	        else:
	            continue
	    return c
	            
	        

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends