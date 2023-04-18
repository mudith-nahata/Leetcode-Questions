class Solution:
	def overlappedInterval(self,intervals):
		#Code here
		intervals=sorted(intervals)
		k=[]
		for i in range(len(intervals)):
		    if not k:
                k.append(intervals[i])
    		elif k[-1][1]<intervals[i][0]:
    		    k.append(intervals[i])
		    else:
		        k[-1][1]=max(k[-1][1],intervals[i][1])
	    return k
		        
		    
#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends