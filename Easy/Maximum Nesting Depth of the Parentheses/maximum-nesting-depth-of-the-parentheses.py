#User function Template for python3

class Solution:
    def maxDepth(self, s):
        # Code here
        k=0
        h=0
        for i in range(len(s)):
            if s[i]=="(":
                k+=1
            elif s[i]==")":
                k-=1
            h=max(h,k)
        return h
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.maxDepth(s))
# } Driver Code Ends