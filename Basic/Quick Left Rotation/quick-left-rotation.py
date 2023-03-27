class Solution:
    def leftRotate(self, arr, k, n):
        if k%n:
            k=k%n
            helper=arr[:k+1]
            for i in range(0,n-k):
                arr[i]=arr[i+k]
            for i in range(0,k):
                arr[i+n-k]=helper[i]
            
            


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends