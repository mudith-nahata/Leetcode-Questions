#{ 
 # Driver Code Starts


#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def removeOuter(self,s):
        stack=[]
        res=""
        for i in range(len(s)):
            if s[i]=="(" and len(stack)==0:
                stack.append(s[i])
            elif s[i]=="(" and stack[-1]=="(":
                res+=s[i]
                stack.append(s[i])
            elif s[i]==")" and stack[-1]=="(" and len(stack)!=1:
                res+=s[i]
                stack.pop()
            elif s[i]==')' and stack[-1]=="(" and len(stack)==1:
                stack.pop()
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