#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        pos=[]
        neg=[]
        for i in range(n):
            if arr[i]<0:
                neg.append(arr[i])
            else:
                pos.append(arr[i])
        arr.clear()
        pos_len=len(pos)
        neg_len=len(neg)
        minn=min(pos_len,neg_len)
        i=0
        while(i<minn):
            arr.append(pos[i])
            arr.append(neg[i])
            i+=1
        if minn==pos_len:
            i=pos_len
            while(i<neg_len):
                arr.append(neg[i])
                i+=1
        else:
            i=neg_len
            while(i<pos_len):
                arr.append(pos[i])
                i+=1
        return arr 
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends