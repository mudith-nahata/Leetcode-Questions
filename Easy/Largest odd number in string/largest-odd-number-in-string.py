#User function Template for python3

class Solution:
    def maxOdd(self, s):
        if int(s[-1])%2!=0:
            return str(s)
        else:
            ans=-1
            for i in range(len(s)):
                if(int(s[i])%2!=0):
                    ans=i
            if ans==-1:
                return ""
            else:
                return str(s[0:ans+1])
            
                    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.maxOdd(s))
# } Driver Code Ends