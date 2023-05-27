#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        if len(a)!=len(b):
            return False
        k1=[0]*256
        k2=[0]*256
        for i in range(len(a)):
            k1[ord(a[i])]+=1
        for i in range(len(b)):
            k2[ord(b[i])]+=1
        for i in range(256):
            if k1[i]!=k2[i]:
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends