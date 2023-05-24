#{ 
 # Driver Code Starts


#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def removeOuter(self,s):
        if len(s)==0:
            return ""
        elif len(s)!=0:
            cnt=0
            res=""
            for i in range(len(s)):
                if cnt==0:
                    cnt+=1
                    continue
                if s[i]=="(":
                    cnt+=1
                    if cnt>1:
                        res+=s[i]
                elif s[i]==")":
                    cnt-=1
                    if cnt>0:
                        res+=s[i]
        return res
#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        s = input()
        ob = Solution()
        res = ob.removeOuter(s)
        print(res)
# } Driver Code Ends